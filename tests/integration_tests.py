import requests
from assertpy import *

# Run tests depending on stubbing
response = requests.get("http://localhost:8080")
expected_oracle_prediction = "olleh tttttttttt"
assert_that(response.text).is_equal_to("The oracle has seen your future: \"" + expected_oracle_prediction + "\"")

# Run tests depending on mocking
response = requests.get("http://dnsmocks.local")
json = response.json()
assert_that(json["github.com"]).starts_with("/search?q=")
assert_that(json["www.google.com"]).starts_with("/search?client=safari&rls=en&q=")
assert_that(json["www.google.com"]).ends_with("&ie=UTF-8&oe=UTF-8")

print("Pass")
