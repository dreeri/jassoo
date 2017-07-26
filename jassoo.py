#!/usr/bin/python3

from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import urllib.request
import json

API_URL = "https://api.unsplash.com/photos/random/?client_id="
APPLICATION_ID = "c08cd20813787def6e8c4fb5da974394afea0763c16cb04db67766fa5e828904"
IMAGES_PATH = "resources/images/"


def load_image(url):
    urllib.request.urlretrieve(url, IMAGES_PATH+"img0.jpg")

def random_image_url():
    response = urllib.request.urlopen(API_URL+APPLICATION_ID)
    data = response.read()
    json_result = json.loads(data.decode('utf-8'))
    return json_result['urls']['raw']

def draw_text():
    image = Image.open(IMAGES_PATH+"img0.jpg")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("resources/liberation-serif/LiberationSerif-Regular.ttf", 182)
    draw.text((0, 0), "Sample texti", (255, 255, 255), font=font)
    image.save(IMAGES_PATH+'img1.jpg')

def main():
    load_image(random_image_url())
    draw_text()

main()
