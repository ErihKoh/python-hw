from fastapi import FastAPI
import aiohttp
from bs4 import BeautifulSoup
from config import METEOPROG_URL, METEO_URL
from models import MeteoprogWeather, MeteoWeather


app = FastAPI()


@app.get('/meteo', response_model=MeteoWeather)
async def get_weather_by_meteo():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEO_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="weather-detail__main")
            head = result.find('div', class_="weather-detail__main-title").text.replace('\n', '')
            current_temp = result.find('div', class_="weather-detail__main-temp").text
            desc = result.find('div', class_="weather-detail__main-specification").text
    return MeteoWeather(
        head=head,
        current_temp=current_temp,
        desc=desc
    )


@app.get('/meteoprog', response_model=MeteoprogWeather)
async def get_weather_by_meteoprog():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEOPROG_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, 'lxml').find('section', class_="today-block")
            head = result.find('h2').text
            current_temp = result.find('div', class_="today-temperature").text.replace('\n', '').strip()
            desc = result.find('h3').text
    return MeteoprogWeather(
        head=head,
        current_temp=current_temp,
        desc=desc
    )
