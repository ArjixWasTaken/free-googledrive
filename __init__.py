import re
import sys

import requests

AUTODRIVE_BOT_API_URL = "https://www.pon.workers.dev/drive"

def create(email_address, storage_name):
    """API call for free Google Drive Shared Drive generation."""
    if not re.match(r"[\w.-]+@gmail\.com", email_address) and input("\"{}\" doesn't seem to be using the domain 'gmail.com', if the email is not a business email connected to a Google Drive, this process would fail. \nContinue? [y/N]: ".format(email_address)).lower().strip() == 'n':
        return False
    return requests.post(AUTODRIVE_BOT_API_URL, json={'emailAddress': email_address, 'teamDriveName': storage_name, 'teamDriveThemeId': 'random'}).ok

if __name__ == '__main__':
    create(*sys.argv[1:][:2])