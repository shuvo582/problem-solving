# n , k = map(int,input().split())
'''
If n is not div by 10 then subtract 1 else divide by 10 
do this task k times
'''

with open("input.txt") as f:
    n,k = map(int,(f.readline().split()))
    for i in range(k):
        if n % 10 != 0 :
            n=n-1 
        else:
            n = int(n / 10) 
    print(n)
    