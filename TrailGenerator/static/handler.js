function generate() {
    document.getElementById("output")?.remove();

    const place = document.getElementById("text").value;

    if (!place) {
        let text = document.createElement("textarea");
        text.id = "output";
        text.value = "Please enter a park";
        text.readOnly = true;
        text.style.display = "block";
        text.style.margin = "0 auto";
        text.style.resize = "none";

        const area = document.getElementById("outputArea");
        area.appendChild(text);
        return;
    }
    
    // Query selector finds a specific tag, :checked is used to find which radio button was pressed
    const levelDiff = document.querySelector('input[name="diff"]:checked')?.value;
    let levelSelected = levelDiff ? true: false;

    const len = document.querySelector('input[name="dist"]:checked')?.value;
    let lenSelected = len ? true: false;

    // If neither group of radio buttons was selected, tell the user to select one or both
    if (!levelSelected && !lenSelected) {
        let text = document.createElement("textarea");
        text.id = "output";
        text.value = "Please select the difficulty, distance, or both";
        text.readOnly = true;
        text.style.display = "block";
        text.style.margin = "0 auto";
        text.style.resize = "none";

        const area = document.getElementById("outputArea");
        area.appendChild(text);
        return;
    }

    // Creates the data that is going to be sent to app.py
    const info = {
        park: place,
        diff: levelDiff ?? null, // The ?? operator assigns diff to null if levelDiff is undefined
        diffSelected: levelSelected,
        dist: len ?? null,
        distSelected: lenSelected,
    }

    // Connects to the Flask get_trails function and makes all the data into JSON strings
    fetch("/get_trails", {
        method: "POST",
        headers: {
            "Content-Type": "application/json" // Need this header to show that I am sending JSON to Flask
        },
        body: JSON.stringify(info),
    })
    .then(response => {
        if (!response.ok) {
            throw new Error("Program ran into an exception.");
        }
        return response.json(); //parses the response from app.py as JSON
    })
    .then(data => {
        let text = document.createElement("textarea");
        text.id = "output";
        text.readOnly = true;
        text.style.width = "500px";
        text.style.height = "80px";
        text.style.fontSize = "12px";
        text.style.display = "block";
        text.style.margin = "0 auto";
        text.style.resize = "none";

        if (data.length == 0) {
            text.value = "Could not find trails under the specified preferences";
        } else {
            for (let i = 0; i < data.length; i++) {
                let name = data[i]["name"];
                let difficulty = data[i]["difficulty"];
                let mileage = data[i]["mileage"];
                let elevation = data[i]["elevation"];
                
                text.value += "Trail: " + name + ", " + "Difficulty: " + difficulty + ", " + 
                mileage + " miles, " + elevation + " ft. \n";
            }
        }
        
        const area = document.getElementById("outputArea");
        area.appendChild(text);
    })
    .catch(error => console.error(error));
    
}