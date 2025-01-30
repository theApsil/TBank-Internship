import sys
import math

sys.setrecursionlimit(10**7)

def solve(n, s, a):
    p = [0]*(n+1)
    for i in range(n):
        p[i+1] = p[i] + a[i]

    nxt = [n+1]*(n+1)  
    r = 1
    for i in range(1, n+1):
        while r <= n and p[r] - p[i-1] <= s:
            r += 1
        nxt[i] = r 
   
    LOG = math.ceil(math.log2(n+1))+1
    jump = [ [n+1]*(n+2) for _ in range(LOG) ]

    for i in range(1, n+1):
        jump[0][i] = nxt[i]

    for k in range(1, LOG):
        for i in range(1, n+1):
            jump[k][i] = jump[k-1][ jump[k-1][i] ]

    def pieces_count(l, r):
        if l > r:
            return 0
        res = 0
        cur = l

        while cur <= r:
            moved = False
            for k in reversed(range(LOG)):
                nxtpos = jump[k][cur]
                if nxtpos <= r:
                    cur = nxtpos
                    res += (1 << k)  
                    moved = True
                    break
            if not moved:
                res += 1
                break

        return res

    sum_f = 0
    for l in range(1, n+1):
        for r in range(l, n+1):
            sum_f += pieces_count(l, r)

    return sum_f


n, s = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, s, a))
