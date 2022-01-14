import jinja2
import aiohttp_jinja2
from aiohttp import web

from weather_client import meteoprog_response, meteo_response


async def get_temp(request: web.Request) -> web.Response:

    context = {
        'head_1': meteoprog_response[2],
        'head_2': meteoprog_response[3],
        'cur_temp': meteoprog_response[4],
        'desc_weather': meteoprog_response[5],
        'param': meteoprog_response[0],
        'param_val': meteoprog_response[1],
        # 'temp2': meteo_response
    }
    response = aiohttp_jinja2.render_template("index.html", request,
                                          context=context)

    return response

if __name__ == "__main__":

    # run on http://127.0.0.1:8080/

    app = web.Application()

    # setup jinja2
    aiohttp_jinja2.setup(app,
                         loader=jinja2.FileSystemLoader(
                             'templates'
                         ))

    app.router.add_get('/', get_temp)

    web.run_app(app)
