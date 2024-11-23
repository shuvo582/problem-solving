def c2033():
    
    t=int(input())
    for _ in range(t):
        i=0
        j=0
        count=0
        n=int(input()) # number of numbers 
        a_n=list(map(int,input().split()))
        # a_n.sort(reverse=True)
        arr_1=[]
        while n >= 1 :
            arr_1.append(a_n[n-1])
            n=n-1
            
            
        n=len(arr_1)
        # print(arr_1)
        while i < n -1 :
            if arr_1[i]==arr_1[i+1]:
                count=count+1
            i = i + 1
            
        print(count)
        
c2033()