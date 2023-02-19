import requests
import json
import re
from random import choice

import asyncio
import aiohttp

from logzero import logger

from program.utils import searchapi as s
from program.utils import proxyapi as p

with open('program/config.json', 'r') as f:
    config = json.load(f)

apiKeys = config['apiKey']
searchParam = config['searchParam']

rawUrl = "raw.githubusercontent.com/"

currentKey = 0
keyNum = len(apiKeys)

def searchcode():
    global currentKey
    apiKey = apiKeys[currentKey]
    logger.info(currentKey)
    logger.info('searching github...')
    logger.info(apiKey)
    request = s.searchcall(searchParam, apiKey)
    if currentKey == 5:
        currentKey = 0
    else:
        currentKey = currentKey + 1
    logger.info(currentKey)
    return request.json()

def getcontent(content):
    logger.info('getting proxies')
    proxylist = p.getProxies()

    proxy = {'http' : choice(proxylist)}
    logger.info('getting file content...')
    contentLinks = [f"https://raw.githubusercontent{i['html_url'][14:]}".replace('/blob', '') for i in content['items']]
    return [requests.get(i, proxies=proxy).text for i in contentLinks]

def searchcontent(content):
    #dumb stupid annoying regex
    logger.info('searching for webhooks...')
    quotes = []
    
    for i in content:
        quotes.append(re.findall("['\"](.*?)['\"]", i))

    hooks = []
    for i in quotes:
        for j in i:
            if re.search("https:\/\/discord.com\/api\/webhooks\/([^\/]+)\/([^\/]+)\\w", j) != None:
                hooks.append(j)

    return hooks
            
        
if __name__ == "__main__":
    logger.warning("Please run main.py")