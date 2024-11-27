import sys
# from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    S=input()
    S1=S[0].capitalize()
    
    S= S1 + S[1:]
    
    write(str(S))
    
solve()