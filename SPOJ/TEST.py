# https://www.spoj.com/problems/TEST/

def fn():
    n=0
    while n != 42:
        n=int(input())
        if n != 42:
            print(n)
        else:
            return
        
fn()
        