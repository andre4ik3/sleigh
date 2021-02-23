from ujson import loads, dumps
from aiohttp import web
from pathlib import Path
from .. import cookie
import aiofiles


async def preflight(request):
    """Handle preflight requests from santactl-sync"""
    machine_id = request.match_info["machine_id"]

    try:
        body = await request.json(loads=loads)
        serial = body["serial_num"]
        hostname = body["hostname"]
        user = body["primary_user"]
        mode = body["client_mode"]

    except (ValueError, KeyError):
        return web.json_response({"error": "invalid_body"}, dumps=dumps, status=400)

    filename = ""

    if Path(f"config/preflight/{machine_id}.json").is_file():
        filename = f"config/preflight/{machine_id}.json"

    elif Path(f"config/preflight/{serial}.json").is_file():
        filename = f"config/preflight/{serial}.json"

    elif Path(f"config/preflight/{hostname}.json").is_file():
        filename = f"config/preflight/{hostname}.json"

    elif Path("config/preflight/_default.json").is_file():
        filename = "config/preflight/_default.json"

    else:
        return web.json_response({"error": "not_found"}, dumps=dumps, status=404)

    async with aiofiles.open(filename) as file:
        config = await file.read()
        set_cookie = await cookie.set(request, machine_id)

        return web.Response(
            text=config,
            content_type="application/json",
            headers=set_cookie,
        )
