'''
n: number of rooms 
q: capacity 
p: currently filled 

output number of rooms available for them
'''

with open("input.txt") as f:
    n = int(f.readline().strip())
    av=0
    for i in range(n):
        p,q=map(int,f.readline().split())
        if abs(q-p) >= 2 :
            av += 1 
    print(av)
        