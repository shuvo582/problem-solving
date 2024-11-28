'''
Example
Input: n (string)

ATTCGGGA

Output:

3
'''
def soln(n):
    # n=input()
    k=0
    max=0
    for i in range(0,len(n)-1):
        if n[i]==n[i+1]:
            k=k +1 
            if k > max :
                max = k
        else:
            k=0
    print(max+1)
    return
    
n=input()
soln(n)
            