from abc import abstractclassmethod
import requests
import re
from random import choice

from functools import lru_cache

URL = "https://www.pon.workers.dev/drive"
PROXY_API = "https://www.proxy-list.download/api/v1/get?type=https&anon=elite"


@lru_cache()
def fetch_proxies():
    return requests.get(PROXY_API).text.splitlines()


def create(email_address, storage_name, *, avoid_ratelimit=False):
    if not re.match(r"[a-zA-Z\.0-9]+?\@gmail\.com", email_address):
        print('The email address provided: {} appears to not be a valid gmail (non business) address.'.format(email_address))
        answer = input('Are you sure you want to continue with this address? [Y]/N: ')

        if answer.strip() == '':
            pass
        elif answer.strip().lower() == 'y':
            pass
        else:
            print('Aborting...')
            exit()
    """
    Just an API call to send a "Google Drive Shared Storage" to your Google account in seconds?
    """
    return requests.post(URL, json={
        'emailAddress': email_address,
        'teamDriveName': storage_name,
        'teamDriveThemeId': 'random'
    }, proxies={} if not avoid_ratelimit else {
        'http': "http://%s/" % choice(fetch_proxies())
    }).ok


if __name__ == '__main__':
    import sys
    create(*sys.argv[1:][:2], avoid_ratelimit=True)
