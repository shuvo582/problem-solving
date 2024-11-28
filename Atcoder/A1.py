def a1112():
    N=int(input())
    S=input()
    one="1"
    two="2"
    if N % 2 != 0 :
        if S[int((N+1)/2)-1]=="/":
            # print(S[int((N+1)/2):])
            if S[:int(N/2)]==one*int(N/2) and S[int((N+1)/2):]==two*int(N/2):
                # print("YES")
                return "Yes"
    # print()
    return "No"

print(a1112())