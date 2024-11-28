def a():
    N =int(input())
    count1=0
    count2=0
    count3=0
    count4_9= 0
    for i in str(N):
        # print(i)
        if i == "1":
            count1= count1 +1 
        elif i == "2":
            count2= count2 + 1 
        elif i == "3":
            count3= count3 + 1

    if count3 == 3 and count1 == 1 and count2== 2 :
        print('Yes')
    else:
        print("No")
    # print(count1,count2,count3,count4_9)

a()