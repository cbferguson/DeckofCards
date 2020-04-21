import requests
import json
from urllib.request import urlopen
from PIL import Image
import io
from pprint import pprint

shuffled = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"

payload = {}
headers = {
  'Cookie': '__cfduid=d738a0c7b876ab4b87b37a9e23a6999291586367304'
}

response = requests.request("GET", shuffled, headers=headers, data = payload)

#print(response.text.encode('utf8'))
deck = response.json()
deck_id = deck['deck_id']
#print(deck_id)

drawcards = "https://deckofcardsapi.com/api/deck/34q0xwdokh08/draw/?count=2"



#def draw():
drawresponse = requests.request("GET", drawcards, headers=headers, data = payload)
    #requests.request("GET", drawcards, headers=headers, data = payload)
    #print(drawresponse.text.encode('utf8'))
    

#reshuffle
def shuffle():
    reshuffle_url = "https://deckofcardsapi.com/api/deck/34q0xwdokh08/shuffle/"
    #reshuffle = requests.request("GET", reshuffle_url, headers=headers, data = payload)
    requests.request("GET", reshuffle_url, headers=headers, data = payload)

cards = json.loads(drawresponse.text)

#print(response.text.encode('utf8'))

#for cardsdrew in cards:
print(json.dumps(cards, sort_keys=True, indent=4))
#pprint(cards)
card1 = requests.get(cards['cards'][0]['images']['png'])
card2 = requests.get(cards['cards'][1]['images']['png'])
card1_file = io.BytesIO(card1.content)
card2_file = io.BytesIO(card2.content)
card1_image = Image.open(card1_file)
card2_image = Image.open(card2_file)
card1_image.show()
card2_image.show()
print("You drew a " + cards['cards'][0]['value'] + " of " + cards['cards'][0]['suit'] + " and a " + cards['cards'][1]['value'] + " of " + cards['cards'][1]['suit'])

shuffle_answer = input(str("Do you want to reshuffle? (y or n)"))

if shuffle_answer == 'y':
  shuffle()


    #draw()


#print("The value of your cards is " + )
    #print(cards['cards']['suit'])
#response.close()