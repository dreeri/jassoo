#!/usr/bin/python3

import urllib.request
import json

API_URL = "https://api.unsplash.com/photos/random/?client_id="
APPLICATION_ID = "c08cd20813787def6e8c4fb5da974394afea0763c16cb04db67766fa5e828904"

def load_image(url):
    urllib.request.urlretrieve(url, "images/img0.jpg")

def random_image_url():
    response = urllib.request.urlopen(API_URL+APPLICATION_ID)
    data = response.read()
    json_result = json.loads(data.decode('utf-8'))
    return json_result['urls']['raw']

def main():
    load_image(random_image_url())

main()
