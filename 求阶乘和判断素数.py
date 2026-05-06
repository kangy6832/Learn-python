import functools
import operator

fac = lambda n: functools.reduce(operator.mul, range(2, n + 1), 1)

is_prime = lambda m : all(map(lambda f : m % f, range(2, int(m ** 0.5) + 1)))

print(fac(6))
print(is_prime(37))