# Take empty array
my_list = []

#Add elements
my_list= ['A','B','C']
print (my_list[1])

#Append values into array
my_list.append('D')
print (len(my_list))
print (my_list[3])

#Extend elemets
my_list.extend(['E','F','G','Last'])
print(my_list)

#insertion
my_list.insert(0,'First')
print(my_list)
#list contains
#['First', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'Last']
#pop
print (my_list.pop(0))
print (my_list.pop())
print (my_list[-1])
print (my_list[-2])