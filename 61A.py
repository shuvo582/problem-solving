A=input()
B=input()
result=""
for i in range(len(A)):
    if A[i]==B[i] :
        result += "0"
        # print(A[i])
    else:
        result += "1"

print(result)