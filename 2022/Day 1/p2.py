def main():
    with open('./input.txt') as file:
        lines = file.read().splitlines()
    count = 0
    ansArr = []

    for i in lines:
        if i != '':
            newNum = int(i)
            count = count + newNum
        else:
            ansArr.append(count)
            count = 0
    ansArr.append(count)
    ansArr.sort(reverse=True)
    print(ansArr[0] + ansArr[1] + ansArr[2])

if __name__ == "__main__":
    main()