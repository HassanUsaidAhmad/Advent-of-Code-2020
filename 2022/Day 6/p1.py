def main():
    with open('./input.txt') as file:
        lines = file.read().strip()

    # Orignal Solution
    '''
    string = lines[0]
    for i in range(len(string)):
        print(i+1 , string[i+3], string[i+2], string[i+1], string[i])
        if string[i+3] != string[i+2] and string[i+3] != string[i+1] and string[i+3] != string[i] \
           and string[i+2] != string[i+1] and string[i+2] != string[i] \
           and string[i+1] != string[i]:
            print('The i is', i+4)
            exit()
    '''
    # Thank you Isaac
    START_OF_PACKET = 4

    for i in range(len(lines)):
        if len(set(lines[i:i+START_OF_PACKET])) == START_OF_PACKET:
            print(i + START_OF_PACKET)
            break


if __name__ == "__main__":
    main()