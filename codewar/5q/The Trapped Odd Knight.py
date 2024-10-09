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


def generate_spiral(limit):
    spiral = {}
    x, y = 0, 0
    dx, dy = 0, -1
    for i in range(limit ** 2):
        if (-limit // 2 < x <= limit // 2) and (-limit // 2 < y <= limit // 2):
            spiral[(x, y)] = i
        if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1 - y):
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
    return spiral


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


def knight_tour(n, m, limit):
    spiral = generate_spiral(limit)
    visited = set()
    path = []
    x, y = 0, 0

    while len(path) < limit:
        moves = get_knight_moves(x, y, n, m)
        moves = [move for move in moves if move in spiral and move not in visited]
        if not moves:
            break
        move = min(moves, key=lambda move: spiral[move])
        visited.add(move)
        path.append((move, spiral[move]))
        x, y = move

    return path


# Параметры: n = 1, m = 2, размер спирали = 100
path = knight_tour(1, 2, 10000)

for step in path:
    print(f"Клетка: {step[0]}, Значение: {step[1]}")