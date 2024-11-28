def soln():
    N=int(input())
    S=input()
    arr=S.split("/")
    max=0
    for i in range(0,len(arr)-1):
        for j in range(len(arr)-1,1,-1):
            if i[j]==i[j-1]:
                count=count+1
            else:
                count
            
        