n,m=map(int,input().split())
for _ in range(1,n+1):
    if _ % 4 == 1 :
        print("#"*m)
        # print(_)
    elif _ % 4 == 2:
        print("."*(m-1)+"#")
        # print(_)
    elif _ % 4 == 3 :
        print("#"*m)
        # print(_)
    elif _ % 4 == 0 :
        print("#"+"."*(m-1))