import sys
# from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    count=0
    n = int(input())
    # n=12
    if n == 1 :
        count= 0
    elif n == 2 or n==4 or n==5:
        count = -1
    elif n== 3:
        count = 2    
    else:
        while n >= 2 :
            if n == 1:
                count = count + 1
                n = -1
            elif n  == 2 or n == 4 or n ==5:
                count = -1 
                n = -1
            elif n % 6== 0 and n>= 6:
                n = n// 6
                count= count + 1
            elif n % 3 == 0:
                n = n * 2
                count = count +1
            else:
                
                count = -1
                n = -1
            
            
        
    
    write(str(count)+'\n')
    # print(count)
    
   
t = int(input())
for _ in range(t):
    solve()