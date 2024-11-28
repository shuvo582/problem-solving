def a_n(n,x,y):
    
    
    a_n(1)=x
    a_n(2)=y
    for j in range(3,n+1):
        a_n(j)=a_n(j-1)+a_n(j-2)
n=5
x=1
y=1

print()