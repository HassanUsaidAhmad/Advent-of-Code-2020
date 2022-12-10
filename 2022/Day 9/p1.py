def main():
    with open('./test.txt') as file:
        # lines = file.read().splitlines()
        lines = [[i[:1], int(i[2:])] for i in file.read().splitlines()]

    seen = set()
    HEAD = 0
    TAIL = 0
    for i in range(len(lines)):
        for a in range(lines[i][1]):
            if lines[i][0] == 'R':
                seen.add(lines[i][1]-1)
            elif lines[i][0] == 'U':
                seen.add(lines[i][1]-1)
            elif lines[i][0] == 'L':
                seen.add(lines[i][1]-1)
            elif lines[i][0] == 'D':
                seen.add(lines[i][1]-1)

    print(seen)
    print(len(seen))
    print('sum', sum(seen))



if __name__ == "__main__":
    main()