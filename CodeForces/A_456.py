n=int(input())
# global dummy
# dummy=[]
def soln(n):
    dummy=[]
    for i in range(n):
        a,b=map(int,input().split())
        dummy.append([a,b])
    
    dummy= sorted(dummy, key= lambda x:x[0])
    for j in range(0,len(dummy)-1):
        # j =[1,2]
        # print(dummy[j])
        if dummy[j][0] < dummy[j+1][0]:
            if dummy[j][1] > dummy[j+1][1]:
                return "Happy Alex"
        if dummy[j][0] > dummy[j+1][0]:
            if dummy[j][1] < dummy[j+1][1]:
                return "Happy Alex"
            
            
    return "Poor Alex" 

print(soln(n))
        
            
        