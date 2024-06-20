stack=[]
s=input()
ok=1
n=len(s)
if s[0]==']' or s[0]=='}' or s[0]==')':
    print(False)
for i in range(n):
    if s[i]=='[':
        stack.append(']')
    elif s[i]=='(':
        stack.append(')')
    elif s[i]=='{':
        stack.append('}')
    elif s[i]==']' or s[i]=='}' or s[i]==')':
        if s[i]==stack[-1]:
            stack.pop()
        else:
            ok=0
            break
    else:
        print("Invalid Paranthesis")
        ok=-1
        break
if ok==1:
    print("Balanced")
elif ok==0:
    print("Not Balanced")
