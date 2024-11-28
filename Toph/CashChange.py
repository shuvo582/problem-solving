# https://toph.co/p/cash-change

import sys 
input=sys.stdin.readline
write=sys.stdout.write

def solve():
    N= int(input())
    arr=[]
    for i in range(1,N+1):
        if N >= 500 :
            n= N // 500 
            N = N - n * 500
            for j in range(n):
                arr.append(500)
        elif N >= 100:
            n= N // 100 
            N = N - n * 100
            for j in range(n):
                arr.append(100)
            
        elif N >= 50:
            n= N // 50 
            N = N - n * 50
            for j in range(n):
                arr.append(50)
            
        elif N >= 10:
            n= N // 10 
            N = N - n * 10
            for j in range(n):
                arr.append(10)
            
        elif N >= 5:
            n= N // 5
            N = N - n * 5
            for j in range(n):
                arr.append(5)
            
        else:
            n= N // 1 
            N = N - n * 1
            for j in range(n):
                arr.append(1)
            
            
            
    arr.sort()
    print(*arr)
    return

solve()
            
            
