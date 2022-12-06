def main():
    with open('./input.txt') as file:
        lines = file.read().strip()

    # Orignal Solution
    '''
    string = lines[0]
    for i in range(len(string)):
        print(i+1 , string[i], string[i+1], string[i+2], string[i+3], string[i+4], string[i+5], string[i+6], string[i+7], string[i+8], string[i+9], string[i+10], string[i+11], string[i+12], string[i+13])
        if string[i] != string[i+1] and string[i] != string[i+2] and string[i] != string[i+3] and string[i] != string[i+4] and string[i] != string[i+5] and string[i] != string[i+6] and string[i] != string[i+7] and string[i] != string[i+8] and string[i] != string[i+9] and string[i] != string[i+10] and string[i] != string[i+11] and string[i] != string[i+12] and string[i] != string[i+13]\
           and string[i+1] != string[i+2] and string[i+1] != string[i+3] and string[i+1] != string[i+4] and string[i+1] != string[i+5] and string[i+1] != string[i+6] and string[i+1] != string[i+7] and string[i+1] != string[i+8] and string[i+1] != string[i+9] and string[i+1] != string[i+10] and string[i+1] != string[i+11] and string[i+1] != string[i+12] and string[i+1] != string[i+13]\
           and string[i+2] != string[i+3] and string[i+2] != string[i+4] and string[i+2] != string[i+5] and string[i+2] != string[i+6] and string[i+2] != string[i+7] and string[i+2] != string[i+8] and string[i+2] != string[i+9] and string[i+2] != string[i+10] and string[i+2] != string[i+11] and string[i+2] != string[i+12] and string[i+2] != string[i+13]\
           and string[i+3] != string[i+4] and string[i+3] != string[i+5] and string[i+3] != string[i+6] and string[i+3] != string[i+7] and string[i+3] != string[i+8] and string[i+3] != string[i+9] and string[i+3] != string[i+10] and string[i+3] != string[i+11] and string[i+3] != string[i+12] and string[i+3] != string[i+13]\
           and string[i+4] != string[i+5] and string[i+4] != string[i+6] and string[i+4] != string[i+7] and string[i+4] != string[i+8] and string[i+4] != string[i+9] and string[i+4] != string[i+10] and string[i+4] != string[i+11] and string[i+4] != string[i+12] and string[i+4] != string[i+13]\
           and string[i+5] != string[i+6] and string[i+5] != string[i+7] and string[i+5] != string[i+8] and string[i+5] != string[i+9] and string[i+5] != string[i+10] and string[i+5] != string[i+11] and string[i+5] != string[i+12] and string[i+5] != string[i+13]\
           and string[i+6] != string[i+7] and string[i+6] != string[i+8] and string[i+6] != string[i+9] and string[i+6] != string[i+10] and string[i+6] != string[i+11] and string[i+6] != string[i+12] and string[i+6] != string[i+13]\
           and string[i+7] != string[i+8] and string[i+7] != string[i+9] and string[i+7] != string[i+10] and string[i+7] != string[i+11] and string[i+7] != string[i+12] and string[i+7] != string[i+13]\
           and string[i+8] != string[i+9] and string[i+8] != string[i+10] and string[i+8] != string[i+11] and string[i+8] != string[i+12] and string[i+8] != string[i+13]\
           and string[i+9] != string[i+10] and string[i+9] != string[i+11] and string[i+9] != string[i+12] and string[i+9] != string[i+13]\
           and string[i+10] != string[i+11] and string[i+10] != string[i+12] and string[i+10] != string[i+13]\
           and string[i+11] != string[i+12] and string[i+11] != string[i+13]\
           and string[i+12] != string[i+13]:
            print('The i is', i+14)
            exit()
    '''
    # Thank you Isaac
    START_OF_PACKET = 14

    for i in range(len(lines)):
        if len(set(lines[i:i+START_OF_PACKET])) == START_OF_PACKET:
            print(i + START_OF_PACKET)
            break


if __name__ == "__main__":
    main()