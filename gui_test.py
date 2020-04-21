import io
import base64
import requests
try:
    # Python2
    import Tkinter as tk
    from urllib2 import urlopen, Request
except ImportError:
    # Python3
    import tkinter as tk
    from urllib.request import urlopen, Request

#number of decks
deckcount = 6

#request decks
request = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=' + str(deckcount)
response = requests.get(request)
rdeck_id = response.json()['deck_id']

#start with 2 cards
numcards = 2

#request number of cards
def get_cards(numofcards):
    draw = requests.get('https://deckofcardsapi.com/api/deck/' + str(rdeck_id) + '/draw/?count=' + str(numofcards))
    rcards = draw.json()
    return rcards

#get one card
def hit_me():
    card = get_image(get_cards(1))
    return card

#get images for card(s)
def get_image(url):
    image_url = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    image_byt = urlopen(image_url).read()
    #print('here' + image_byt)
    image_b64 = base64.encodebytes(image_byt)
    return image_b64

root = tk.Tk()
root.title("Test Deck")

# a little more than width and height of image
w = 600
h = 350
x = 600
y = 350

# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))

# this GIF picture previously downloaded to tinypic.com
cards = get_cards('2')
photo = tk.PhotoImage(data=get_image(cards['cards'][0]['image']))
photo2 = tk.PhotoImage(data=get_image(cards['cards'][1]['image']))

# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')

# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
cv.create_image(10, 10, image=photo, anchor='nw')
cv.create_image(45, 10, image=photo2, anchor='nw')

root.mainloop()