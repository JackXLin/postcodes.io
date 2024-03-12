from postcodes_class import *


# Single postcode lookup with GET
postcodes1 = Postcode("TW13 6JH")
print(postcodes1.postcode)
print(postcodes1.parliamentary_constituency)
print(postcodes1.primary_care_trust)
postcodes1.save_json("json_test")


# Single postcode lookup with GET & Write to json
postcodes2 = Postcode("SW1A 1AA")
print(postcodes2.primary_care_trust)
postcodes2.save_json("json_test")

# Postcode lookup error test
postcodes3 = Postcode("TW99 9ZZ")
print(postcodes3.postcode)

# # Bulk lookup postcodes with POST
postcodes4_6 = Postcodes(["OX49 5NU", "M32 0JG", "NE30 1DP"])
print(postcodes4_6.postcode)
postcodes4_6.save_json("test")

# # Random postcode test for parent class
postcode_none = Postcode()
print(postcode_none.postcode)
postcode_none.save_json("json_test1")

# # Random postcodes test for child class
postcodes_none = Postcodes()
postcodes_none.get_detail()
