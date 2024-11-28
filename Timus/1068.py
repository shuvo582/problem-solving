n=int(input())
if n == -1 :
    print(0)
elif n< 0 :
    sumL= -int(n*(n-1)/2)+1
    print(sumL)
elif n ==0 :
    print(1)
else:
    sumR= int(n*(n+1)/2)
    print(sumR)