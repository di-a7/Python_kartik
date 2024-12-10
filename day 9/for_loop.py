# iterables = sequencial or group datatype
# iterators = variable that is used to perform iteration
# iteration = repeating the block of code, loop that runs within the iterables from first to last

# syntax: for iterators in iterables

# a = ["cat","dog","cow",1,2,3]
# i =  "dog"
# a = "Hello World"

# for i in a:
#    if i == 1:
#       break
#    print(i)

# for i in a:
#    if i == 1:
#       continue
#    print(i)
   

# nested
a = ["a",'b','c']
b = [8,9,]

# i=b
for i in a:
   print(f"parent for :{i}") # c
   # j =8
   for j in b:
      print(f"Child for : {j}")

#Task:
# create a list or tuple of integers and store it in a variable
# start a for loop
# print the total number of the integers
