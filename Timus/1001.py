import sys 
import math
input_data=sys.stdin.read()
input_numbers=list(map(int,input_data.split()))
for i in range(len(input_numbers)-1,-1,-1):
    print(format(math.sqrt(input_numbers[i]), ".4f"))
    