# hypixel banwave scanner
Automatically retrieves & sends data about Hypixel's punishment staistics through a Discord webhook. Useful for people who macro farming/ghosts to know when staff are active.

Has five distinct levels of "ban risk" depending on the # of bans in 15 minutes.

Displays 6 data points, organized neatly.

## Instructions
1) Download `banwavescanner.py` and `requirements.txt`
2) In the directory you downloaded these files from, run `pip install -r requirements.txt`
3) Configure available variables (`WEBHOOK_URL`, `API_KEY`)
4) Run the script and wait for the first round of data to populate.

> **NOTE:** The first round of data sent to the webhook after the script has started will **always** show up as 0 bans. Allow the script to run for >15 minutes for accurate results.
