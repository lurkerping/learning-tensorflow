#!/usr/bin/python3
a, b = 0, 1
while b < 1000:
    print(b, end=' ')
    a, b = b, a + b
print()

# range
print(range(10))
a, b = 0, 1
for i in range(10):
    print(b, end=' ')
    a, b = b, a + b
print()
