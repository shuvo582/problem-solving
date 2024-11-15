H,M=map(int,input().split())

diff=abs(abs(12-H)+M/5)
diff_angle= 360*(diff/12)
mini_angle = (360/12)*(M/60)
total=diff_angle-mini_angle
print(f"{total: .7f}")