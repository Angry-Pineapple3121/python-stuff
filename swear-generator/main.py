import json
import random

WORDS_FILE = open('words.json')
WORDS_INDEX = json.loads(WORDS_FILE.read())
WORDS_FILE.close()

if __name__ == "__main__":
    number = input("[~] Please input the number of words to generate: ")
    number = int(number)
    RANDOM_WORD = random.choices(WORDS_INDEX, k=number)
    
    print(f"[!] Finished generating {number} words, word list: \n{RANDOM_WORD}")
