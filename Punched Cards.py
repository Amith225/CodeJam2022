__points__ = 11

n = int(input())

for i in range(n):
    r, c = map(int, input().split())

    print('Case', f'#{i + 1}:')
    print('..', '+', '-+' * (c - 1), sep='')
    print('..', '|', '.|' * (c - 1), sep='')
    print(('+' + '-+' * c + '\n' + '|' + '.|' * c + '\n') * (r - 1), '+' + '-+' * c, sep='')
