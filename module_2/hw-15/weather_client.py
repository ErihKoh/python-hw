import aiohttp
import asyncio
from bs4 import BeautifulSoup
from config import METEOPROG_URL, METEO_URL


async def fetch_to_meteoprog():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEOPROG_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, 'lxml').find('section', class_="today-block")

            head = result.find('h2').text
            current_temp = result.find('div', class_="today-temperature").text.replace('\n', '').strip()
            desc = result.find('h3').text

            return head, current_temp, desc


async def fetch_to_meteo():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEO_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="weather-detail__main")
            head = result.find('div', class_="weather-detail__main-title").text.replace('\n', '')
            current_temp = result.find('div', class_="weather-detail__main-temp").text
            desc = result.find('div', class_="weather-detail__main-specification").text

            return head, current_temp, desc


async def main():
    sites = asyncio.gather(fetch_to_meteoprog(), fetch_to_meteo())
    return await sites


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
responses = asyncio.run(main())
meteoprog_response = responses[0]
meteo_response = responses[1]

