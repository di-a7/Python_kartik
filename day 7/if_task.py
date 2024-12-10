# Exam Mark analyser

# Requirements:
# user input for user marks(100-0)
mark = int(input("Enter your mark: "))
# if user mark is greater than 90 and less than 100 print "Excelent" 
if mark >= 90 and mark < 100:
   print("Excellent")

# if user mark is greater than 80 and less than 90 print "Very Good"
elif mark >= 80 and mark < 90:
   print("Very Good")
   
# if user mark is greater than 70 and less than 80 print "Good"
elif mark >= 70 and mark < 80 :
   print("Good")
   
# if user mark is greater than 60 and less than 70 print "Better"
elif mark >= 60 and mark < 70:
   print("Better")
   
# if user mark is greater than 50 and less than 60 print "Fair"
elif mark >= 50 and mark < 60:
   print("Fair")
   
# if user merk is greater than 40 and less than 50 print "Passed"
elif mark >= 40 and mark < 50:
   print("Passed")
   
# if user mark is less than 40 print "Failed"
else:
   print("Failed")