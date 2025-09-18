#importing directories
import discord
from discord.ext import commands
# from replit import db
import asyncpraw
import os
import asyncio
import db as mdb
import json
import logger

# right now is a mix of config and env, ideally would move all to env or config.


async def login():
    #reddit login credentials
    global reddit
    reddit = asyncpraw.Reddit(client_id=os.getenv("clientid"),
                            client_secret=os.getenv("secret"),
                            username=os.getenv("username"),
                            password=os.getenv("password"),
                            user_agent=os.getenv("agent"))


intents = discord.Intents.all()
client = commands.Bot(command_prefix='-', intents=intents)

antidmlist = os.getenv("antidm").split(",")

#modules
async def advertisehot(subreddit, lim, title, content):
    await logger.log_info("_ _")
    await logger.log_info(f"[*Inviting from **r/{subreddit}***]")
    await logger.log_info("_ _")

    sub = await reddit.subreddit(subreddit)
    topsub = sub.hot(limit = lim)

    async for submission in topsub:
        await logger.log_info(f"starting {subreddit}")
        
        try:
            if submission.author.name.lower() in (s.lower() for s in antidmlist):
                await logger.log_info(f"{submission.author.name} in antidm list. ignored.")
                pass
            else:
                dbuser = await mdb.user_find(submission.author.name.lower())
                if dbuser and os.getenv("current_camp") in dbuser["camps"]:
                    await logger.log_info(submission.author.name +
                        ": found in the dm log, going to next user")
                else:
                    await logger.log_info(submission.author.name + ": didnt find in the dm log")


                    # add user here
                    # would use update_user here since we are checking camps.
                    await mdb.update_user(submission.author.name.lower())

                    await logger.log_info("written in the dm log")

                    tuser = await reddit.redditor(submission.author.name)

                    await tuser.message(title,content)

                    await logger.log_info(
                        f"{submission.author.name} has been dmd an invite")                          
                    await asyncio.sleep(45)
          
        except Exception as e:
            await logger.log_warning(e)
            await logger.log_info(f"{submission.author.name} probably has dms off, not added to dm log")
            await logger.log_warning(f"Couldnt dm {submission.author.name}, they probably have dms off")

        # go thru comments also now
        try:
            await submission.load()
            await submission.comments.replace_more(limit=0)
            comments = sorted(
                submission.comments.list(),
                key=lambda c: c.score if c.author else 0,
                reverse=True
            )[:10] # only top 15 here, inc/dec as needed.

            for comment in comments:
                if not comment.author:
                    continue  # skip deleted users
                if comment.author.name.lower() in (s.lower() for s in antidmlist):
                    await logger.log_info(f"{comment.author.name} in antidm list. ignored.")
                    pass
                try:
                    dbuser = await mdb.user_find(comment.author.name.lower())
                    if dbuser and os.getenv("current_camp") in dbuser["camps"]:
                        await logger.log_info(comment.author.name +
                            ": found in the dm log, skipping")
                        continue

                    await logger.log_info(comment.author.name + ": didnt find in the dm log")

                    await mdb.update_user(comment.author.name.lower())
                    await logger.log_info("written in the dm log")

                    tuser = await reddit.redditor(comment.author.name)
                    await tuser.message(title, content)

                    await logger.log_info(
                        f"{comment.author.name} has been dmd an invite")
                    await asyncio.sleep(45)

                except Exception as ce:
                    await logger.log_warning(ce)
                    await logger.log_info(
                        f"{comment.author.name} probably has dms off, not added to dm log")
                    await logger.log_warning(
                        f"Couldnt dm {comment.author.name}, they probably have dms off")

        except Exception as e:
            await logger.log_warning(e)
            await logger.log_warning(
                f"Couldnt process comments for {submission.id}")



async def advertisenew(subreddit, lim, title, content):
    await logger.log_info("_ _")

    await logger.log_info(f"[*Inviting from **r/{subreddit}***]")
    await logger.log_info("_ _")

    sub = await reddit.subreddit(subreddit)
    bottomsub = sub.new(limit = lim)

    async for submission in bottomsub:
        await logger.log_info(f"starting {subreddit}")
        if submission.author.name.lower() in (s.lower() for s in antidmlist):
            await logger.log_info(f"{submission.author.name} in antidm list. ignored.")
            continue
        else:
            try:
                dbuser = await mdb.user_find(submission.author.name.lower())
                if dbuser and os.getenv("current_camp") in dbuser["camps"]:
                    await logger.log_info(submission.author.name +
                        ": found in the dm log, going to next user")
                    continue
                else:
                    await logger.log_info(submission.author.name + ": didnt find in the dm log")

                    await mdb.update_user(submission.author.name.lower())
                    
                    await logger.log_info("written in the dm log")

                    tuser = await reddit.redditor(submission.author.name)

                    await tuser.message(title, content)

                    await logger.log_info(
                        f"{submission.author.name} has been dmd an invite")                          
                    await asyncio.sleep(45)
            
            except:
                await logger.log_info(f"{submission.author.name} probably has dms off, not added to dm log")
                await logger.log_warning(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue          
