# def soln():
#     t= int(input()) # number of melodies 
#     for i in range(t):
#         n=int(input())
#         list_a= list(map(int,input().split()))
#         for i in range(len(list_a)-1):
#             if abs(list_a[i]-list_a[i+1]) != 7 and abs(list_a[i]-list_a[i+1]) != 5 :
#                 return "NO"
#         return "YES"
    
# soln()

def soln():
    t = int(input())
    sol_list=[1]*t
    for k in range(t):
        n=input()
        list_a= list(map(int,input().split()))
        for i in range(len(list_a)-1):
            if abs(list_a[i]-list_a[i+1]) ==7 or abs(list_a[i]-list_a[i+1]) == 5 :
                continue
            else:
                sol_list[k]=0
    # print(sol_list)
    for _ in sol_list:
        if _ == 1 :
            print("YES")
        elif _ == 0:
            print("NO")
soln()