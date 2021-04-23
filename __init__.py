from abc import abstractclassmethod
import requests
from random import choice

from functools import lru_cache

URL = "https://www.pon.workers.dev/drive"
PROXY_API = "https://www.proxy-list.download/api/v1/get?type=https&anon=elite"

@lru_cache()
def fetch_proxies():
    return requests.get(PROXY_API).text.splitlines()

def create(email_address, storage_name, *, avoid_ratelimit=False):
    """
    Just an API call to send a "Google Drive Shared Storage" to your Google account in seconds?
    """
    return requests.post(URL, json={'emailAddress': email_address,'teamDriveName': storage_name,'teamDriveThemeId':'random'}, proxies={} if not avoid_ratelimit else {'http': "http://%s/" % choice(fetch_proxies())}).ok

if __name__ == '__main__':
    import sys
    create(*sys.argv[1:][:2], avoid_ratelimit=True)