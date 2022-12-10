def signalStrengths(lines, cycleNumber):
    X = 1
    cycleTime = 0

    for i in lines:
        if cycleTime >= cycleNumber:
            break
        if i[0] == 'a':
            firstPart, secondPart = i.split(' ', 1)
            num = int(secondPart)
            cycleTime += 2
            if cycleTime >= cycleNumber:
                break
            X += num
        else:
            if cycleTime >= cycleNumber:
                break
            cycleTime += 1

    return X * cycleNumber


def main(lines):
    finalAns = 0
    for i in range(20, 221, 40):
        finalAns += signalStrengths(lines, i)

    print(finalAns)


if __name__ == "__main__":
    with open('./input.txt') as file:
        lines = file.read().splitlines()

    main(lines)
