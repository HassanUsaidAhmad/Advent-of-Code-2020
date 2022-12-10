def main():
    with open('./test.txt') as file:
        lines = file.read().splitlines()

    test = {}

    count = 0
    for i in range(len(lines)):
        if lines[i][:1] == '$':
            test[count] = []
            count += 1
        else:
            if len(test[count-1]) == 0:
                test[count - 1] = [lines[i]]
            else:
                test[count - 1].append(lines[i])
    print(test)
    idkArr = []
    for i in range(len(test)):
        total = 0
        for j in range(len(test[i])):
            a = test[i][j].split()[0]
            newa = int(a)
            total = total + newa
        idkArr.append(total)

    print(idkArr)


if __name__ == "__main__":
    main()