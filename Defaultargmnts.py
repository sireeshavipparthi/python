def print_something(name,age):
    print("My name is " + name + " and my age is " + str(age))
print_something("nick" ,27)

def print_something(name,age):
    print("My name is", name ,"and my age is ", age)
    print_something("hari" ,27)


def print_something(name = "someone ",age = "unknown"):
    print("My name is", name ,"and my age is ", age)
    print_something()


# keyword arguments
def print_something(name = "someone ",age = "unknown"):
    print("My name is", name ,"and my age is ", age)
    print_something(age = 27, name ="maks")