'''
input is position i recieved gift from serials p_i

output whom given gifts by serial 1 2 3 4  

roll 1 2 3 4 kake gift diche serially ta show korte hobe 

'''

# with open("input.txt") as f:
#     n = int(f.readline().strip())
#     kake_diche=[]
#     for i in range(n):
#         gifts_by_rolls=list(map(int,f.readline().split()))
#         keys=sorted(gifts_by_rolls) 
#         gift_recort=dict(zip(keys,gifts_by_rolls)) # dict{kake_diche:k_diche}
#         # roll 1-n kake gift diche ta ber korte hobe 
#         for i in keys:
            
            
with open("input.txt") as f:
    n = int(f.readline().strip())
    kake_diche=[]
    for i in range(n):
        gifts_by_rolls=list(map(int,f.readline().split()))
        temp=gifts_by_rolls
        whom_given=[] # given by roll order 
        for i in gifts_by_rolls:
            temp[i]=temp[temp.index(i)]
        
    print(temp)