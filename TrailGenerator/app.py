from flask import Flask, request, jsonify, render_template
from preferences import checkPreferences #Getting function from preferences.py

#Creates an instance of the Flask class which can later be ran with app.run()
app = Flask(__name__)

# Flask runs this function when someone visits the corresponding URL
@app.route("/")
def home():
    return render_template("screen.html") #HTML file has to be in a templates directory and JS has to be in static

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
    return jsonify(preferences)
    
if __name__ == "__main__":
    app.run()