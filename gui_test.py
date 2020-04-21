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
def get_image(url):
    image_url = Request(httpimage, headers={'User-Agent': 'Mozilla/5.0'})
    image_byt = urlopen(image_url).read()
    #print('here' + image_byt)
    image_b64 = base64.encodebytes(image_byt)
    return image_b64

deckcount = 6
request = 'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=' + str(deckcount)
response = requests.get(request)

rdeck_id = response.json()['deck_id']
draw2 = requests.get('https://deckofcardsapi.com/api/deck/qjfuzljbm0z6/draw/?count=2')
deck = draw2.json()
#print(json.dumps(draw2.json(),sort_keys=True,indent=4))
httpimage = deck['cards'][0]['image']
httpimage2 = deck['cards'][1]['image']
print(httpimage2)
root = tk.Tk()
root.title("display a website image")
# a little more than width and height of image
w = 600
h = 600
x = 80
y = 200
# use width x height + x_offset + y_offset (no spaces!)
root.geometry("%dx%d+%d+%d" % (w, h, x, y))
# this GIF picture previously downloaded to tinypic.com

photo = tk.PhotoImage(data=get_image(httpimage))
photo2 = tk.PhotoImage(data=get_image(httpimage2))
# create a white canvas
cv = tk.Canvas(bg='white')
cv.pack(side='top', fill='both', expand='yes')
# put the image on the canvas with
# create_image(xpos, ypos, image, anchor)
cv.create_image(10, 10, image=photo, anchor='nw')
cv.create_image(100, 10, image=photo2, anchor='ne')
root.mainloop()