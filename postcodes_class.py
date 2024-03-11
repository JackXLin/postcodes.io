import requests
import json


class Postcode:
    def __init__(self, postcode=None):
        self.postcode = postcode
        self.url = f"https://api.postcodes.io/postcodes/{self.postcode}"
        self.urls = "https://api.postcodes.io/postcodes"
        if postcode is None:
            self.url = "https://api.postcodes.io/random/postcodes"

    def get_detail(self):
        response = requests.get(self.url)

        if response.status_code == 200:
            data = response.json()
            print(f"Postcode: {data['result']['postcode']}")
            print(f"Primary Care Trust: {data['result']['primary_care_trust']}")
            print(f"Parliamentary Constituency: {data['result']['parliamentary_constituency']}")
            return data
        else:
            print(f"Error: {response.status_code}")

    def save_json(self, name):
        with open(name + ".json", "w") as outfile:
            json.dump(self.get_detail(), outfile)


class Postcodes(Postcode):
    def __init__(self, postcode=None):
        super().__init__(postcode)
        if postcode is None:
            raise Exception("Sorry, Random postcode function not support here!")

    def get_detail(self):
        data = {
            "postcodes": [self.postcode]
        }
        response = requests.post(self.urls, data=data)

        if response.status_code == 200:
            result = response.json()
            for query in result["result"]:
                print(f"Postcode: {query["result"].get("postcode")}")
                print(f"Primary Care Trust: {query["result"].get("primary_care_trust")}")
                print(f"Parliamentary Constituency: {query["result"].get("parliamentary_constituency")}")

            return result
        else:
            print(f"Error: {response.status_code}")


