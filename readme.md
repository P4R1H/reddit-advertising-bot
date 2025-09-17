# `Reddit advertiser`

You can use this script to advertise anything, this was originally intended to be used with [replit](https://replit.com), so it utilizes replitdb, though with minor programming knowledge you can easily convert it into another database.

# `> Key features` 

1) Uses a database to prevent advertising to the same user multiple times

2) Completely avoids rate limits by sleeping for a few mins between runs

3) Logs people dmd in a discord channel

4) highly customizable

# `> Setup`

1) Add your reddit bot account's credentials and discord bot token as envs

2) rename `config.example.json` to `config.json`. go to `config.json`, and fill in the subreddits you want to advertise in, along with the limit of posts you want it to go through for that particular subreddit. generally if the sub gets a lot of posts, put the limit around 25-35, otherwise around 10-15

3) find the `channelid` key in `config.json` and enter the discord channel's id where you want the bot to log all the people it has dmd on reddit

4) find the `dmcontent` and `dmtitle` in `config.json` and fill them accordingly to what u want the bot to advertise

5) save subreddits to go through as "sub1:limit , sub2:limit , sub3:limit" ...... in the .env

# `> Notes`

bot dms 15 people in `new` by default, if you want to change this, find the `advertisenew` function call in `main.py` and change the `15` in there to the amount of people you want to dm in new, amount of people dmd in hot already specified by you in `config.json`.

Reddit bans account for mass dming, though that only happens rarely and only if a user reports the bot, so try not to make your advertisement too annoying.

 
 
