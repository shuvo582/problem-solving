import sys
# from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    n = int(input())
    cn_2=0
    cn_3=0
    while n % 2 == 0 :
        n //= 2
        cn_2 +=1
    
    while n % 3 == 0 :
        n //= 3 
        cn_3 += 1
    if n != 1 :
        write(str(-1)+'\n')
        return
    
    if cn_2 > cn_3 :
        write(str(-1)+'\n')
        return
    
    
        
    
    
    write(str(cn_3+(cn_3-cn_2)) + '\n')
    
    
    
t = int(input())
for _ in range(t):
    solve()