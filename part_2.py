def main():
    rover_status = {
        "Battery": 100,
        "Heater": "Off",
        "Camera": "Standby"
    }

    print("Battery: ", rover_status["Battery"])

    rover_status["Battery"] = 85
    rover_status["Heater"] = "On"
    rover_status["Speed"] = 5

    print(rover_status)

    mission_log = [{
        "Site": "Crater A",
        "Radiation": "Low",
        "Water": "False"
    },
    {
        "Site": "Dune B",
        "Radiation": "High",
        "Water": "True"
    }]

    for i in range(len(mission_log)):
        print("Site ", mission_log[i]["Site"], " has ", mission_log[i]["Radiation"], " radiation.")

main()