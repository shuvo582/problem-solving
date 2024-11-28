import sys
# from typing import List
input = sys.stdin.readline
write = sys.stdout.write


def solve() -> None:
    k=1
    cn=0
    n = int(input())
    if n <= 4:
        write(str(0)+'\n')
       
    else:
        while (5 ** k) <= n:
            cn=int(n/ ( 5 ** k)) + cn
            k = k+1
        write(str(cn) + '\n')
    
   
t = int(input())
for _ in range(t):
    solve()

# solve()