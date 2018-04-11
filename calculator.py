def Multiply(x,y):
    " This function multiplies two numbers"
    return x * y
def Divide(x,y):
    " This function divides two numbers"
    return x / y
def Add(x,y):
    " This function add two numbers"
    return x + y
def Subtract(x,y):
    " This function subtract two numbers"
    return x - y

#Take input from the user
print("Select Operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

if choice   == '1':
    print(num1, "+", num2, "=", Add(num1,num2))
elif choice == '2':
    print(num1, "-", num2, "=", Subtract(num1,num2))
elif choice == '3':
    print(num1, "*", num2, "=", Multiply(num1,num2))
elif choice == '4':
    print(num1, "/", num2, "=", Divide(num1,num2))
else:
    print("Invalid Input")




