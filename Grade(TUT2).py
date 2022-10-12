
# Question 5
grade = 0
while True:
    try:
       grade = int(input("Enter students Marks:"))
       print("test 1 passed".upper())
    except ValueError:
        print("Entered marks are invalid (Only Numbers should be inputted)")
        print("Test 2 passed".upper())
        continue
    else:
        print("test 3 passed".upper())
        break
if grade < 0 or grade > 100:
        print("out of range".upper())
        print("test 4 passed".upper())
elif grade >= 80:
        print("Student got an A")
        print("test 2 passed".upper())
elif grade > 70 and grade < 80:
        print("Student got a B")
elif grade > 60 and grade < 70:
        print("student got a C")
elif grade >= 50 and grade < 60:
        print("Student got a D")
else:
        print("Student got a F")



