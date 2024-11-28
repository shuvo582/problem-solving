x123=map(int,input().split())
x123=sorted(x123)
# print(x123)
distance= abs(x123[0] - x123[1]) + abs ( x123[1] - x123[2])

print(distance)
