#Exchange the Values of Two Numbers Without Using a Temporary Variable
a = int(input("Enter a value:"))
b = int(input("Enter b value:"))

a = a + b
b = a - b
a = a - b
print (a)
print("a is:",a," b is:",b)

