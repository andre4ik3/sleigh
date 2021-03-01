from ujson import dumps, loads
from datetime import datetime
from pathlib import Path
from aiohttp import web
from time import sleep
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
    app.router.add_post("/eventupload/{machine_id}", routes.event_upload)
    return loop.run_until_complete(aiohttp_client(app))


################################################################################
## Tests                                                                       #
################################################################################


async def test_invalid_method(cli):
    for i in range(0, 1000):
        preflight = random.Preflight()
        resp = await cli.get(f"/eventupload/{preflight._data['machine_id']}")
        assert resp.status == 405
        assert resp.cookies == {}


async def test_invalid_body_format(cli):
    for i in range(0, 1000):
        preflight = random.Preflight()
        resp = await cli.post(f"/eventupload/{preflight._data['machine_id']}", data="testing")
        assert resp.status == 400
        assert resp.cookies == {}


async def test_invalid_body_data(cli):
    for i in range(0, 1000):
        preflight = random.Preflight()
        resp = await cli.post(f"/eventupload/{preflight._data['machine_id']}", data="{}")
        assert resp.status == 400
        assert resp.cookies == {}


async def test_valid(cli):
    for i in range(0, 1000):
        # Preflight to get Cookie
        preflight = random.Preflight()
        pf_expected_result = preflight.make_configs("config/preflight")
        pf_resp = await cli.post(
            f"/preflight/{preflight._data['machine_id']}", data=dumps(preflight._data)
        )

        assert pf_resp.status == 200
        assert await pf_resp.json(loads=loads) == pf_expected_result
        cookie = pf_resp.cookies["machine"]
        assert cookie != None

        # Now the actual Event Upload
        event = random.Event()

        date = datetime.now()
        year = date.strftime("%Y")
        month = date.strftime("%m")
        day = date.strftime("%d")

        path = Path(
            f"config/events/{year}/{month}/{day}/{preflight._data['machine_id']}.json"
        ).resolve()

        resp = await cli.post(
            f"/eventupload/{preflight._data['machine_id']}",
            data=dumps({"events": [event._data]}),
            cookies={"machine": cookie.value},
        )

        assert resp.status == 200
        assert await resp.json(loads=loads) == {}

        with open(path) as fp:
            parsed = loads(fp.read())
            assert event._data in parsed
