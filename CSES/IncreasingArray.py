def soln():
    n=int(input())
    arr_x=list(map(int,input().split()))
    count=0
    for i in range(0,len(arr_x)-1):
        if arr_x[i+1]<arr_x[i]:
            count=abs(arr_x[i]-arr_x[i+1]) + count
            arr_x[i+1]=arr_x[i+1] + abs(arr_x[i]-arr_x[i+1])
            
    print(count) 
    return 
soln()


        