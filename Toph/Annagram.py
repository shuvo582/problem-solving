A= input()
B = input()
count=0
for i in B:
    if i in A:
        count=count+1
if count == len(B):
    print("Yes")
else:
    print("No")