# n=int(input())
# count=0
# for i in range(n):
#     a,b,c=map(int,input().split())
#     if a+b+c >= 2 :
#         count=count+1
        
# print(count)

with open("input.txt") as f:
    n=int(f.readline().strip())
    count=0
    for i in range(n):
        a,b,c = map(int,f.readline().split())
        if a+b+c >= 2 :
            count += 1
    print(count)

