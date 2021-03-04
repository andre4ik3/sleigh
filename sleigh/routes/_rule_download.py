from ujson import loads, dumps
from pathlib import Path
from aiohttp import web
from .. import cookie
import aiofiles


async def rule_download(request):
    """Return rules from the rules directory according to the machine."""
    machine_id = request.match_info["machine_id"]
    cookie_valid = await cookie.check(request, machine_id)

    if not cookie_valid:
        return web.json_response(
            {"error": "no_cookie"}, dumps=dumps, status=400
        )

    saved_cookie = await cookie.get(request, machine_id)
    serial = saved_cookie["data"]["serial_num"]
    hostname = saved_cookie["data"]["hostname"]
    user = saved_cookie["data"]["primary_user"]

    rules = []
    files = []

    paths = [
        Path(f"config/rules/{machine_id}"),
        Path(f"config/rules/{serial}"),
        Path(f"config/rules/{hostname}"),
        Path(f"config/rules/{user}"),
        Path("config/rules/global"),
    ]

    for path in paths:
        if path.is_dir():
            path = path.resolve()

            for file in path.glob("**/*.json"):
                files.append(file)

    for filename in files:
        async with aiofiles.open(filename, "r") as file:
            json = loads(await file.read())

            if type(json) == list:
                for rule in json:
                    rules.append(rule)

            else:
                rules.append(json)

    return web.json_response({"rules": rules}, dumps=dumps)
