# https://www.spoj.com/problems/PRIME1/
import sys

def prime_check(n):
    if n == 1 :
        return False
    elif n == 2:
        return True 
    elif n % 2 == 0 :
        return False
    
    for i in range(3, int(n**0.5)+1,2):
        if n % i ==0:
            return False
    return True
input=sys.stdin.readline
t=int(input())
def prime_list(t):
    for i in range(t):
        L,R= map(int,input().split())
        for i in range(L,R+1,1):
            if i == 2:
                sys.stdout.write(str(i)+'\n')
            elif prime_check(i) and i % 2 != 0 :
                sys.stdout.write(str(i)+'\n')
        print()

prime_list(t)