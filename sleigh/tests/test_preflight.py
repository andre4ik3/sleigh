from ujson import dumps, loads
from pathlib import Path
from aiohttp import web
from .. import routes
from . import random
import pytest

################################################################################
## App Generator                                                               #
################################################################################


@pytest.fixture
def cli(loop, aiohttp_client):
    app = web.Application()
    app.router.add_post("/preflight/{machine_id}", routes.preflight)
    return loop.run_until_complete(aiohttp_client(app))


################################################################################
## Tests                                                                       #
################################################################################


async def test_invalid_method(cli):
    for i in range(0, 1000):
        preflight = random.Preflight()
        resp = await cli.get(f"/preflight/{preflight._data['machine_id']}")
        assert resp.status == 405
        assert resp.cookies == {}


async def test_invalid_body_format(cli):
    for i in range(0, 1000):
        preflight = random.Preflight()
        resp = await cli.post(
            f"/preflight/{preflight._data['machine_id']}", data="testing"
        )
        assert resp.status == 400
        assert resp.cookies == {}


async def test_invalid_body_data(cli):
    for i in range(0, 1000):
        preflight = random.Preflight()
        resp = await cli.post(f"/preflight/{preflight._data['machine_id']}", data="{}")
        assert resp.status == 400
        assert resp.cookies == {}


async def test_valid(cli):
    for i in range(0, 1000):
        preflight = random.Preflight()
        expected_result = preflight.make_configs("config/preflight")
        resp = await cli.post(
            f"/preflight/{preflight._data['machine_id']}", data=dumps(preflight._data)
        )

        assert resp.status == 200
        assert await resp.json(loads=loads) == expected_result
        assert resp.cookies["machine"] != None
