#parkName is temporary until geocoding API is implemented
parkName = "Joshua Tree"

def checkPreferences(diff, diffSelected, dist, distSelected):
    if not diffSelected and not distSelected:
        return 
    
    trails = []
    diffs = []
    mileage = []
    heights = []
    
    with open("TrailGenerator/csv.txt") as csv:
        for line in csv:
            parts = line.split(",")
            if parts[0] == parkName:
                #checks if both difficulty and distance buttons were selected
                if diffSelected and distSelected:  
                    if parts[2].strip() == diff and distanceChecker(dist, float(parts[3])):
                        trails.append(parts[1].strip())
                        diffs.append(parts[2].strip())
                        mileage.append(parts[3].strip())
                        heights.append(parts[4].strip())
                #checks only for the difficulty button
                elif diffSelected:
                    if parts[2].strip() == diff:
                        trails.append(parts[1].strip())
                        diffs.append(parts[2].strip())
                        mileage.append(parts[3].strip())
                        heights.append(parts[4].strip())
                #checks for the distance button (no buttons was handled at the start of the function)
                else:
                    if distanceChecker(dist, float(parts[3])):
                        trails.append(parts[1].strip())
                        diffs.append(parts[2].strip())
                        mileage.append(parts[3].strip())
                        heights.append(parts[4].strip())
    
    if not trails:
        print("No Trails That Meet These Specifications")

    for i in range(len(trails)):
        print(f"Trail: {trails[i]}, Diff: {diffs[i]}, Length: {mileage[i]}, Elevation: {heights[0]}")
    
    return
 
# function checks whether the line's trail length is in the range specified by the user
def distanceChecker(dist, trailLength) -> bool:
    if dist == "Between 0.1 and 3.0":
        if 0.1 < trailLength < 3.0 or abs(trailLength - 0.1) < 0.001 or abs(trailLength - 3.0) < 0.001:
            return True
        else:
            return False
    elif dist == "Between 3.1 and 6.0":
        if 3.1 < trailLength < 6.0 or abs(trailLength - 3.1) < 0.001 or abs(trailLength - 6.0) < 0.001:
            return True
        else:
            return False
    elif dist == "Between 6.1 and 9.0":
        if 6.1 < trailLength < 9.0 or abs(trailLength - 6.1) < 0.001 or abs(trailLength - 9.0) < 0.001:
            return True
        else:
            return False
    elif dist == "Between 9.1 and 12.0":
        if 9.1 < trailLength < 12.0 or abs(trailLength - 9.1) < 0.001 or abs(trailLength - 12.0) < 0.001:
            return True
        else:
            return False
    elif dist == "Greater than 12.0":
        return trailLength > 12.0
    else:
        return False

# checkPreferences("Easy", True, "Between 0.1 and 3.0", True)