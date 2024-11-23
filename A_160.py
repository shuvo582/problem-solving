def A160():
    n=int(input())
    arr=list(map(int,input().split()))
    arr.sort()
    sum_arr=sum(arr)
    Rsum=0
    Lsum= 0
    while n > 0 :
        Rsum = sum(arr[n-1:])
        Lsum = sum_arr - Rsum
        if Rsum > Lsum :
            return len(arr)-(n-1)
            
        n = n -1 
print(A160())