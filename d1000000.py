__points__ = 9 + 11

t = int(input())

for i in range(t):
    n = int(input())
    s = sorted((map(int, input().split())))

    print('Case', f'#{i + 1}:', end=' ')
    length = 0
    i = 0
    while i < n:
        if s[i] > length:
            length += 1
            i += 1
        else:
            length -= 1
    print(length)
