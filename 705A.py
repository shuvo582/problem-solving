n=int(input())
odd="I hate it"
even="I love it"
odd_steps="I hate that "
even_steps="I love that "
if n ==1:
    print(odd)
elif n % 2 == 0 :
    # print(n)
    print((int(n/2)-1)*(odd_steps+even_steps)+odd_steps+even)
else:
    print(int(n//2)*(odd_steps+even_steps)+odd)