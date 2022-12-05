def main():
    with open('./input.txt') as file:
        lines = file.read().splitlines()

    # hashMap = {
    #     1:['Z','N'],
    #     2:['M', 'C', 'D'],
    #     3:['P']
    # }

    hashMap = {
        1:['W','M','L','F'],
        2:['B','Z','V','M','F'],
        3:['H','V','R','S','L','Q'],
        4:['F','S','V','Q','P','M','T','J'],
        5:['L','S','W'],
        6:['F','V','P','M','R','J','W'],
        7:['J','Q','C','P','N','R','F'],
        8:['V','H','P','S','Z','W','R','B'],
        9:['B','M','J','C','G','H','Z','W']
    }
    '''
    move 1 from 2 to 1
    move 3 from 1 to 3
    move 2 from 2 to 1
    move 1 from 1 to 2
    '''
    for i in lines:
        newI = i.split(' ')
        str_list = list(filter(None, newI))
        newList = list(map(int, str_list))
        for i in range(newList[0]):
            a = hashMap[newList[1]].pop()
            hashMap[newList[2]].append(a)

    ans = ''
    for i in hashMap:
        a = hashMap[i]
        ans += a[-1]

    print(ans)

if __name__ == "__main__":
    main()