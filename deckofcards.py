import requests
import json
from urllib.request import urlopen
from PIL import Image
import io
from pprint import pprint

numofdecks = input("How many decks do you want to play with?")

drawcards = "https://deckofcardsapi.com/api/deck/34q0xwdokh08/draw/?count=2"
hit_url = "https://deckofcardsapi.com/api/deck/34q0xwdokh08/draw/?count=1"
shuffled = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=" + numofdecks
reshuffle_url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=" + numofdecks
#print(shuffled)

value_face = 0
value_ace = 0

payload = {}
headers = {
  'Cookie': '__cfduid=d738a0c7b876ab4b87b37a9e23a6999291586367304'
}

response = requests.request("GET", shuffled, headers=headers, data = payload)
drawresponse = requests.request("GET", drawcards, headers=headers, data = payload)

#print(response.text.encode('utf8'))
deck = response.json()
deck_id = deck['deck_id']
#print(deck_id)

#numofcards = input("How many cards to you want?")


def draw():
    #drawresponse = requests.request("GET", drawcards, headers=headers, data = payload)
    requests.request("GET", drawcards, headers=headers, data = payload)
    #print(drawresponse.text.encode('utf8'))

def hit():
    requests.request("GET", hit_url, headers=headers, data=payload)

#reshuffle
def shuffle():
    requests.request("GET", reshuffle_url, headers=headers, data=payload)
    #reshuffle = requests.request("GET", reshuffle_url, headers=headers, data = payload)

cards = json.loads(drawresponse.text)

#print(response.text.encode('utf8'))

#for cardsdrew in cards:
#print(json.dumps(cards, sort_keys=True, indent=4))
#pprint(cards)
card1 = requests.get(cards['cards'][0]['images']['png'])
card2 = requests.get(cards['cards'][1]['images']['png'])
card1_file = io.BytesIO(card1.content)
card2_file = io.BytesIO(card2.content)
card1_image = Image.open(card1_file)
card2_image = Image.open(card2_file)
card1_image.show()
card2_image.show()
card1_value = cards['cards'][0]['value']
card2_value = cards['cards'][1]['value']
card1_suit = cards['cards'][0]['suit']
card2_suit = cards['cards'][1]['suit']
print("You drew a " + card1_value + " of " + card1_suit + " and a " + card2_value + " of " + card2_suit)


#figuring up points
if card1_value == 'JACK':
    card1_value = 10
elif card1_value == 'KING':
    card1_value = 10
elif card1_value == 'QUEEN':
    card1_value = 10

if card1_value == 'ACE':
    card1_value = 1

if card2_value == 'JACK':
    card2_value = 10
elif card2_value == 'KING':
    card2_value = 10
elif card2_value == 'QUEEN':
    card2_value = 10

if card2_value == 'ACE':
    card2_value = 1

card_numeric_value = int(card1_value) + int(card2_value)

print("You have a total of " + str(card_numeric_value))

#print(card1_value)
#print(card2_value)
print(card_numeric_value)

#def main_question()
tired_of_playing = input(str("Are you tired of playing? (y or n)"))

if tired_of_playing == 'n':
    hit_answer = input(str("Do you want a hit? (y or n)"))
    if hit_answer == 'y':
        hit()
    else:
        print("you've decided to hold")
elif shuffle_answer == 'y':
  shuffle()

#print("The value of your cards is " + )
    #print(cards['cards']['suit'])
#response.close()