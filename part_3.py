def main():
    try:
        speed = int(input("Enter motor speed: "))
        print("Speed set to ", speed)

    except:
        print("Error: Corrupted Signal. Maintaining current speed.")

    xCoord = get_coordinate()

def get_coordinate():
    while True:
        
        try:
            xCoord = int(input("Please enter a valid X-Coordinate: "))

        except:
            print("Invalid")

        if xCoord > 100 or xCoord < -100:
            print("Invalid")

        else:
            break

    return xCoord   

main()