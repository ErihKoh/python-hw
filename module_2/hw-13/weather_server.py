import jinja2
import aiohttp_jinja2
from aiohttp import web

from weather_client import responses


async def greet_user(request: web.Request) -> web.Response:

    context = {
        'temp1': responses[0],
        'temp2': responses[1]
    }
    response = aiohttp_jinja2.render_template("index.html", request,
                                          context=context)

    return response

if __name__ == "__main__":

    app = web.Application()

    # setup jinja2
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader(
                             'templates'
                         ))

    app.router.add_get('/', greet_user)

    web.run_app(app)
