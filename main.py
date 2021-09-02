#maymay bot code

#importing directories

import discord
from discord.ext import commands
import os
import asyncpraw
import asyncio



#reddit login credentials

reddit = asyncpraw.Reddit(client_id=os.getenv("id"),
                          client_secret=os.getenv("ab"),
                          username="TheMayMayMakers",
                          password=os.getenv("pass"),
                          user_agent=os.getenv("ef"))

#setting default command

client = commands.Bot(command_prefix="-")

#client.event from here
client.remove_command('help')



@client.event
async def on_ready():
    print("we have logged in as {0.user}".format(client))



#client.command from here











#advertising bot for aid


@client.command(brief='[redacted]', aliases= ["adv"])
@commands.is_owner()
async def advertise(ctx):
    while(1):

        meme = await reddit.subreddit("meme")
        dankmemes = await reddit.subreddit("dankmemes")
        donkmemes = await reddit.subreddit("memes_of_the_dank")
        memes = await reddit.subreddit("memes")
        

        topmemes = memes.hot(limit = 30)
        topmeme = meme.hot(limit=15)
        bottommeme = meme.new(limit = 15)
        topdankmemes = dankmemes.hot(limit=20)
        bottomdankmemes = dankmemes.new(limit = 15)
        topdonkmemes = donkmemes.hot(limit=10)
        bottomdonkmemes = donkmemes.new(limit = 15)
        
        await ctx.send("```Hot invite batch incoming```")
        await ctx.send("_ _")

        await ctx.send("[*Inviting from **r/dankmemes***]")
        await ctx.send("_ _")

        async for submission in topdankmemes:
            print("starting r/dankmemes")

            with open("dmddank.txt", "r") as f:
              
              try:

                  if submission.author.name.lower() in f.read():
                      print(submission.author.name,
                            ": found in the dm log, going to next user")
                      continue
                  else:
                      print(submission.author.name, ": didnt find in the dm log")
                      with open("dmddank.txt", "a") as f:
                          f.write(submission.author.name.lower())
                          f.write(",")

                          print("written in the dm log")

                          tuser = await reddit.redditor(submission.author.name)

                          await tuser.message(
                              "Hello fellow memer!",
                              "looks like you like making memes. Would you like to join a  Discord community of meme creators by top memers where we help each other with meme creation? If so, here's your invite: [discord.gg/memereview](https://discord.gg/ESZxaHWw3X)"
                          )

                          await ctx.send(
                              f"{submission.author.name} has been dmd an invite")                          
                          await asyncio.sleep(45)
                
              except:
                print(f"{submission.author.name} probably has dms off, not added to dm log")
                await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue

        await ctx.send("_ _")
        await ctx.send("[*Inviting from **r/meme***]")
        await ctx.send("_ _")
        async for submission in topmeme:
            print("starting r/meme")

            with open("dmddank.txt", "r") as g:
              
              try:


                  if submission.author.name.lower() in g.read():
                      print(submission.author.name,
                            ": found in the dm log, going to next user")
                      continue
                  else:
                      print(submission.author.name, ": didnt find in the dm log")
                      with open("dmddank.txt", "a") as g:
                          g.write(submission.author.name.lower())
                          g.write(",")

                          print("written in the dmdmemes")

                          duser = await reddit.redditor(submission.author.name)

                          await duser.message(
                              "Hello fellow memer!",
                              "looks like you like making memes. Would you like to join a  Discord community of meme creators by top memers where we help each other with meme creation? If so, here's your invite: [discord.gg/memereview](https://discord.gg/ESZxaHWw3X)"
                          )
                          
                          await ctx.send(
                              f"{submission.author.name} has been dmd an invite")


                          await asyncio.sleep(45)
             
              except:
                print(f"{submission.author.name} probably has dms off, not added to dm log")
                await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue
                

        await ctx.send("_ _")
        await ctx.send("[*Inviting from **r/memes\_of\_the\_dank***]")
        await ctx.send("_ _")
        async for submission in topdonkmemes:
            print("starting r/memes_of_the_dank")

            with open("dmddank.txt", "r") as h:

              try:

                  if submission.author.name.lower() in h.read():
                      print(submission.author.name,
                            ": found in the dm log, going to next user")
                      continue
                  else:
                      print(submission.author.name, ": didnt find in the dm log")
                      with open("dmddank.txt", "a") as h:
                          h.write(submission.author.name.lower())
                          h.write(",")

                          print("written in the dmdmemes")

                          duser = await reddit.redditor(submission.author.name)

                          await duser.message(
                              "Hello fellow memer!",
                              "looks like you like making memes. Would you like to join a  Discord community of meme creators by top memers where we help each other with meme creation? If so, here's your invite: [discord.gg/memereview](https://discord.gg/ESZxaHWw3X))"
                          )

                          await ctx.send(
                              f"{submission.author.name} has been dmd an invite")



                          await asyncio.sleep(45)
             
              except:
                print(f"{submission.author.name} probably has dms off, not added to dm log")
                await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue


        await ctx.send("_ _")

        await ctx.send("[*Inviting from **r/MemeEconomy***]")
        await ctx.send("_ _")
        async for submission in topmemes:
            print("starting r/memes")

            with open("dmddank.txt", "r") as i:
              
              try:

                  if submission.author.name.lower() in i.read():
                      print(submission.author.name,
                            ": found in the dm log, going to next user")
                      continue
                  else:
                      print(submission.author.name, ": didnt find in the dm log")
                      with open("dmddank.txt", "a") as i:
                          i.write(submission.author.name.lower())
                          i.write(",")

                          print("written in the dmdmemes")

                          duser = await reddit.redditor(submission.author.name)

                          await duser.message(
                              "Hello fellow memer!",
                              "looks like you like making memes. Would you like to join a  Discord community of meme creators by top memers where we help each other with meme creation? If so, here's your invite: [discord.gg/memereview](https://discord.gg/ESZxaHWw3X)"
                          )
                          
                          await ctx.send(
                              f"{submission.author.name} has been dmd an invite")


                          await asyncio.sleep(45)

              except:
                print(f"{submission.author.name} probably has dms off, not added to dm log")
                await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue





        await ctx.send("_ _")
        await ctx.send("```waiting 1 hour to send next batch of invites```")
        await asyncio.sleep(3600)







        await ctx.send("```new invite batch incoming```")
        await ctx.send("_ _")

        await ctx.send("[*Inviting from **r/dankmemes***]")
        await ctx.send("_ _")

        async for submission in bottomdankmemes:
            print("starting r/dankmemes")

            with open("dmddank.txt", "r") as j:
              
              try:

                  if submission.author.name.lower() in j.read():
                      print(submission.author.name,
                            ": found in the dm log, going to next user")
                      continue
                  else:
                      print(submission.author.name, ": didnt find in the dm log")
                      with open("dmddank.txt", "a") as j:
                          j.write(submission.author.name.lower())
                          j.write(",")

                          print("written in the dm log")

                          tuser = await reddit.redditor(submission.author.name)

                          await tuser.message(
                              "Hello fellow memer!",
                              "Looks like you like making memes, would you like to join our discord community of meme creators by top memers where we help each other in making and editing memes, share meme templates, host competitions and talk? If so, here's your invite:  [discord.gg/memereview](https://discord.gg/ESZxaHWw3X)"
                          )

                          await ctx.send(
                              f"{submission.author.name} has been dmd an invite")                          
                          await asyncio.sleep(45)
                
              except:
                print(f"{submission.author.name} probably has dms off, not added to dm log")
                await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue

        await ctx.send("_ _")
        await ctx.send("[*Inviting from **r/meme***]")
        await ctx.send("_ _")
        async for submission in bottommeme:
            print("starting r/meme")

            with open("dmddank.txt", "r") as k:
              
              try:


                  if submission.author.name.lower() in k.read():
                      print(submission.author.name,
                            ": found in the dm log, going to next user")
                      continue
                  else:
                      print(submission.author.name, ": didnt find in the dm log")
                      with open("dmddank.txt", "a") as k:
                          k.write(submission.author.name.lower())
                          k.write(",")

                          print("written in the dmdmemes")

                          duser = await reddit.redditor(submission.author.name)

                          await duser.message(
                              "Hello fellow memer!",
                              "Looks like you like making memes, would you like to join our discord community of meme creators by top memers where we help each other in making and editing memes, share meme templates, host competitions and talk? If so, here's your invite:  [discord.gg/memereview](https://discord.gg/ESZxaHWw3X)"
                          )
                          
                          await ctx.send(
                              f"{submission.author.name} has been dmd an invite")


                          await asyncio.sleep(45)
             
              except:
                print(f"{submission.author.name} probably has dms off, not added to dm log")
                await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue
                

        await ctx.send("_ _")
        await ctx.send("[*Inviting from **r/memes\_of\_the\_dank***]")
        await ctx.send("_ _")
        async for submission in bottomdonkmemes:
            print("starting r/memes_of_the_dank")

            with open("dmddank.txt", "r") as l:

              try:

                  if submission.author.name.lower() in l.read():
                      print(submission.author.name,
                            ": found in the dm log, going to next user")
                      continue
                  else:
                      print(submission.author.name, ": didnt find in the dm log")
                      with open("dmddank.txt", "a") as l:
                          l.write(submission.author.name.lower())
                          l.write(",")

                          print("written in the dmdmemes")

                          duser = await reddit.redditor(submission.author.name)

                          await duser.message(
                              "Hello fellow memer!",
                              "Looks like you like making memes, would you like to join our discord community of meme creators by top memers where we help each other in making and editing memes, share meme templates, host competitions and talk? If so, here's your invite:  [discord.gg/memereview](https://discord.gg/ESZxaHWw3X))"
                          )

                          await ctx.send(
                              f"{submission.author.name} has been dmd an invite")



                          await asyncio.sleep(45)
             
              except:
                print(f"{submission.author.name} probably has dms off, not added to dm log")
                await ctx.send(f"Couldnt dm {submission.author.name}, they probably have dms off")
                continue



        await ctx.send("_ _")
        await ctx.send("```waiting 1 hour to send next batch of invites```")
        await asyncio.sleep(3600)

@advertise.error
async def advertise_error(ctx, error):
    if isinstance(error, commands.NotOwner):
        em = discord.Embed(title = "This is a dev-only command", color = discord.Color.red())

        await ctx.send(embed = em)


#running bot with token

client.run(os.getenv("token"))