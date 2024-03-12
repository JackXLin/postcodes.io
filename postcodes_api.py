import requests


class PostcodeAPI:
    def __init__(self, postcode=None):
        self.postcode = postcode
        self.url = f"https://api.postcodes.io/postcodes/{self.postcode}"
        if postcode is None:
            self.url = "https://api.postcodes.io/random/postcodes"
        self.response = requests.get(self.url)
        # if response.status_code == 200:
        #     data = response.json()
        #     self.postcode = data["result"]["postcode"]
        #     self.primary_care_trust = data['result']['primary_care_trust']
        #     self.parliamentary_constituency = data['result']['parliamentary_constituency']
        #     self.json = data
        # else:
        #     print(f"Error: {response.status_code}")


class PostcodesAPI(PostcodeAPI):
    def __init__(self, postcode):
        super().__init__(postcode)
        self.url = "https://api.postcodes.io/postcodes"
        data = {
            "postcodes": [self.postcode]
        }
        self.response = requests.post(self.url, data=data)
