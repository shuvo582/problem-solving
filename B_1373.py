import sys 
input=sys.stdin.readline
write=sys.stdout.write

def solve() -> None:
    cn=0
    i=0
    S=input()
    # for i in range(0,len(S)-2):
    while i <= len(S)-2:
        L= i 
        R= i+1
        # print(S[L],S[R])
        if S[L] != S[R]:
            # print(S[L],S[R])
            if len(S)>=2:
                S=S[:L]+S[R+1:]
                i=0
                cn=cn+1
    print(cn)
    if cn % 2 ==0:
        write('NET'+'\n')
    else:
        write('DA'+'\n')
            
# solve()               
t=int(input())
for _ in range(t):
    solve()

# 3
# 01
# 1111
# 0011

# DA
# NET
# NET
