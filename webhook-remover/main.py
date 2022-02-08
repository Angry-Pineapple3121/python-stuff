import requests
import json
import time
import uuid

WEBHOOK_OUTPUT_URL = ''
embeds = []

if __name__ == '__main__':
    while True:
        webhook = input('[=] Please enter webhook URL: ')
        data = requests.get(webhook)
        webhook_id = uuid.uuid1()
        print(data.text)
        obj_1 = json.loads(data.text)
        webhook_data_formatted = json.dumps(obj_1, indent=4)
        requests.delete(webhook)
        print(f'[#] Deleted the webhook with UUID {webhook_id} + sent log to the webhook!')
        embeds = []

        embed = {
            "fields": [
                {"name": "ㅤ", "value": f":arrow_right: Webhook Link: {webhook}", "inline": False},
                {"name": "ㅤ", "value": f":arrow_right: Webhook UUID: `{webhook_id}`", "inline": False},
                {"name": "ㅤ", "value": f":arrow_right: Webhook Data: \n```json\n{webhook_data_formatted}```", "inline": False},
                {"name": "ㅤ", "value": f":arrow_right: Time of Deletion: {time.strftime('%m/%d/%Y @ %H:%M:%S Eastern Standard Time')}", "inline": False},
            ]
        }
        embeds.append(embed)
        
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
        }
    
        payload = json.dumps({"embeds": embeds, "content": ":white_check_mark: **A webhook has been deleted successfully!**"})
    
        try:
            requests.post(WEBHOOK_OUTPUT_URL, data=payload.encode(), headers=headers)
        except:
            pass