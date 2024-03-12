import requests


class PostcodeAPI:
    def __init__(self, postcode=None):
        self.postcode = postcode
        self.url = f"https://api.postcodes.io/postcodes/{self.postcode}"
        if postcode is None:
            self.url = "https://api.postcodes.io/random/postcodes"
        self.response = requests.get(self.url)


class PostcodesAPI(PostcodeAPI):
    def __init__(self, postcode):
        super().__init__(postcode)
        self.url = "https://api.postcodes.io/postcodes"
        data = {
            "postcodes": [self.postcode]
        }
        self.response = requests.post(self.url, data=data)
