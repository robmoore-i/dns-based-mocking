# External Server Mocking

## Problem

I want to test a RESTful API, but...

- the functionality I want to verify requires that I stub the responses of other servers.

- I want to make assertions on the requests that the API sends to its dependencies

## This solution

Mess with local DNS configuration to enable developers to control the interactions of the fixture with its external
runtime dependencies.

