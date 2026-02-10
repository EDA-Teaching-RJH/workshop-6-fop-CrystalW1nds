def main():
    sample_bay = ["Basalt", "Silica", "Iron", "Dust"]
    finalIdx = len(sample_bay) - 1
    new_findings = []

    print(sample_bay[0])
    print(sample_bay[finalIdx])

    for i in range(len(sample_bay)):
        print("Transmitting data for: ", sample_bay[i])

    for i in range(3):
        new = input("Please enter a new rock type found: ")
        new_findings.append(new)

    for i in range(len(new_findings)):
        print(new_findings[i])

    for i in range(len(sample_bay)):
        if sample_bay[i] == "Dust":
            sample_bay.pop(i)

    for i in range(len(sample_bay)):
        print(sample_bay[i])


main()
