# # exception 
# try:   # the statements that might have exceptions in them
#    a = int(input("Enter number:"))
#    b = 10 - a
#    print(b)
# except ValueError:  # if the statement in try has error then the statement inside the except is executed.
#    #multiple except can be used.
#    print("Value Error...")
# except TypeError:
#    print("Type Error...")
# except NameError:
#    print("Name Error...")
# except:
#    print("hello")
# # else:  # runs only when the statements inside the try block is executed properly
# #    print("End")
# finally:    # runs with or without any exception
#    print("Finally keyword.")
   
# try:
#    p = 5
#    q = "a"
#    if p < q:
#       print("q is less.")
# except:
#    print("Terminated.")
# else:
#    print("Else statement ecxecuted.")
# finally:
#    print("Finally statement executed.")

# mind * 10 # output: mindmindmind
try:
   a = ["A","B","C"]
   n = int(input("Enter a number")) #0
   for i in a:
      print(a[n]) # a[0]
      n += 1
except IndexError:
   print("Calculation terminated.because of index error")
except:
   print("Invalid")