
'''

Let m be an integer. Using only the operations // and % make
another integer n with a reversed sequence of digits with respect
to m.
'''

m = 123
n = 0

while m > 0:
    a = m % 10
    n = n * 10 + a
    m = m // 10

print(n)
