N=int(input())
numbers=list(map(int,input().split()))
def nums():
    for i in range(0,len(numbers)-1):
        if numbers[i] <= numbers[i+1] :
            continue
        else:
            return "No"
            
            
    return "Yes"

print(nums())