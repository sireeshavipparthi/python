# for loop
numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

numbers = ["arun","vamsi","raju"]
for item in numbers:
    print("This person name is" ,item)

# while loop
run = True
current = 1

while run:
    if current == 100:
        run = False
    else:
        print(current)
        current += 1