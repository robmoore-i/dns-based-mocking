# Proof of concept for external server mocking

(Note from the future: I think this may have been misguided. I recommend making the hostnames of your external dependencies configurable so that you don't have to do daft things like this. But it was fun to make and I learnt from making it, so #noregrets.)

## Problem

I want to test a RESTful API, but...

- the functionality I want to verify requires that I stub the responses of other servers which are used in the course
of handling my request.

- I want to make assertions on the requests that the API sends to other servers

## This solution

Mess with local DNS configuration to enable developers to control the interactions of the fixture with its external
runtime dependencies.

## Pros / Cons of this approach (at least the ones I can think of, more are welcome always)

+ (+) I can run integration tests against endpoints that I would otherwise only be able to 
exercise
in an end-to-end test.
- (-) I need root permissions to mess with /etc/hosts
+ (+) Enables more automated tests to run locally on developer machines
- (-) Tests require complicated set up

## Usage of this example

- Open 3 terminal tabs
- In the first, run `./run-dns-mocks`
- In the second, run `./run-fixture`
- In the last, run `./run-tests` (I'm using the assertpy external python library)

The tests should pass and you should see some logging from the two other tabs.
