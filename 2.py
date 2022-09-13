N = int(input())

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

ans = 0

for i in range(1,N+1):
    if i % 2 == 0:
        continue

    dividors = make_divisors(i)
    if len(dividors) == 8:
       ans += 1

print(ans)

