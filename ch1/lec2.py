result = 0
operator = ""
number1 = 0
number2 = 0

while(True):
    if len(operator)==0:
        number1 = int(input("Enter first number"))
        result = number1
    operator = input("Enter the operator from (+,-,&,/) and = to exit")
    if(operator == "="):
        print("Final result", result)
        break
    number2 = int(input("Enter the next number"))

    