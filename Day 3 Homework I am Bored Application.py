import requests
from colorizer import print_blue, print_green, print_yellow


class Bored():
    def __init__(self):
        self.activity = ""
        self.type = ""
        self.participants = ""
        self.price = ""

    def bored_api(self):
        response = requests.get(f'http://www.boredapi.com/api/activity?minprice=0&maxprice=0.1')
        if not response.ok:
            return False
        data=response.json()

        self.activity = data["activity"]
        print_blue(self.activity)
        self.type = data["type"]
        self.participants = data["participants"]
        print_yellow(self.participants)
        self.price = data["price"]
        print_green(self.price)
        
        return True

data = Bored.bored_api
print(data)


    