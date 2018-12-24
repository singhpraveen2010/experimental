s = "aaabceeffff"
c=""
i=0
l=len(s)
while i<l:
    if i ==l-1:
    	if s[i-1]!= s[i-2]!=s[i]:
        	c=c+s[i]
    	break
    elif s[i+1]==s[i]==s[i+2]:
        i=i+3
    else:
        c=c+s[i]
        i=i+1

print c