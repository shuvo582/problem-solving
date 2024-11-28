import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1

def prime_check(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

for _ in range(t):
    L, R = map(int, data[index:index + 2])
    index += 2
    for i in range(L, R + 1):
        if prime_check(i):
            sys.stdout.write(str(i) + "\n")
