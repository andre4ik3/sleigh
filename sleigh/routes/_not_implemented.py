from aiohttp import web


async def not_implemented(request):
    return web.Response(
        text="{\n    \"error\": \"not_implemented\"\n    }",
        content_type="application/json"
    )
