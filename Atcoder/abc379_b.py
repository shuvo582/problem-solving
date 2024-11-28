'''
N K 
S
N- total teeth
K- consecutive healthy teeth needed to eat 1 apple
S - teeth string 
O means Goood
X means bad teeth
'''

N , K =map(int,input().split())
S=input()
count= 0 
T=0
for i in range(0,len(S)-1,1):
    if S[i]==S[i+1] and S[i]=="O":
        count= count+1
        if S[i+1]== S[-1] and count >= K-1:
            T = T + int((count+1) /K )
                        
    else:
        if count >= K-1 :
            T = T + int((count+1) /K )
        count=0
print(T)
