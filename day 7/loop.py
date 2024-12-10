# while loop - multi lined statement, conditional statement , block of code is executed multiple times until the requirement is met
# check the condition and execute the block if the condition is True
# if the condition is True and doesnt change then it will run indefinitely
# we have to write logics that will change the condition to False at some point

# Requirement: print "A is greater than B" 5 times
a = 5
b = 0

while a > b:
   print("A is greater than B")
   b += 1  #(b = 4 + 1 = 5)
   continue
   # print("After the continue")

print("End of while")

# break - terminate the loop and execute the next line of code
# continue - goes back to the while condition and check the condition again