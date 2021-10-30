#importing directories
import discord
from discord.ext import commands
from replit import db
import asyncpraw
import os
import asyncio


#reddit login credentials
reddit = asyncpraw.Reddit(client_id=os.getenv("clientid"),
                          client_secret=os.getenv("secret"),
                          username="TheMayMayMakers",
                          password=os.getenv("password"),
                          user_agent=os.getenv("agent"))


intents = discord.Intents.all()
client = commands.Bot(command_prefix='-', intents=intents)


#modules
async def advertisehot(ctx, subreddit, lim, title, content):
    await ctx.send("_ _")
    await ctx.send(f"[*Inviting from **r/{subreddit}***]")
    await ctx.send("_ _")

    sub = await reddit.subreddit(subreddit)
    topsub = sub.hot(limit = lim)

    async for submission in topsub:
        print(f"starting {subreddit}")
        
        try:

            if submission.author.name.lower() in db["dmd"]:
                print(submission.author.name,
                      ": found in the dm log, going to next user")
                continue
            else:
                print(submission.author.name, ": didnt find in the dm log")

                db["dmd"] = db["dmd"] + "," + submission.author.name.lower()

                print("written in the dm log")

                tuser = await reddit.redditor(submission.author.name)

                await tuser.message(title,content)

                await ctx.send(
                    f"{submission.author.name} has been dmd an invite")                          
                await asyncio.sleep(45)
          
        except:
          print(f"{submission.author.name} probably has dms off, not added to dm log")
          await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
          continue




async def advertisenew(ctx, subreddit, lim, title, content):
    await ctx.send("_ _")

    await ctx.send(f"[*Inviting from **r/{subreddit}***]")
    await ctx.send("_ _")

    sub = await reddit.subreddit(subreddit)
    bottomsub = sub.new(limit = lim)

    async for submission in bottomsub:
        print(f"starting {subreddit}")
        
        try:

            if submission.author.name.lower() in db["dmd"]:
                print(submission.author.name,
                      ": found in the dm log, going to next user")
                continue
            else:
                print(submission.author.name, ": didnt find in the dm log")

                db["dmd"] = db["dmd"] + "," + submission.author.name.lower()

                print("written in the dm log")

                tuser = await reddit.redditor(submission.author.name)

                await tuser.message(title, content)

                await ctx.send(
                    f"{submission.author.name} has been dmd an invite")                          
                await asyncio.sleep(45)
          
        except:
          print(f"{submission.author.name} probably has dms off, not added to dm log")
          await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
          continue          