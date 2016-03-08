from math import factorial
def nCr(n, r):
    return factorial(n)/(factorial(n-r)*factorial(r))

def cumulative_binomial_distribution(x, n, p):
    # Less than or equal
    s = 0
    for i in range(0, x+1):
        print(i)
        s += nCr(n, i) * (p**i) * (1-p)**(n-i)

    return s

print(1 - cumulative_binomial_distribution(6, 10, 0.2))
