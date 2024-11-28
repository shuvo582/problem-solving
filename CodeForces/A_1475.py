def odd(t):
    # t=int(input())
    for i in range(t):
        n=int(input())
        def temp(n):
            if n == 2:
                return "NO"
            elif n % 2 != 0 :
                return "YES"
            else:
                for j in range(n):
                    n= n / 2
                    if n % 2 != 0 :
                        return "YES"
                if n % 2 == 0 :
                    return "NO"
        print(temp(n))
                
t=int(input())
odd(t)