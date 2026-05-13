print("        SIMPLE CALCULATOR     ")
a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print(" 1 for ADDITION \n 2 for SUBTRACTION \n 3 for PRODUCT \n 4 for DIVISION")
n=int(input("Enter your choice: "))
match n:
    case 1:
        print("Sum of the number",a,"and",b,"= ",a+b)
    case 2:
        print("Subtraction of the number",a,"and",b,"=",a-b)
    case 3:
        print("Product of the number",a,"and",b,"= ",a*b)
    case 4:
        if b==0:
            print("Not Possible")
        else:
            print("Division of the number",a,"and",b,"= ",a/b)
    case _:
        print("INVALID CHOICE")                            