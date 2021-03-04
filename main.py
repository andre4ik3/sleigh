from ujson import load
from sleigh import routes
from pathlib import Path
from aiohttp import web
import sys

if not Path("config").resolve().is_dir():
    print("Error: No config folder!")
    print("Error: Look in the GitHub repository for a sample config folder")
    print("Error: https://github.com/andre4ik3/sleigh")
    sys.exit(1)

with open("config/server.json") as fp:
    config = load(fp)

doRuleDownload = config.get("doRuleDownload", True)
doEventUpload = config.get("doEventUpload", True)
doPostflight = config.get("doPostflight", False)

app = web.Application()

rule_download = routes.rule_download if doRuleDownload else routes.not_implemented
event_upload = routes.event_upload if doEventUpload else routes.not_implemented
postflight = routes.postflight if doPostflight else routes.not_implemented

app.add_routes(
    [
        web.post("/preflight/{machine_id}", routes.preflight),
        web.post("/ruledownload/{machine_id}", rule_download),
        web.post("/eventupload/{machine_id}", event_upload),
        web.post("/postflight/{machine_id}", postflight),
    ]
)


if __name__ == "__main__":
    web.run_app(app)
