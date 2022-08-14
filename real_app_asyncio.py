import asyncio
import time
from aiohttp import ClientSession


API_KEY = 'babdbc71a58e349a2ac31633d780f6a7'


async def get_weather(city):
    async with ClientSession() as session:
        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=ru'
        # params = {
        #     'g': city,
        #     'appid': 'babdbc71a58e349a2ac31633d780f6a7'
        # }

        # async with session.get(url=url, params=params) as response:
        async with session.get(url=url) as response:
            weather_json = await response.json()
            print(f'{city}: {weather_json["weather"][0]["main"]}')
            # print(weather_json)


async def main(_cites):
    tasks = []
    for city in _cites:
        tasks.append(asyncio.create_task(get_weather(city=city)))

    for task in tasks:
        await task


cities = ['Moscow', 'St. Petersburg', 'Rostov-on-Don', 'Kaliningrad', 'Vladivostok',
          'Minsk', 'Beijing', 'Delhi', 'Istanbul', 'Tokyo', 'London', 'New York']

if __name__ == '__main__':
    print(time.strftime('%X'))
    try:
        asyncio.run(main(cities))
    except RuntimeError:
        pass
    print(time.strftime('%X'))
