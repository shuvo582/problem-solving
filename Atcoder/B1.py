def soln():
    S=input()
    N=len(S)
    set_1=set()
    if N % 2 == 0 :
        for i in range(0,int(N/2)):
            if S[2*i]==S[2*i + 1]:
                set_1.add(S[2*i])
            else:
                return "No"
        if len(set_1) == int(N/2) and N % 2 == 0:
            return "Yes"
        else:
            return "No"
    else:
        return 'No'     
    

    
print(soln())
                