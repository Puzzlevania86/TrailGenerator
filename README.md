# TrailGenerator

Generates trails at national parks based on your location and preferred difficulty

## The Problem

It is often hard to find what trails you may want to go on. This site is intended to provide users with the highest-rated trails at whatever difficulty they prefer. 

## How It Works

- Program takes in data from a CSV file about various national parks and the highest rated trails at each location
- The site allows the user to enter their location or of a location they would like to view
- Python "geocodes" these locations, finding the closest relevant national parks
- Then, the user can specify what kind of difficulty, mileage, and incline they may want
- These preferences inform the program to return trails that relate to your designated preferences

![System Diagram](https://github.com/user-attachments/assets/6e613fae-1d8b-44e6-b9e6-a7d37dba1314)

## Tech Stack

- **Languages**: HTML/CSS, Python, JavaScript
- **External Tools**: Geocoding API by Geoapify

## How to Use

Run localhost on your computer with LiveServer VSCode Extension

## Roadmap

- [ ] Put all data in a CSV file manually
- [ ] Use Python to break apart the CSV file
- [ ] Get data from Python to JavaScript
- [ ] Implement basic HTML page and CSS Styling using JavaScript function(s)
- [ ] Figure out best way to represent trail data
- [ ] Implement Python API handler and test
- [ ] Use python data in JavaScript/HTML
- [ ] Improve UI
- [ ] Add more national parks/trails if time

## Author 

Xander Smits, [Github link](https://github.com/Puzzlevania86)


