'''
This part was copied from https://github.com/jonathanpaulson/AdventOfCode/blob/master/2022/10.py
Mainly the handle_tick() function
Just wanted to learn because I was having trouble understanding the question
'''

G = [['?' for _ in range(40)] for _ in range(6)]


def handle_tick(cycleTime, x):
    global G
    t1 = cycleTime - 1
    G[t1 // 40][t1 % 40] = ('#' if abs(x - (t1 % 40)) <= 1 else ' ')


def main(lines):
    X = 1
    cycleTime = 0
    global G

    for i in lines:
        if i[0] == 'a':
            firstPart, secondPart = i.split(' ', 1)
            num = int(secondPart)
            cycleTime += 1
            handle_tick(cycleTime, X)
            cycleTime += 1
            handle_tick(cycleTime, X)
            X += num
        else:
            cycleTime += 1
            handle_tick(cycleTime, X)

    for a in range(6):
        print(''.join(G[a]))


if __name__ == "__main__":
    with open('./input.txt') as file:
        lines = file.read().splitlines()

    main(lines)
