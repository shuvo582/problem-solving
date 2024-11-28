import sys
# from typing import List
input = sys.stdin.readline
write = sys.stdout.write

def solve() -> None:
    # n = int(input())
    a,b=map(int,input().split())
    # arr = list(map(int, input().split()))
    
    # If single output
    write(str() + '\n')
    
    # If multiple outputs on same line
    # write(' '.join(map(str, arr)) + '\n')
    
    # If multiple lines of output
    # output = []
    # for x in arr:
        # output.append(str(x * 2))
    # write('\n'.join(output) + '\n')

# For multiple test cases
t = int(input())
for _ in range(t):
    solve()