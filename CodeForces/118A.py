S=input()
vs=['a','e','i','o','u']
for i in range(0,len(S)-1):
    ss=S[i].lower()
    if ss in vs:
        S= S[:i]+S[i+1:]
print(S)