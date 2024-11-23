with open("input.txt") as f:
    M,N=map(int,f.readline().split())
    max_dom = (M*N) // 2 
    print(max_dom)