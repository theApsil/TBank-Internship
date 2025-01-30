def solve(n, m, a):
    a1, a2 = a[0], a[1]
    left, right = min(a1, a2), max(a1, a2)

    fix_costs = []
    good_days = 0

    for i in range(2, n):
        if left <= a[i] <= right:
            good_days += 1
        else:
            if a[i] < left:
                fix_costs.append(left - a[i])
            else:
                fix_costs.append(a[i] - right)

    if good_days >= m:
        return 0

    needed = m - good_days
    fix_costs.sort()

    answer = sum(fix_costs[:needed])
    return answer

n, m = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, m, a))