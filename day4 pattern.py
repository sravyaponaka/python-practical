n=int(input("rows="))
for i in range(0,n):
    print((n-i) , end=" ")
    k=0.1
    for j in range(0,i):
        print("{:.1f}".format(k),end=" ")
        k=k+0.1
    print("\r")
