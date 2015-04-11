import math

def solve(x, r, c):
    area = r * c

    bs = x / 2 + 1 if x % 2 == 0 else math.ceil(x / 2.0)

    if x == 1:
        return "GABRIEL"
    if x == 2 and area % 2 == 0:
        return "GABRIEL"
    if r < x and c < x:
        return "RICHARD"
    if area % x != 0:
        return "RICHARD"
    if r < bs or c < bs:
        return "RICHARD"
    return "GABRIEL"

if __name__ == '__main__':
    f = open('input')
    n = int(f.readline().rstrip())

    for case in range(n):
        x, r, c = map(int, f.readline().rstrip().split())
        print('Case #{0}: {1}'.format(case + 1, solve(x, r, c)))
