# Postcodes.io Project

Welcome to the **Postcodes.io Project** repository! This project interacts with the Postcodes.io API to retrieve postcode-related information for the UK.

## Introduction

The **Postcodes.io Project** aims to provide easy access to geolocation data based on UK postcodes. It leverages the Postcodes.io API to retrieve details such as parliamentary constituencies, primary care trusts, and more.

## Features

- **Single Postcode Lookup**: Retrieve detailed information for individual postcodes.
- **Bulk Postcodes Lookup**: Perform bulk queries to find information on multiple postcodes.
- **Random Postcode Lookup**: Provide a random postcode if none provided.

## Classes

### Postcode

The `Postcode` class handles single postcode lookups. It retrieves data from the Postcodes.io API and stores the postcode, primary care trust, and parliamentary constituency information. If the API response is successful (HTTP status code 200), it parses the JSON response and stores the relevant data. If not, it prints an error message. It also includes a `save_json` method to save the retrieved data as a JSON file.

### Postcodes

The `Postcodes` class handles bulk postcode lookups. Similar to the `Postcode` class, it retrieves data from the Postcodes.io API and stores the JSON response. However, it doesn't support random postcode lookups and raises an exception if no postcode is provided. It also includes a `save_json` method to save the retrieved data as a JSON file.

## Usage

```python
from postcodes import Postcode, Postcodes

# Single postcode lookup
p = Postcode("NN9 5XD")
print(p.postcode)  # Prints the postcode
p.save_json("postcode_data")  # Saves the data as postcode_data.json

# Bulk postcode lookup
p = Postcodes(["NN9 5XD", "NN8 1LD"])
p.save_json("postcodes_data")  # Saves the data as postcodes_data.json