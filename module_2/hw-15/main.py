from fastapi import FastAPI
from models import MeteoprogWeather, MeteoWeather
from weather_client import meteoprog_response, meteo_response

app = FastAPI()


@app.get('/meteo', response_model=MeteoWeather)
async def get_weather_by_meteo():
    return MeteoWeather(
        head=meteo_response[0],
        current_temp=meteo_response[1],
        desc=meteo_response[2]
    )


@app.get('/meteoprog', response_model=MeteoprogWeather)
async def get_weather_by_meteoprog():
    return MeteoprogWeather(
        head=meteo_response[0],
        current_temp=meteo_response[1],
        desc=meteo_response[2]
    )
