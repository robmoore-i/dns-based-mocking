import requests
import dnsdouble
from assertpy import *

dnsdouble.stub("github.com", "abc class=hello def")
dnsdouble.stub("www.google.com", "tttttttttttttttttttttttttttttt")
dnsdouble.activate_double()

response = requests.get("http://localhost:8080")
expected_oracle_prediction = "olleh tttttttttt"
assert_that(response.text).is_equal_to("The oracle has seen your future: \"" + expected_oracle_prediction + "\"")
print("Pass")
