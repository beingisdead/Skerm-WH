import requests
import json
from logzero import logger


baseurl = "https://api.github.com/"

def searchcall(param, key):
    headers = {'Authorization' : f'Token {key}'}
    data = requests.get(f"{baseurl}{param}", headers=headers)
    return data

if __name__ == "__main__":
    logger.warning("Please run 'main.py'")