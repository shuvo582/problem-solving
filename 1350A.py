def f(n):
    if n % 2 == 0 :
        return 2
    else:
        for i in range(3,int(n**0.5)+1,2):
            if n % i == 0 :
                return i 
        return n 
    
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

    
def A1350():
    t=int(input())
    for i in range(t):
        n,k = map(int,input().split())
        # for j in range(0,k):
        #     n= n + f(n)
        # print(n)
        if n % 2 == 0 :
            print(n+ k*2)
        elif prime_check(n):
            print( 2*n + 2*(k-1))
        else:
            print( n + f(n)+ 2*(k-1))
            
    
A1350()
    



                