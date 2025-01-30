def solve(n, k, a):
    MOD = 998244353

    S = [0] * (k + 1)
    S[0] = n % MOD

    pow_a = [1] * n
    for m in range(1, k + 1):
        total = 0
        for i in range(n):
            pow_a[i] = (pow_a[i] * a[i]) % MOD
            total = (total + pow_a[i]) % MOD
        S[m] = total

    max_p = k
    fact = [1] * (max_p + 1)
    inv_fact = [1] * (max_p + 1)
    for i in range(1, max_p + 1):
        fact[i] = fact[i-1] * i % MOD

    inv_fact[max_p] = pow(fact[max_p], MOD-2, MOD)
    for i in reversed(range(max_p)):
        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    def comb(p, m):
        if m < 0 or m > p:
            return 0
        return fact[p] * inv_fact[m] % MOD * inv_fact[p-m] % MOD

    pow2 = [1] * (k + 1)
    for i in range(1, k + 1):
        pow2[i] = (pow2[i-1] * 2) % MOD
    inv2 = (MOD + 1) // 2  

    results = []
    for p in range(1, k + 1):
        sum_binom = 0
        for m in range(p + 1):
            val = comb(p, m) * S[m] % MOD
            val = val * S[p - m] % MOD
            sum_binom = (sum_binom + val) % MOD

        sum_single = (pow2[p] * S[p]) % MOD
        total = (sum_binom - sum_single) % MOD
        ans = (total * inv2) % MOD

        results.append(ans)

    return results


n, k = map(int, input().split())
a = list(map(int, input().split()))
for i in solve(n, k, a):
    print(i)
