from ujson import loads, dumps, dump
from datetime import datetime
from pathlib import Path
from aiohttp import web
from .. import cookie
from json import dump
import aiofiles


async def event_upload(request):
    machine_id = request.match_info["machine_id"]
    cookie_valid = await cookie.check(request, machine_id)

    try:
        data = await request.json(loads=loads)
    except ValueError:
        return web.json_response({"error": "invalid_body"}, dumps=dumps, status=400)

    if not cookie_valid:
        return web.json_response({"error": "no_cookie"}, dumps=dumps, status=400)

    date = datetime.now()
    year = date.strftime("%Y")
    month = date.strftime("%m")
    day = date.strftime("%d")
    
    path = Path(f"config/events/{year}/{month}/{day}").resolve()
    path.mkdir(parents=True, exist_ok=True)

    if Path(f"{path}/{machine_id}.json").is_file():
        async with aiofiles.open(f"{path}/{machine_id}.json") as file:
            existing = loads(await file.read())
    else:
        existing = []

    new = data.get("events", [])

    async with aiofiles.open(f"{path}/{machine_id}.json", "w") as file:
        await file.write(dumps([*new, *existing], sort_keys=True, indent=2))

    return web.Response(text="{}", content_type="application/json")
