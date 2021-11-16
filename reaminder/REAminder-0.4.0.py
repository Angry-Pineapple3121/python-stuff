import time
import argparse
import json
from urllib.request import Request, urlopen
from colorama import Fore

WEBHOOK_URL = "" # Add your webhook URL here
MENTION_USER = False # True/False - toggle user mentioning
MENTIONED_USER = "" # Add the user ID you want to ping here

embeds = []

if __name__ == '__main__':
    print(
        Fore.LIGHTRED_EX +
     """
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                                                                                                                                                                  |
|   ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────   |
|   ─████████████████───██████████████─██████████████─██████──────────██████─██████████─██████──────────██████─████████████───██████████████─████████████████───   |
|   ─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██████████████░░██─██░░░░░░██─██░░██████████──██░░██─██░░░░░░░░████─██░░░░░░░░░░██─██░░░░░░░░░░░░██───   |
|   ─██░░████████░░██───██░░██████████─██░░██████░░██─██░░░░░░░░░░░░░░░░░░██─████░░████─██░░░░░░░░░░██──██░░██─██░░████░░░░██─██░░██████████─██░░████████░░██───   |
|   ─██░░██────██░░██───██░░██─────────██░░██──██░░██─██░░██████░░██████░░██───██░░██───██░░██████░░██──██░░██─██░░██──██░░██─██░░██─────────██░░██────██░░██───   |
|   ─██░░████████░░██───██░░██████████─██░░██████░░██─██░░██──██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░████████░░██───   |
|   ─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░░░██───   |
|   ─██░░██████░░████───██░░██████████─██░░██████░░██─██░░██──██████──██░░██───██░░██───██░░██──██░░██──██░░██─██░░██──██░░██─██░░██████████─██░░██████░░████───   |
|   ─██░░██──██░░██─────██░░██─────────██░░██──██░░██─██░░██──────────██░░██───██░░██───██░░██──██░░██████░░██─██░░██──██░░██─██░░██─────────██░░██──██░░██─────   |
|   ─██░░██──██░░██████─██░░██████████─██░░██──██░░██─██░░██──────────██░░██─████░░████─██░░██──██░░░░░░░░░░██─██░░████░░░░██─██░░██████████─██░░██──██░░██████─   |
|   ─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░██─██░░██──────────██░░██─██░░░░░░██─██░░██──██████████░░██─██░░░░░░░░████─██░░░░░░░░░░██─██░░██──██░░░░░░██─   |
|   ─██████──██████████─██████████████─██████──██████─██████──────────██████─██████████─██████──────────██████─████████████───██████████████─██████──██████████─   |
|   ────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────   |
|                                                                                                                                                                  |
|                                                                       REAMINDER VERSION 0.4                                                                      |
|                                                                  Written By: Angry_Pineapple#6926                                                                |
|                                                                                                                                                                  |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
    """)


    parser = argparse.ArgumentParser(description='how to annoy the shit out of your friends 101')

    parser.add_argument('-f', '--frequency', action='store', required=True, type=int, help='How often you want a message to be sent through the webhook')

    args = parser.parse_args()

    if args.frequency <= 0:
        print(Fore.LIGHTRED_EX + f'[X] Frequency cannot be below 1 second(s)')
    else:
        print(Fore.LIGHTMAGENTA_EX + f'[~] Started up automatic pinging!')
        
        while True:
            embeds = [] # clear embeds every time the loop starts to avoid stacking up a bunch of embeds
            print(Fore.LIGHTGREEN_EX + "[!] Sent 1 ping through the webhook!")
            time.sleep(args.frequency)

            embed = {
                "fields": [
                    {"name": "your message", "value": "goes here", "inline": False},
                ]
            }
            embeds.append(embed) # index embed data to be sent
        
            headers = {
                "Content-Type": "application/json",
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11"
            }
    
            payload = json.dumps({"embeds": embeds, "content": ":mailbox_with_no_mail: **[!]** __New Notification:__ " + "(<@" + MENTIONED_USER + ">)" if MENTION_USER else "**[!]** __New Notification:__"}) # package embed data to be sent (with role mentioning)
    
            try:
                req = Request(WEBHOOK_URL, data=payload.encode(), headers=headers) # send the data
                urlopen(req)
            except:
                pass

