#Define The Addition Function 
def Add(a, b):
    return a+b
#Define The Subtraction Function
def Subtract(a,b):
    return a-b
#Define The Multiplication Function
def Multiply(a,b):
    return a*b
#Define The Division Function
def Divide(a,b):
    if b!=0:
        return a/b
    else:
        return "Cannot Divide By Zero"
#Display Operation Value
print("Select Operation" )
print("1. Add")
print("2. Subtract")
print("3. Multiplication")
print("4. Divide")

Choice = int(input("Enter Your Choice (1,2,3,4)")) #User Choice Input
num1 = float(input("Enter First Number")) #Input First Number
num2 = float(input("Enter Second Number")) #Input Second Number

#Add Two Numbers And Show The Output
if Choice == 1:
    print(f"The Sum Of Two Numbers is {Add(num1,num2)}")
#Subtract Two Numbers And Show The Output
elif Choice == 2:
    print(f"The Subtraction Of Two Numbers is {Subtract(num1,num2)}")
#Multiply Two Numbers And Show The Result
elif Choice == 3:
    print(f"The MUltiplication Of Two Numbers is {Multiply(num1,num2)}")
#Divide Two numbers And Show The Result
elif Choice == 4:
    print(f"The Division Of Two Numbers is {Divide(num1,num2)}")
#User Get Invalid Input
else:
    print("Invalid Input")
