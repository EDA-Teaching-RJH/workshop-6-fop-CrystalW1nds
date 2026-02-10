def main():
    travel_log = []

    while True:

        try:
            angle = int(input("Sensor reading (slope angle): "))

        except:
            print("Sensor Glitch.")

        if angle > 45:
            print("CRITICAL TILT! HALTING.")
            break

        travel_log.append(angle)
        print("Path stable. Moving forward.")

    print("Mission Terminated.")
    print("Total steps taken: ", len(travel_log))
    print(travel_log)

main()