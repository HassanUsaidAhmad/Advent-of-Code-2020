from itertools import groupby

def main():
    with open('./input.txt') as file:
        lines = file.read().splitlines()

    arr = []
    score = 0
    for i in lines:
        newArr = []
        firstHalf, secondHalf = i[:len(i) // 2], i[len(i) // 2:]

        for char in firstHalf:
            if char in secondHalf:
                newArr.append(char)

        removeConsectiveDuplicate = [i[0] for i in groupby(newArr)]
        arr.append(removeConsectiveDuplicate[0])

    for i in arr:
        if ord('a') <= ord(i) <= ord('z'):
            score += ord(i) - ord('a') + 1
        else:
            score += ord(i) - ord('A') + 27

    print(score)


if __name__ == "__main__":
    main()