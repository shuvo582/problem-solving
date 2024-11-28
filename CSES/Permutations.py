# N=int(input())
# S1="" 
# S2=""
# if N == 1:
#     print(1)
# elif N <= 3 :
#     print("NO SOLUTION")
# else:
#     for i in range(1,N+1,2):
#         if i+1 % 2 == 0 and (i+1)<=N:
#             S1=  S1 +" "+ str(i+1)
#         else:
#             S2=  S2 +" "+ str(i)
# print(S1[1:],S2[1:])

N=int(input())
S1="" 
S2=""
if N == 1:
    print(1)
elif N <= 3 :
    print("NO SOLUTION")
else:
    for i in range(1,N+1,2):
        if N % 2 == 0 :
            if (i+1) % 2 == 0 :
                S1=  S1 +" "+ str(i+1)
            else:
                S2=  S2 +" "+ str(i)
        else:
            if (i+1) % 2 == 0 and (i+1)<N:
                S1=  S1 +" "+ str(i+1)
            else:
                S2=  S2 +" "+ str(i)
            
print(S1[1:],S2[1:])
        
        