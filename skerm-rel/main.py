#!/usr/bin/env python3

__author__ = "beingisdead"
__version__ = "0.1.0"
__license__ = "MIT"

import os
import argparse
import json

import schedule
import time as tm
from datetime import time, timedelta, datetime

from logzero import logger
from program.utils import searchapi
from program.utils import webhook
from program.utils import resultparser
from art import *

def main():

    codehits = resultparser.searchcode()
    codecontent = resultparser.getcontent(codehits)
    hooks = resultparser.searchcontent(codecontent)

    logger.info(len(hooks))

    for i in hooks:
        logger.info(f'sending message to {i}')
        webhook.sendMessage(i, webhookConfig)
        webhook.deleteHook(i)
    

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')

    print(text2art('Skerm ', "fancy5",decoration='barcode1'))

    logger.info('starting skerm')

    with open('program/config.json', 'r') as f:
        config = json.load(f)

    webhookConfig = config['webhookConfig']
    webhookurl = config["webhook"]

    main()
    schedule.every(20).seconds.do(main)

    while True:
        schedule.run_pending()
        tm.sleep(1)