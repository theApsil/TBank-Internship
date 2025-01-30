import math

def solve(n, x, y, z, a):
    def cost_divisible(value, divisor):
        return 0 if (value % divisor) == 0 else (divisor - (value % divisor))
    
    lcm_xy = x * y // math.gcd(x, y)
    lcm_xz = x * z // math.gcd(x, z)
    lcm_yz = y * z // math.gcd(y, z)
    lcm_xyz = lcm_xy * z // math.gcd(lcm_xy, z)

    matrix = [None] * n

    for i in range(n):
        cx = cost_divisible(a[i], x)
        cy = cost_divisible(a[i], y)
        cz = cost_divisible(a[i], z)
        cxy = cost_divisible(a[i], lcm_xy)
        cxz = cost_divisible(a[i], lcm_xz)
        cyz = cost_divisible(a[i], lcm_yz)
        cxyz = cost_divisible(a[i], lcm_xyz)
        
        matrix[i] = [
            0,   
            cx,      
            cy,        
            cxy,        
            cz,           
            cxz,         
            cyz,          
            cxyz          
        ]
    
    INF = 10 ** 20
    dp = [INF] * 8
    dp[0] = 0

    for i in range(n):
        new_dp = dp[:]
        for mask in range(8):
            if dp[mask] == INF:
                continue
            base_cost = dp[mask]
            for role in range(1, 8):
                new_mask = mask | role
                _cost = matrix[i][role]
                c_and = base_cost + _cost
                if c_and < new_dp[new_mask]:
                    new_dp[new_mask] = c_and
        dp = new_dp
    
    return dp[7]

n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, x, y, z, a))