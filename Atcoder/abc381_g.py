# https://atcoder.jp/contests/abc381/tasks/abc381_g
import sys
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    N ,x ,y=map(int,input().split())
    arr=[0]*N
    arr[0]=x
    arr[1]=y
    for i in range(2,len(arr)):
        arr[i]=arr[i-1]+arr[[i-2]]
        
    write(str() + '\n')
    
    

t = int(input())
for _ in range(t):
    solve()