from ujson import loads, dumps
from pathlib import Path
from aiohttp import web
import aiofiles


async def rule_download(request):
    """Return rules from the rules directory according to the machine."""
    machine_id = request.match_info["machine_id"]
    cookie = request.app.get("cookies", {}).pop(machine_id, None)
    browser_cookie = request.cookies.get("machine", None)

    if (
        cookie is None
        or browser_cookie is None
        or cookie.get("cookie", None) != browser_cookie
    ):
        return web.json_response({"error": "no_cookie"}, dumps=dumps, status=400)

    serial = cookie["data"]["serial_num"]
    hostname = cookie["data"]["hostname"]
    user = cookie["data"]["primary_user"]

    # At this point we know that we have seen the client before.
    # The data in the cookie has the machine serial number and hostname.
    # Now we start looking for files to merge & send back.

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
