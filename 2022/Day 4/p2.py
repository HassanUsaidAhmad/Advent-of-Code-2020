def main():
    with open('./input.txt') as file:
        lines = file.read().splitlines()

    counter = 0
    for i in lines:
        newI = i.replace('-', ',').split(',')
        newList = list(map(int, newI))
        num1set1, num2set1, num1set2, num2set2 = newList[0], newList[1], newList[2], newList[3]

        if num1set2 <= num1set1 <= num2set2 or num1set2 <= num2set1 <= num2set2:
            counter += 1
        elif num1set1 <= num1set2 <= num2set1 or num1set1 <= num2set2 <= num2set1:
            counter += 1

    print(counter)


if __name__ == "__main__":
    main()