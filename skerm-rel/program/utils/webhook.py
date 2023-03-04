# handles all webhook functions, including notifying us that skerm found a working webhook
import json
import requests
from logzero import logger
from program.utils import proxyapi as p
import random
config = json.load(open('program/config.json', 'r'))

webhook = config["webhook"]
content = config["homewebhook"]

#proxylist = p.getProxies()
#proxy = {'https' : random.choice(proxylist)}

def notifyServer(webhookurl, data):
    response = requests.post(webhookurl, json=data)

def deleteHook(hook):
    response = requests.delete(hook)
    if response.status_code == 200:
        logger.info('deleted message successfully')

def sendMessage(hook, data):
    
    response = requests.post(hook, json=data)
    if response.status_code == 404:
        logger.warning('webhook does not exist.')
    elif response.status_code == 429:
        logger.warning('ratelimited, too many requests at once')
    elif response.status_code == 200:
        logger.info('sent message successfully')
        notifyServer(webhook, content)
        deleteHook(hook)
