'''
Basically he had some shoes 
suppose he has 4 shoe;s and they are 
1 4 7 7
where numbers are just color code 
so that means he has 3 pair of unique shoes 
here sets come into plays 
len(set) works'''

shoe_list=map(int,input().split())
shoe_set=set(shoe_list)
# print(shoe_set)
if len(shoe_set) >= 4 :
    print(0)
else:
    print(4-len(shoe_set))