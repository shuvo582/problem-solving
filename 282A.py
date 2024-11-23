with open("input.txt") as f:
    n=int(f.readline().strip())
    count=0
    for i in range(n):
        m=f.readline().strip()
        if m =="++X" or m == "X++":
            count += 1
        elif m == "X--" or "--X" :
            count -= 1
            
    print(count)
            
       