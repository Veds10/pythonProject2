# faulty calculator

no_1=int(input("enter 1st no"))
no_2=int(input("enter 2nd no"))

con=input("what operation do you want to perform + - * /")

if con == "+":
    print(no_1+no_2)

elif con == "-":
    print(no_1-no_2)

elif con == "*":
    print(no_1*no_2)

elif con == "/":
    print(no_1/no_2)

else:
    print("invalid")





