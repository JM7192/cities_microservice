# cities_microservice

Apex Social Network: cities_microservice
Introduction

This is a text-based social network service where users can create profiles, create posts and view posts made by other users. The service is currently in alpha and new features will be added in future releases.
Features

    Create profile
    Create post
    View posts

How to Request:
- Make sure cities_request.py is running (on localhost:5000)
- If using Python follow the following steps:
    - import http.client
    - establish a connection using http.client.HTTPConnection("localhost:5000")
    - create a request using conn.request("GET", "/") to create a get-request to root
    - create a variable to store the response
- The microservice will read from all 1000 user profiles in userProfiles.json and select a random set of 50 cities to return in a json file
How to Receive:
    - if the response is "200", read and decode the response using response.read().decode()
    - Any codes other than 200 will fail.
    - The response will contain a JSON file called cities.json containing 50 random cities from the available users in userProfiles.json
    - You may continue to make requests for new cities as many times as you like

![Sequence Diagram](https://user-images.githubusercontent.com/38779850/218405529-a0190d75-2de5-4034-876f-4665d127b80d.JPG)
