import requests
import json
from logzero import logger


baseurl = "https://api.github.com/"

def searchcall(param, key):
    data = requests.get(f"{baseurl}{param}", headers={'Authorization' : f'Token {key}'})
    return data

if __name__ == "__main__":
    logger.warning("Please run 'main.py'")
