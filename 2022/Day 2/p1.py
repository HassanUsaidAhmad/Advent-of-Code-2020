def main():
    with open('./input.txt') as file:
        lines = file.read().splitlines()
    #   1 - Rock - X  (A)          Loss - 0 Points
    #   2 - Paper - Y  (B)         Draw - 3 Points
    #   3 - Scissors - Z (C)        Win - 6 Points
    points = 0
    for i in lines:
        # Rock
        if i[-1] == 'X' and i[:1] == 'C':
            points = points + 1 + 6
        elif i[-1] == 'X' and i[:1] == 'A':
            points = points + 1 + 3
        elif i[-1] == 'X' and i[:1] == 'B':
            points = points + 1
        # Paper
        elif i[-1] == 'Y' and i[:1] == 'A':
            points = points + 2 + 6
        elif i[-1] == 'Y' and i[:1] == 'B':
            points = points + 2 + 3
        elif i[-1] == 'Y' and i[:1] == 'C':
            points = points + 2
        # Scissors
        elif i[-1] == 'Z' and i[:1] == 'B':
            points = points + 3 + 6
        elif i[-1] == 'Z' and i[:1] == 'C':
            points = points + 3 + 3
        elif i[-1] == 'Z' and i[:1] == 'A':
            points = points + 3

    print(points)

if __name__ == "__main__":
    main()