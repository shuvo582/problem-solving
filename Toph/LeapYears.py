# https://toph.co/p/leap-years 

Y = int(input())
if Y % 4 == 0 :
    if Y % 400 == 0 :
        print("No")
    #elif Y % 100 == 0 :
        #print("No")
    else:
        print("Yes")
else:
    print("No")