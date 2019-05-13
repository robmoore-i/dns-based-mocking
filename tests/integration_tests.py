import requests
from assertpy import *

response = requests.get("http://localhost:8080")
expected_oracle_prediction = "olleh tttttttttt"
assert_that(response.text).is_equal_to("The oracle has seen your future: \"" + expected_oracle_prediction + "\"")
print("Pass")
