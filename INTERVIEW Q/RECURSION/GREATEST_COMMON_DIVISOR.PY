

def gcd(n, m):
    assert int(n) == n and int(m) == m, 'Both number must be positive integer !'
    if n < 0:
        n = -1*n
    if m < 0:
        m = -1*m
    if m == 0:
        return n
    else:
        return gcd(m, n % m)


print(gcd(-16, -8))
