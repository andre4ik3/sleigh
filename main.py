from ujson import loads, dumps
from sleigh import routes
from pathlib import Path
from aiohttp import web
import sys

if not Path("config").resolve().is_dir():
    print("Error: No config folder!")
    print("Error: Look in the GitHub repository for a sample config folder")
    print("Error: https://github.com/andre4ik3/sleigh")
    sys.exit(1)

app = web.Application()
app.add_routes(
    [
        web.post("/preflight/{machine_id}", routes.preflight),
        web.post("/ruledownload/{machine_id}", routes.rule_download),
    ]
)

if __name__ == "__main__":
    web.run_app(app)
