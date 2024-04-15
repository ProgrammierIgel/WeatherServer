# import the module
import python_weather
import datetime

import asyncio
import os



async def getweather():
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        loc = "zeitz"
        weather = await client.get(loc)

    # returns the current day's forecast temperature (int)
    temp = round((weather.current.temperature - 32)/(9/5))
    print("Heute sind in {} {}°C  ({})".format(loc, temp, weather.current.description))
    # get the weather forecast for a few days

    for forecast in weather.forecasts:
        print(f'am {forecast.date} waren es...')
        # hourly forecasts
        for hourly in forecast.hourly:
            temp = round((hourly.temperature - 32)/(9/5))
            print(f'...um {hourly.time} sind {temp} °C')



async def getweather1(loc="Zeitz"):
    async with python_weather.Client(unit=python_weather.IMPERIAL) as client:
        loc = loc
        try:
            
            weather = await client.get(loc)
        except:
            print("No Internetconection")
            return
        return weather


if __name__ == '__main__':
    # see https://stackoverflow.com/questions/45600579/asyncio-event-loop-is-closed-when-getting-loop
    # for more details
    if os.name == 'nt':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(getweather())
