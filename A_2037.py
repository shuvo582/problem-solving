t=int(input())
def twice(t):
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        arr.sort()
        i= 0 
        count= 0
        while i < n-1 :
            if arr[i]==arr[i+1]:
                count=count+1
                i=i+2
            else:
                i = i+1 
        print(count)
twice(t)
