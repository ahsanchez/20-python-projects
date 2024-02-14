# original data request is not longer available, I used dummysjson request instead!!!!!

import requests
import json
import time


def update():
    r = requests.get("https://dummyjson.com/products/1")
    data = r.json()
    text = f'Product: {data["title"]} \nDescription: {data["description"]} \nPrice: {data["price"]}'
    print(text)


update()
