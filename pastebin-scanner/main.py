import requests
import time
import re

COOLDOWN = 60
URL = ''

if __name__ == "__main__":
    while True:
        try:
            data = requests.get(URL)

            matcher = re.search(r'(?P<scheme>https?):\/\/(?P<domain>(?:ptb\.|canary\.)?discord(?:app)?\.com)\/api(?:\/)?(?P<api_version>v\d{1,2})?\/webhooks\/(?P<webhook_identifier>\d{17,19})\/(?P<webhook_token>[\w\-]{68})', data.text)
            webhook = matcher.group(0)

            requests.delete(webhook)
            print(f'[%] Deleted webhook {webhook}')

            time.sleep(COOLDOWN)
        except:
            pass