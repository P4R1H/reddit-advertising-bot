#importing directories
import os
import asyncio
from webserver import keep_alive
from modules import advertisehot, advertisenew, login
import json
import logger


dmcontent = os.getenv("dmcontent")
dmtitle = os.getenv("dmtitle")
subreddits = {}

for c in os.getenv("subreddits").split(" , "):
    subreddits[c.split(":")[0]] = c.split(":")[1]


async def advertise():
    while(1):

        for sub in subreddits:
            await advertisehot(sub, int(subreddits[sub]), dmtitle, dmcontent)      
        await asyncio.sleep(3600)

        for sub in subreddits:
            await advertisenew(sub, 15, dmtitle, dmcontent)
        await asyncio.sleep(3600)


async def main():
    keep_alive()
    await login()
    adv_task = asyncio.create_task(advertise())
    await adv_task



asyncio.run(main())



"""
advertise.start()

@advertise.before_loop
async def before_advertise():
    await client.wait_until_ready()
"""



#running bot
# keep_alive() # remove later unless using uptimerbot
