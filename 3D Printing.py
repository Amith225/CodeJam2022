__points__ = 13

reqInk = int(1e6)


def findColor(pr1, pr2, pr3):
    cMin = [min(c) for c in zip(pr1, pr2, pr3)]
    color = [0] * 4
    for j, c in enumerate(cMin):
        sCol = sum(color)
        left = reqInk - sCol
        color[j] = c if c + sCol < reqInk else max(0, left)
    if sum(color) < reqInk: return
    else: return color


n = int(input())
for i in range(n):
    p1 = tuple(map(int, input().split()))
    p2 = tuple(map(int, input().split()))
    p3 = tuple(map(int, input().split()))

    col = findColor(p1, p2, p3)
    print("Case", f'#{i+1}: ', end='')
    if col: print(*col)
    else: print("IMPOSSIBLE")
