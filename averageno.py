#Calculate the Average of Numbers in a Given List
n = int(input("Enter the number of elements to be inserted: "))
a = []
for i in range(0, n):
    element = int(input("Enter element: "))
    a.append(element)
    avg = sum(a) / n
    print("Average of elements in the list", round(avg, 2))

