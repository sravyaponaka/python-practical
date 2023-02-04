s=input("enter the string")
a="a,e,i,o,u"
for i in s:
    if(i not in a):
        print(i,end="")
