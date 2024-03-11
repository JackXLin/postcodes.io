import requests
import json


class Postcode:
    def __init__(self, postcode):
        self.postcode = postcode
        self.url = f"https://api.postcodes.io/postcodes/{self.postcode}"
        self.urls = "https://api.postcodes.io/postcodes"

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
    def __init__(self, postcode):
        super().__init__(postcode)

    def get_detail(self):
        data = {
            "postcodes": [self.postcode]
        }
        response = requests.post(self.urls, data=data)

        if response.status_code == 200:
            result = response.json()
            for query in result["result"]:
                for info in query["result"]:
                    if info in ["postcode", "primary_care_trust", "parliamentary_constituency"]:
                        print(f"Postcode: {query["result"][info]}")
                        # print(f"Primary Care Trust: {query["result"][info]}")
                        # print(f"Parliamentary Constituency: {query["result"][info]}")
            return result
        else:
            print(f"Error: {response.status_code}")

