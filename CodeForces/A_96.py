def A96():
    S=input()
    count=0
    arr=[]
    for i in range(0,len(S)-1):
        if S[i]==S[i+1]:
            # print(count,S[i])
            # print(i)
            count=count+1 
            
            if count == 6:
                print("YES")
                exit()
        else:
            arr.append(count)
            count=0
    print("NO")
    # print(arr)
    
A96()