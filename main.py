#importing directories
import discord
from discord.ext import commands
import os
import asyncio
from webserver import keep_alive
from discord.ext import tasks
from modules import advertisehot, advertisenew, login
import json
intents = discord.Intents.all()
client = commands.Bot(command_prefix='-', intents=intents)


f= open("config.json","r")
settings = json.load(f)
f.close()
subreddits = {}
for setting in settings:
    if setting == "channelid":
        channel = settings[setting]
    elif setting  == "dmcontent":
        dmcontent = settings[setting]
    elif setting  == "dmtitle":
        dmtitle = settings[setting] 
    elif setting in ["cluster_name","token","mongo_link","current_camp","secret","clientid","password","username","agent"]:
        pass
    else:
        subreddits[setting] = settings[setting] 

 

@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))
    await login()
    advertise.start()
    print("started loop")


#Advertising part
@tasks.loop(seconds = 0)
async def advertise():
    ctx = client.get_channel(channel)
    while(1):

        await ctx.send("```Hot invite batch incoming```")
        for sub in subreddits:
            await advertisehot(ctx, sub, int(subreddits[sub]), dmtitle, dmcontent)      
        await ctx.send("```waiting 1 hour to send next batch of invites```")
        await asyncio.sleep(3600)



        await ctx.send("```new invite batch incoming```")
        for sub in subreddits:
            await advertisenew(ctx, sub, 15, dmtitle, dmcontent)
        await ctx.send("```waiting 1 hour to send next batch of invites```")
        await asyncio.sleep(3600)


"""
advertise.start()

@advertise.before_loop
async def before_advertise():
    await client.wait_until_ready()
"""



#running bot
# keep_alive() # remove later unless using uptimerbot
client.run(settings["token"])
