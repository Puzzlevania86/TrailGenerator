from flask import Flask, request
from preferences import checkPreferences #Getting function from preferences.py

#Creates an instance of the Flask class which can later be ran with app.run()
app = Flask(__name__)

#Takes in data from JS and returns the preferences 
@app.route("/get_trails", methods=["POST"])
def get_trails():
    data = request.get_json()
    park = data["park"]
    diff = data["diff"]
    diffSelected = bool(data["diffSelected"])
    dist = data["dist"]
    distSelected = bool(data["distSelected"])
    
    preferences = checkPreferences(park, diff, diffSelected, dist, distSelected)
    return preferences
    
if __name__ == "__main__":
    app.run()