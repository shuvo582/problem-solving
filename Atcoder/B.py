def soln():
    S=input()
    ans=''
    count=0
    for i in S:
        if i == "-":
            count=count+1
        elif ans=='' and count == 0 :
            continue
        else:
            ans = ans + " "+ str(count)
            count = 0
    return ans[1:]

print(soln()) 
            
        