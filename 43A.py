n = int(input())
a_goal, b_goal = 0, 0
for i in range(n): 
    goal = input() 
    if i == 0:  
        a_team = goal
        a_goal = a_goal + 1
    if goal == a_team: 
        a_goal = a_goal + 1
    else:
        b_team = goal
        b_goal = b_goal + 1

if a_goal > b_goal:
    print(a_team)
else:
    print(b_team)
