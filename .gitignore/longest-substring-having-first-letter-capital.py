s=input().strip()
p=""
i=0
for i in range(len(s)):
    k=""
    if s[i].isupper():
        k+=s[i]
        for j in range(i+1,len(s)):
            if s[j].isupper():
                break
            else:
                k+=s[j]
        if len(p)<len(k):
            p=k
if len(p)<=1:
    print(-1)
else:print(p)
