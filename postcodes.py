from postcodes_class import *


# Single postcode lookup with GET
postcodes1 = Postcode("TW13 6JH")
postcodes1.get_detail()

# Single postcode lookup with GET & Write to json
postcodes2 = Postcode("SW1A 1AA")
postcodes2.get_detail()
postcodes2.save_json("json_test")

# Postcode lookup error test
postcodes3 = Postcode("TW99 9ZZ")
postcodes3.get_detail()

# Bulk lookup postcodes with POST
postcodes4_6 = Postcodes(["OX49 5NU", "M32 0JG", "NE30 1DP"])
postcodes4_6.get_detail()
postcodes4_6.save_json("json_test")

# Random postcode test for parent class
postcode_none = Postcode()
postcode_none.get_detail()

# Random postcodes test for child class
postcodes_none = Postcodes()
postcodes_none.get_detail()
