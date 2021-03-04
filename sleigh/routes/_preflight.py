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

    config = {}
    paths = [
        Path("config/preflight/_default.json"),
        Path(f"config/preflight/{machine_id}.json"),
        Path(f"config/preflight/{hostname}.json"),
        Path(f"config/preflight/{serial}.json"),
    ]

    for path in paths:
        path = path.resolve()
        if path.is_file():
            async with aiofiles.open(path) as file:
                config.update(loads(await file.read()))

    if config == {}:
        return web.json_response({"error": "not_found"}, dumps=dumps, status=404)

    set_cookie = await cookie.set(request, machine_id)

    return web.json_response(config, headers=set_cookie, dumps=dumps)
