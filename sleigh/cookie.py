from ujson import loads, dumps
from aiohttp import web
from uuid import uuid4
import asyncio


async def set(request, machine_id: str) -> dict:
    """Returns a header to set the cookie."""
    app = request.app
    cookie = str(uuid4())

    body = await request.json(loads=loads)

    if app.get("cookies", None) is None:
        app["cookies"] = {}

    app["cookies"][machine_id] = {"cookie": cookie, "data": body}

    asyncio.get_event_loop().create_task(purge(app, machine_id))

    return {
        "Set-Cookie": f"machine={cookie}; max-age=60; samesite=strict; path=/; secure",
    }


async def get(request, machine_id: str) -> dict:
    """Returns the saved data of a cookie from a request."""
    app = request.app
    return app.get("cookies", {}).get(machine_id, {})


async def purge(app, machine_id: str) -> None:
    """Removes a cookie after 60 seconds of waiting."""
    await asyncio.sleep(60)
    app["cookies"].pop(machine_id, None)


async def check(request, machine_id: str) -> bool:
    """Checks that browser and stored cookies match."""
    saved_cookie = request.app["cookies"].get(machine_id, {}).get("cookie", None)
    browser_cookie = request.cookies.get("machine", None)

    if saved_cookie == browser_cookie:
        return True
    else:
        return False
