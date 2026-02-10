def main():
    status = {
        "Power": 100,
        "Samples": 0
    }

    inventory = []

    command_batch = [
    "MOVE 10",
    "TURN LEFT",
    "MOVE 5",
    "MOVE five",    # Corrupted: 'five' is text, not a number
    "DIG",
    "MOVE 20",
    "XÆA-12",       # Corrupted: Unknown command
    "RETURN",
    "MOVE 15"
    ]

    for i in range(len(command_batch)):
        command = command_batch[i].split

    rover_state = {
        "x": 0,
        "y": 0,
        "samples": 0
    }

    while True:
        print("1) Dig for Sample")
        print("2) Report Status")
        print("3) Emergency Stop")

        op = input()

        if op == "1":
            sampleName = input("Please enter sample name: ")
            inventory.append(sampleName)
            status["Power"] = status["Power"] - 10
            status["Samples"] = len(inventory)

        elif op == "2":
            print(status)
            print(inventory)

        elif op == "3":
            break

        else:
            print("Invalid")

main()