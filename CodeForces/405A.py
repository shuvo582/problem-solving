import sys
from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    print(*arr)
    
solve()