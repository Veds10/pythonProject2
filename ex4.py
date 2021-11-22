# patterns
n=int(input("how many "))
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()

i=1
while(i<=n):
    print("*",end="")
    j=1
    while(j<=i):
        print("*",end="")
        j+=1
    i+=1
    print()

