def main():
    with open('./test.txt') as file:
        lines = file.read().splitlines()
    #   1 - Rock - X  (A)          Loss - 0 Points
    #   2 - Paper - Y  (B)         Draw - 3 Points
    #   3 - Scissors - Z (C)        Win - 6 Points
    points = 0
    for i in lines:
        if i[:1] == 'A' and i[-1] == 'X':
            points = points + 3
        elif i[:1] == 'A' and i[-1] == 'Y':
            points = points + 1 + 3
        elif i[:1] == 'A' and i[-1] == 'Z':
            points = points + 2 + 6
        # Paper
        if i[:1] == 'B' and i[-1] == 'X':
            points = points + 1
        elif i[:1] == 'B' and i[-1] == 'Y':
            points = points + 2 + 3
        elif i[:1] == 'B' and i[-1] == 'Z':
            points = points + 3 + 6
        # Scissors
        if i[:1] == 'C' and i[-1] == 'X':
            points = points + 2
        elif i[:1] == 'C' and i[-1] == 'Y':
            points = points + 3 + 3
        elif i[:1] == 'C' and i[-1] == 'Z':
            points = points + 1 + 6

    print(points)

if __name__ == "__main__":
    main()