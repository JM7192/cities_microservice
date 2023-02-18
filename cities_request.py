import json
import random
from http.server import HTTPServer, BaseHTTPRequestHandler


class RequestHandler(BaseHTTPRequestHandler):
    """RequestHandler is a class from BaseHTTPRequestHandler that handles 'GET' requests to the server."""
    def do_GET(self):
        """Altered method to handle 'GET' requests made to this server."""
        if self.path == "/":
            # The request URL is the root
            with open("userProfiles.json", "r") as file:
                # Open the JSON of user profiles and load it to dictionary
                users = json.load(file)

            # Retrieve all the values for 'city' from the available users in the JSON file
            cities = [user["city"] for user in users.values()]
            # Randomly select a sample set of 50 cities from those values
            cities = random.sample(cities, 50)

            # Write the 50 city-values to a separate JSON file
            with open("cities.json", "w") as file:
                json.dump(cities, file)

            # Send a response to the client including the contents of cities.json
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            with open("cities.json", "r") as file:
                self.wfile.write(file.read().encode())


# Server will run on local:5000 until stopped
if __name__ == "__main__":
    server = HTTPServer(("", 5000), RequestHandler)
    print("Serving on port 5000...")
    server.serve_forever()

