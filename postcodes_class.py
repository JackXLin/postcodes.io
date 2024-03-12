import json
from postcodes_api import *


class Postcode(PostcodeAPI):
    def __init__(self, postcode=None):
        super().__init__(postcode)
        if self.response.status_code == 200:
            data = self.response.json()
            self.postcode = data["result"]["postcode"]
            self.primary_care_trust = data['result']['primary_care_trust']
            self.parliamentary_constituency = data['result']['parliamentary_constituency']
            self.json = data
        else:
            print(f"Error: {self.response.status_code}")
    # def __init__(self, postcode=None):
    #     self.postcode = postcode
    #     self.url = f"https://api.postcodes.io/postcodes/{self.postcode}"
    #     self.urls = "https://api.postcodes.io/postcodes"
    #     if postcode is None:
    #         self.url = "https://api.postcodes.io/random/postcodes"
    #
    # def get_detail(self):
    #     response = requests.get(self.url)
    #
    #     if response.status_code == 200:
    #         data = response.json()
    #         print(f"Postcode: {data['result']['postcode']}")
    #         print(f"Primary Care Trust: {data['result']['primary_care_trust']}")
    #         print(f"Parliamentary Constituency: {data['result']['parliamentary_constituency']}")
    #         return data
    #     else:
    #         print(f"Error: {response.status_code}")

    def save_json(self, name):
        with open(name + ".json", "w") as outfile:
            json.dump(self.json, outfile)


class Postcodes(PostcodesAPI):
    def __init__(self, postcode=None):
        super().__init__(postcode)
        if self.response.status_code == 200:
            data = self.response.json()
            # self.postcode = data["result"]["postcode"]
            # self.primary_care_trust = data['result']['primary_care_trust']
            # self.parliamentary_constituency = data['result']['parliamentary_constituency']
            self.json = data
        if postcode is None:
            raise Exception("Sorry, Random postcode function not support here!")

    def save_json(self, name):
        with open(name + ".json", "w") as outfile:
            json.dump(self.json, outfile)

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


