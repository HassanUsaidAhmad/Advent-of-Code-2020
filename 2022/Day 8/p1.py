def main():
    with open('./test.txt') as file:
        lines = file.read().splitlines()

    numsList = []
    for i in lines:
        numsList.append([int(x) for x in str(i)])

    counter = 0
    for i in range(1, len(numsList)-1):
        # print(numsList[i])
        for j in range(len(numsList[i])):
            if j == 0 or j == 4:
                counter += 1
            else:
                # print('i')
                # print(*range(i, -1, -1))
                # print('j')
                # print(*range(j, -1, -1))

                for x in range(i, -1, -1):
                    # print(numsList[x])
                    local = 0
                    if local == 0:
                        print(numsList[x])
                    else:
                        continue
                    if x == 0:
                        local += 1


                # for x in range(5):
                    # if numsList[i][j] > numsList[i-1][j] or numsList[i][j] > numsList[i][j+1] or\
                    #    numsList[i][j] > numsList[i+1][j] or numsList[i][j] > numsList[i][j-1]:

                    # gets the rows
                    # print(numsList[i][j], numsList[i][x])
                    # gets the columns
                    # print(numsList[i][j], numsList[x][j])

                    # if numsList[i][j] > numsList[x][j]:
                    # if numsList[i][j] > numsList[i][x]:
                    #     print(numsList[i][j], numsList[i][x])
                    #     counter += 1
                        # print('counter', counter)

    print(counter)

if __name__ == "__main__":
    main()