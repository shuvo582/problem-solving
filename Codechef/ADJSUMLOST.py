# https://www.codechef.com/problems/ADJSUMLOST
import sys 
input=sys.stdin.readline
write=sys.stdout.write

def solve():
    n=int(input())
    Bi=list(map(int,input().split()))
    Bi.sort()
    Ai=[1]*(n)
    if  Bi[0]<2 and len(Bi)==1 :
        print(-1)
        return
    for i in range(0,len(Bi)):
        for k in range(1,Bi[i]):
            Ai[0]=k
            for j in range(len(Bi)):
                Ai[i+1]= Bi[i]-Ai[i]
                if Ai[j+1]<=0 :
                    break
            else :
                print(*Ai)
                return
            
    print(-1)
        
        
    
    
t = int(input())
for _ in range(t):
    solve()