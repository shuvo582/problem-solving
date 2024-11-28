import sys
from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    m,n=map(int,input().split())
    arr = list(map(int, input().split()))
    arr.sort()
    s_arr=0
    # 
    for i in arr:
        if i < 0 and n>0:
            s_arr = s_arr + i
            n = n-1
        else:
            write(str(-s_arr)+'\n')
            return 
        
    write(str(-s_arr)+'\n')
    return 
    

solve()