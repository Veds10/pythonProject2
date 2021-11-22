# guess the number
n=34
i=1

while i<=5:
    guess = int(input("guess the no"))
    if guess>n:
        print("greater no")
    elif guess<n:
        print("smaller no")
    elif guess==n:
        print("boom you are correct")
        break
    else:
        print("invalid")

    print("guesse left",5-i)
    i=i+1

