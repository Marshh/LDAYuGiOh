import json
import requests
import re

base_url = "https://db.ygoprodeck.com/api/v4/cardinfo.php?"

## Request card info of every Yu-Gi-Oh card and turns the JSON into a dict
response = requests.get("https://db.ygoprodeck.com/api/v4/cardinfo.php")
response_list = response.json()

card_list = list()

## Trim and writing to text file {"Name":..., "Text"}
## Note: common words like 'when' and 'if' are not filtered because they have
##       strong connotations in the game
stopwords = "the and was that for can to be with this then of it its as a"

## filter_text function adapted from Professor Ihler's example
def filter_text(text):
    words = re.sub(r'[^\w ]',' ',text)
    words=map(lambda w: w.lower(),words.split(' '))
    words=list(filter(lambda w: w not in stopwords,words))
    return words


## Map an ID to each card for later sorting
count = 0
for x in response_list:
    for card in x:
        card_list.append(
            {
             "CARDNUM": count,
             "Name":card["name"],
             "Text":filter_text(card["desc"])
            }
        )
        count+= 1

card_file = open("card_text", "w")

for card in card_list:
    card_file.writelines(json.dumps(card) + "\n") 

card_file.close()
