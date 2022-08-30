 
from discord_webhook import DiscordWebhook, DiscordEmbed
import requests
import json
import time

# USER-EDITABLE PROGRAM SETTINGS
SLEEP_AMOUNT = 900.0 # how often to run - in seconds
WEBHOOK_URL = '' # your discord webhook url to send data to
API_KEY = '' # your hypixel api key
# END OF USER-EDITABLE PROGRAM SETTINGS

API_ENDPOINT = 'https://api.hypixel.net/punishmentstats'

LAST_TOTAL_STAFF = -1
STAFF_LAST_MINUTE = 0
STAFFBANTOTAL = 0

EMBEDCOLOR = ''
SQUARECOLOR = ''

if __name__ == "__main__":
    while True:
        try:
        ######################
        # API REQUEST SYSTEM #
        ######################

            ban_data = requests.get(f'{API_ENDPOINT}?key={API_KEY}')
            obj_1 = json.loads(ban_data.text)
            ban_data_formatted = json.dumps(obj_1, indent=4)

            STAFFBANTOTAL = obj_1["staff_total"]

            if STAFFBANTOTAL < LAST_TOTAL_STAFF: 
                STAFFBANTOTAL = LAST_TOTAL_STAFF
                
            if LAST_TOTAL_STAFF == -1:
                LAST_TOTAL_STAFF = STAFFBANTOTAL
                
            else: 
                STAFF_LAST_MINUTE = STAFFBANTOTAL - LAST_TOTAL_STAFF
                LAST_TOTAL_STAFF = STAFFBANTOTAL
                
        except:
            print('[Error] An error occurred while parsing API data.')
            pass
        
        #######################
        # COLOR CHANGE SYSTEM #
        #######################

        if STAFF_LAST_MINUTE <= 9:
            EMBEDCOLOR = '79b058'
            SQUARECOLOR = '🟩'
        if STAFF_LAST_MINUTE >= 10:
            EMBEDCOLOR = 'fcca58'
            SQUARECOLOR = '🟨'
        if STAFF_LAST_MINUTE >= 20:
            EMBEDCOLOR = 'f5900d'
            SQUARECOLOR = '🟧'
        if STAFF_LAST_MINUTE >= 40:
            EMBEDCOLOR = 'dc2f44'
            SQUARECOLOR = '🟥'
        if STAFF_LAST_MINUTE >= 45:
            EMBEDCOLOR = '31363d'
            SQUARECOLOR = '⬛'

        ##################
        # WEBHOOK SYSTEM #
        ##################

        webhook = DiscordWebhook(url=f'{WEBHOOK_URL}')

        embed = DiscordEmbed(title=f'{SQUARECOLOR} - Banwave Scanner - {SQUARECOLOR}', description='Automatically scanned the Hypixel API (punishment data) and checked for bans!\nThe colored squares and colored embed bar will automatically update based on the risk of being banned for QOL activities.', color=f'{EMBEDCOLOR}')
        embed.set_footer(text='Automatically displays new information every 15 minutes.')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/704479038970003570/984152950500896798/unknown.png')
        embed.add_embed_field(name='Staff Bans', value=f':star: Staff Bans (rolling daily): {obj_1["staff_rollingDaily"]}\n:star: Staff Bans (total): {obj_1["staff_total"]}')
        embed.add_embed_field(name='Watchdog Bans', value=f':star: Watchdog Bans (last minute): {obj_1["watchdog_lastMinute"]}\n:star: Watchdog Bans (rolling daily): {obj_1["watchdog_rollingDaily"]}\n:star: Watchdog Bans (total): {obj_1["watchdog_total"]}')
        embed.add_embed_field(name='Last 15 Minutes', value=f':star: Staff Bans (last 15m): {STAFF_LAST_MINUTE}', inline=True)
        embed.add_embed_field(name='Banwave Information', value=f'🟩 - Bans (15m) < 9 - `Low Risk of being banned`\n🟨 - Bans (15m) > 10 - `Medium Risk of being banned`\n🟧 - Bans (15m) > 20 - `Elevated Risk of being banned`\n🟥 - Bans (15m) > 40 - `High Risk of being banned`\n⬛ - Bans (15m) > 45 - `Very High risk of being banned / Active Banwave`', inline=False)
        embed.set_timestamp()

        webhook.add_embed(embed)

        try:
            print('[Success] Sent ban data to the webhook successfully!')
            response = webhook.execute()
        except:
            print('[Error] An exception occurred while sending the webhook data.')
            pass

        time.sleep(SLEEP_AMOUNT)