#helper for mongodb

from datetime import datetime
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
import time
import json

f= open("config.json","r")
settings = json.load(f)
f.close()

cluster = MongoClient(settings["mongo_link"], server_api=ServerApi('1'))
db = cluster[settings["cluster_name"]]
collection = db['users-dmd']

async def user_find(userid: str):
    result = list(collection.find({'username': userid}))
    if len(result)==0:
        return None
    return result[0]

# for now just store username, expand later if needed?
# assume they dont exist, use update_user normally
async def insert_user(username: str):
    collection.insert_one({"username": username, "camps": [settings["current_camp"]]}) # store camp incase ever want to expand to others and re dm same user about new camp


# check if exist and update camps
# only to be done if camps are there to be updated!
async def update_user(username: str):
    user_data = await user_find(username)
    if not user_data:
        insert_user(username)
    elif settings["current_camp"] not in user_data["camps"]:
        collection.update_one({"username": username} , {"$set": {"username":username, "camps": user_data["camps"].append(settings["current_camp"])}})
    else:
        pass

