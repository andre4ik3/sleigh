from ujson import loads, dumps
from aiohttp import web
import uuid


async def set(request, machine_id) -> dict:
    """Returns a header to set the cookie."""
    app = request.app
    cookie = str(uuid.uuid4())

    body = await request.json(loads=loads)

    if app.get("cookies", None) is None:
        app["cookies"] = {}

    app["cookies"][machine_id] = {"cookie": cookie, "data": body}

    return {
        "Set-Cookie": f"machine={cookie}; max-age=60; samesite=strict; path=/; secure",
    }


async def get(request, machine_id) -> dict:
    """Returns the saved data of a cookie from a request."""
    app = request.app
    return app.get("cookies", {}).get(machine_id, {})
