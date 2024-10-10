'''
We have an endless chessboard, and on each cell there is a number written in a spiral.
16ㅤㅤ15ㅤㅤ14ㅤㅤ13ㅤㅤ12
17ㅤㅤ4 ㅤㅤ3 ㅤㅤ2 ㅤㅤ11
18ㅤㅤ5 ㅤㅤ0 ㅤㅤ1 ㅤㅤ10
19ㅤㅤ6 ㅤㅤ7 ㅤㅤ8 ㅤㅤ9ㅤㅤ
20ㅤㅤ21ㅤㅤ22ㅤㅤ23ㅤㅤ24ㅤㅤ25

And we have a knight. A normal chess knight moves +1 to one axis and +2 to the other.
But this knight moves +n to one axis and +m to the other.
And this knight has two more rules: He cannot move to the same square twice,
and he only moves to the smallest available square. For example, an ordinary knight (n=1, m=2) starts his journey like this:
0 -> 9 -> 2 -> 5 -> 8 -> ...
But someday he will reach a cell from which he will not be able to get out without violating the rule,
it is this last cell that the function must return. For this case it 2083
Performance requirements:
Values of m up to 300_000_000 will be tested in fixed tests. Multiple random tests with m up to 20_000.
You will always have 0 < n < m.
'''


def generate_spiral(n, m):
    x, y = 0, 0
    dx, dy = 0, -1
    visited = {}
    i = 0
    min_x, max_x = -n, n
    min_y, max_y = -m, m
    while True:
        if (x, y) not in visited:
            visited[(x, y)] = i
            yield (x, y), i
            i += 1
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        if not (min_x <= x <= max_x and min_y <= y <= max_y):
            x, y = 0, 0
            dx, dy = 0, -1
            min_x, max_x = min_x - n, max_x + n
            min_y, max_y = min_y - m, max_y + m

def get_knight_moves(x, y, n, m):
    return [
        (x + n, y + m),
        (x + n, y - m),
        (x - n, y + m),
        (x - n, y - m),
        (x + m, y + n),
        (x + m, y - n),
        (x - m, y + n),
        (x - m, y - n)
    ]

def knight_tour(n, m):
    spiral_gen = generate_spiral(n, m)
    spiral_map = {}
    visited = {(0, 0)}
    path = [((0, 0), 0)]
    x, y = 0, 0

    # Генерируем координаты заранее в пределах (x-n <= x <= x+n) и (y-m <= y <= y+m)
    for _ in range(100):
        coord, value = next(spiral_gen)
        spiral_map[coord] = value

    while True:
        moves = get_knight_moves(x, y, n, m)
        possible_moves = []

        for move in moves:
            if move not in visited:
                if move not in spiral_map:
                    coord, value = next(spiral_gen)
                    spiral_map[coord] = value
                possible_moves.append(move)

        if not possible_moves:
            break

        move = min(possible_moves, key=lambda move: spiral_map[move])
        visited.add(move)
        path.append((move, spiral_map[move]))
        x, y = move

        # Генерируем новые координаты в пределах (x-n <= x <= x+n) и (y-m <= y <= y+m) каждый ход
        coord, value = next(spiral_gen)
        spiral_map[coord] = value

    return path

# Параметры: n = 1, m = 2
path = knight_tour(1, 2)

for step in path:
    print(f"Клетка: {step[0]}, Значение: {step[1]}")

# Последняя посещенная ячейка
print(f"Последняя посещенная ячейка: {path[-1][0]}, Значение: {path[-1][1]}")



