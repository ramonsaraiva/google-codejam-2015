import datetime

quaternions = {}
quaternions['1'] = {'1': '1', 'i': 'i', 'j': 'j', 'k': 'k'}
quaternions['i'] = {'1': 'i', 'i': '-1', 'j': 'k', 'k': '-j'}
quaternions['j'] = {'1': 'j', 'i': '-k', 'j': '-1', 'k': 'i'}
quaternions['k'] = {'1': 'k', 'i': 'j', 'j': '-i', 'k': '-1'}

after = {}
after['i'] = 'j'
after['j'] = 'k'

def substrings_of(s):
    l = len(s)
    return [s[:j+1] for j in range(l)]

def _try(s, expected):
    for x in range(len(s)):
        sub = s[:x+1]
        q = ''
        for i,c in enumerate(sub):
            if len(sub) == 1 and c == expected:
                return s
            if q == '':
                q = c
                continue

            negative = False
            p = ''
            if q[0] == '-':
                q = q[1]
                negative = not negative
            if c[0] == '-':
                c = c[1]
                negative = not negative
            if negative:
                p = '-'

            if quaternions[q][c][0] == '-':
                if p == '-':
                    q = quaternions[q][c][1]
                else:
                    q = p + quaternions[q][c]
            else:
                q = p + quaternions[q][c]
        if q == expected:
            return sub
    return ''

def solve(s):
    if len(s) < 3:
        return "NO"
    if s == 'ijk':
        return "YES"
    r = _try(s, 'i')
    if not r:
        return "NO"
    r = _try(s[len(r)-2:], 'j')
    if not r:
        return "NO"
    r = _try(s[len(r)-1:], 'k')
    return "YES" if r else "NO"


if __name__ == '__main__':
    f = open('input')
    n = int(f.readline().rstrip())

    print(datetime.datetime.now())
    for case in range(n):
        l, x = map(int, f.readline().rstrip().split())
        s = f.readline().rstrip()
        s = s * x
        print('Case #{0}: {1}'.format(case + 1, solve(s)))
    print(datetime.datetime.now())
