import sys 
input=sys.stdin.readline
print=sys.stdout.write
t=int(input())

def sol(t):
    a,b=map(int,input().split())
    arr=list(map(int,input().split()))
    print(str(t)+ '\n')
    print(str(a)+' '+str(b))
    
sol(t)