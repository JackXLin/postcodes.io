import requests
import json


class Postcodes:
    def __init__(self, postcode):
        self.postcode = postcode

    def get_detail(self):
        url = f"https://api.postcodes.io/postcodes/{self.postcode}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            print(f"Postcode: {data['result']['postcode']}")
            print(f"Primary Care Trust: {data['result']['primary_care_trust']}")
            print(f"Parliamentary Constituency: {data['result']['parliamentary_constituency']}")
        else:
            print(f"Error: {response.status_code}")