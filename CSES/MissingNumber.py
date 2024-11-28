def miss():
    n=int(input())
    n_list=list(map(int,input().split()))
    missing= int(n*(n+1)/2) - sum(n_list)
    # print(missing)
    return missing

print(miss())