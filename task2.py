import bisect

def solve(budgets):
    powers = [1 << i for i in range(60)]
    
    three_sums = []
    for i in range(60):
        for j in range(i+1, 60):
            for k in range(j+1, 60):
                s = powers[i] + powers[j] + powers[k]
                if s <= 10**18:
                    three_sums.append(s)

    three_sums.sort()

    results = []
    for budget in budgets:
        idx = bisect.bisect_right(three_sums, budget)
        if idx == 0:
            results.append(-1)
        else:
            results.append(three_sums[idx-1])
    
    return results


n = int(input())
budgets = [int(input()) for i in range(n)]

answers = solve(budgets)
print("\n".join(map(str, answers)))
