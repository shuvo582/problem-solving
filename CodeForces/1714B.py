import sys
from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    n = int(input())
    arr = list(map(int, input().split()))
    set_arr=set()
    if n == len(set(arr)):
        write('0'+'\n')
        return
    else:
        for i in range(-1,-(n+1),-1):
            if arr[i]  in set_arr:

                write(str(n - len(set_arr)) + '\n')
                return
                
            else:
                set_arr.add(arr[i])

        
        if arr[i]  in set_arr:
                write(str(n - len(set_arr)) + '\n')
                return
                 
    
  
t = int(input())
for _ in range(t):
    solve()