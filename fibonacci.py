n = int(input("Enter number of terms:"))
print("Fibonacci sequence:")

def fib(n):
    if n <= 1 :
        return n
    else:
        return(fib(n-1) + fib(n-2))


for i in range(n):
     print (fib(i))