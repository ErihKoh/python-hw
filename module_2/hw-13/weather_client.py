import aiohttp
import asyncio
from bs4 import BeautifulSoup
from config import METEOPROG_URL, METEO_URL


async def fetch_to_meteoprog():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEOPROG_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, 'html.parser').find('section',
                                                             class_="today-block white-icons block-weather-bg-day_cloud")
            head_1 = result.find('h1').text
            head_2 = result.find('h2').text
            current_temp = result.find('div', class_="today-temperature").text
            desc = result.find('h3').text

            hhhh = result.findAll('th')
            # print(hhhh)
            dddd = result.findAll('td')
            # print(dddd)



            return hhhh, dddd


async def fetch_to_meteo():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEO_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="weather-detail__main-degree").text \
                .replace(' ', '')

            # print(result)
            return result


async def main():
    sites = asyncio.gather(fetch_to_meteoprog(), fetch_to_meteo())
    return await sites


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
responses = asyncio.run(main())
meteoprog_response = responses[0]
meteo_response = responses[1]
