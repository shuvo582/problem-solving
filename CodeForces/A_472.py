
def prime_check(n):
    if n == 1 :
        return True
    elif n == 2:
        return True 
    elif n % 2 == 0 :
        return False
    
    for i in range(3, int(n**0.5)+1,2):
        if n % i ==0:
            return False
    return True


def A472(n1):
    j=1
    mid = int(n1/2)
    if n1 % 2 == 0 :
        if prime_check(mid)== False:
            print(int(n1/2),int(n1/2))
        else:
            while j <= int(n1/2):
                L1= mid -j 
                R1= mid + j 
                if prime_check(L1) == False and prime_check(R1)== False:
                    print(L1,R1)
                    return
                j=j+1
    else:
        while j <= int(n1/2):
            L1= mid -j +1 
            R1= mid + j 
            if prime_check(L1) == False and prime_check(R1)== False:
                ans = str(L1) + " " + str(R1)
                print(L1,R1)
                return
            j=j+1

n1=int(input())     
A472(n1)