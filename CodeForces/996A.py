import sys
from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    arr=[100,20,10,5,1]
    n=0
    N = int(input())
    for i in arr:
        if N >= i:
            n = N // i  + n
            N = N % i
    print(n)
        

solve()