#Finds the preferences based on the user's specified difficulty and/or distance
def checkPreferences(parkName, diff, diffSelected, dist, distSelected):
    if not diffSelected and not distSelected:
        return []
    
    trails = []
    
    with open("TrailGenerator/csv.txt") as csv:
        for line in csv:
            parts = line.split(",")
            if parts[0] == parkName:
                #checks if both difficulty and distance buttons were selected
                if diffSelected and distSelected:  
                    if parts[2].strip() == diff and distanceChecker(dist, float(parts[3])):
                        res = addData(parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip())
                        trails.append(res)
                #checks only for the difficulty button
                elif diffSelected:
                    if parts[2].strip() == diff:
                        res = addData(parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip())
                        trails.append(res)
                #checks for the distance button (no buttons was handled at the start of the function)
                else:
                    if distanceChecker(dist, float(parts[3])):
                        res = addData(parts[1].strip(), parts[2].strip(), parts[3].strip(), parts[4].strip())
                        trails.append(res)
    
    if not trails:
        return []
    
    return trails

# function adds trail data into a dictionary that is returned to the checkPreferences() function
def addData(data1, data2, data3, data4):
    trailData = {}
    trailData["name"] = data1
    trailData["difficulty"] = data2
    trailData["mileage"] = data3
    trailData["elevation"] = data4
    return trailData
 
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

