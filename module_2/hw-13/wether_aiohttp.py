import aiohttp
import asyncio
from bs4 import BeautifulSoup
from config import METEOPROG_URL, METEO_URL


async def fetch_to_meteoprog():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEOPROG_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="today-temperature").text.replace(' ', '') \
                .replace('\n', '').replace('C', '')

            print(result)


async def fetch_to_meteo():
    async with aiohttp.ClientSession() as session:
        async with session.get(METEO_URL) as response:
            text = await response.read()
            result = BeautifulSoup(text, "lxml").find('div', class_="weather-detail__main-degree").text\
                .replace(' ', '')

            print(result)


async def main():
    sites = asyncio.gather(fetch_to_meteoprog(), fetch_to_meteo())
    await sites


if __name__ == "__main__":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
