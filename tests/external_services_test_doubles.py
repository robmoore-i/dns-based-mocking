import dnsdouble

dnsdouble.stub("github.com", "abc class=\"hello\" def")
dnsdouble.stub("www.google.com", "tttttttttttttttttttttttttttttt")
dnsdouble.activate_double()
