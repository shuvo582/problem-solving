# X number of children
# Y number of chocolates 
X,Y = map(int,input().split())
def fair():
    return X- (Y % X)

print(fair())