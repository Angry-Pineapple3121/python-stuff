# hypixel banwave scanner
automatically pulls & sends data about hypixel punishment statistics (through discord webhook) so you can know when to stop cheating
has 5 distinct levels of "ban risk" (they probably don't mean anything)

## instructions
1) download `banwavescanner.py` and `requirements.txt`
2) in the directory you downloaded these files from, run `pip install -r requirements.txt`
3) open the `banwavescanner.py` file and configure the following:
 - your discord webhook
 - your hypixel api key
4) run the script and accurate results will appear within **15** minutes

**NOTE:** the first round of data sent to the webhook after the script has started will **always** be 0, as it hasn't got any prior data to go off of yet