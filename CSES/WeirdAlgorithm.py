n=int(input())

def weird(n):
    outp=str(n)
    while n != 1 :
        if n % 2 == 0 :
            n = int(n / 2)
            outp= outp+ " " + str(n)
        else:
            n = 3 * n + 1
            outp=outp+" "+ str(n)
    return outp 
print(weird(n))