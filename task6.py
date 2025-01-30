import math
from collections import defaultdict

def solve(n, points):
    if n < 3:
        return 0

    def gcd(a, b):
        return math.gcd(a, b)

    c = 1
    for i in range(n):
        slopes = defaultdict(int)
        same_points = 0
        x1, y1 = points[i]

        for j in range(i+1, n):
            x2, y2 = points[j]
            dx = x2 - x1
            dy = y2 - y1

            if dx == 0 and dy == 0:
                same_points += 1
            else:
                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = 1
                slopes[(dx, dy)] += 1

        local_max = 0 if not slopes else max(slopes.values())
        local_max += (1 + same_points)
        c = max(c, local_max)

    if c < 3:
        print(n // 3)
        return

    m = n - c

    max_triangles = 0
    limit = min(c // 2, m)
    for x in range(limit + 1):
        candidate = x + (m - x) // 3
        if candidate > max_triangles:
            max_triangles = candidate

    return max_triangles


n = int(input().strip())
points = [tuple(map(int, input().split())) for _ in range(n)]
print(solve(n, points))