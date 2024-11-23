def near_lucky():
    n=input()
    count=0
    for i in n:
        if i == "7" or i =="4" :
            count = count + 1 
    if count == 7 or count == 4 :
        return "YES"
    else:
        return "NO"

near_lucky() 