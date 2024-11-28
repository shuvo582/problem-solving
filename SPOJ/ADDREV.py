import sys
# from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    # n = int(input())
    a,b=input().split()
    # arr = list(map(int, input().split()))
    a,b=a[::-1],b[::-1]
    s= int(a)+int(b)
    # s=int(str(a)[::-1])
    
    # If single output
    # write(str(s) + '\n')
    # print(a,b)
    # s= int(a)+int(b)
    s1= str(s)
    s1= s1[::-1]
    write(str(int(s1))+'\n')


t = int(input())
for _ in range(t):
    solve()