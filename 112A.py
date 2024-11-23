word1=input()
word2=input()

word1_sorted=''.join(sorted(word1.upper()))
word2_sorted=''.join(sorted(word2.upper()))


if word1_sorted == word2_sorted :
    print(0)
elif word1_sorted<word2_sorted:
    print(-1)
else:
    print(1)
