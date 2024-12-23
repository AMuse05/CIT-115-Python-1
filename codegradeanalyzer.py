# Code Grade Analyzer

##sName = input("Name of person that we are calculating the grades for: ")
##
##fTest1 = float(input("Test 1: "))
##fTest2 = float(input("Test 2: "))
##fTest3 = float(input("Test 3: "))
##fTest4 = float(input("Test 4: "))
##
##drop_lowest = input("Do you want to drop the lowest grade? (Y or N): ")
##
##grades = [fTest1, fTest2, fTest3, fTest4]
##
##if drop_lowest == 'Y':
##    grades.remove(min(grades))
##    average_grade = sum(grades) / 3
##else: 
##    average_grade = sum(grades) / 4
##
##print(f"{sName}'s average grade is: {average_grade:.2f}")
##
##if average_grade >= 97.0:
##    letter_grade = "A+"
##elif 94.0 <= average_grade < 97.0:
##    letter_grade = "A"
##elif 90.0 <= average_grade < 94.0:
##    letter_grade = "A-"
##elif 87.0 <= average_grade < 90.0:
##    letter_grade = "B+"
##elif 83.0 <= average_grade < 87.0:
##    letter_grade = "B"
##elif 80.0 <= average_grade < 83.0:
##    letter_grade = "B-"
##elif 77.0 <= average_grade < 80.0:
##    letter_grade = "C+"
##elif 73.0 <= average_grade < 77.0:
##    letter_grade = "C"
##elif 70.0 <= average_grade < 73.0:
##    letter_grade = "C-"
##elif 67.0 <= average_grade < 70.0:
##    letter_grade = "D+"
##elif 63.0 <= average_grade < 67.0:
##    letter_grade = "D"
##elif 60.0 <= average_grade < 63.0:
##    letter_grade = "D-"
##else:
##    letter_grade = "F"
##
##print(f"{sName}'s letter grade is: {letter_grade}")


sName = input("Name of person that we are calculating the grades for: ")

fTest1 = float(input("Test 1: "))
fTest2 = float(input("Test 2: "))
fTest3 = float(input("Test 3: "))
fTest4 = float(input("Test 4: "))

drop_lowest = input("Do you want to drop the lowest grade? (Y or N): ")


grade1, grade2, grade3, grade4 = fTest1, fTest2, fTest3, fTest4


if drop_lowest == 'Y':
 
    if grade1 <= grade2 and grade1 <= grade3 and grade1 <= grade4:
        lowest = grade1
    elif grade2 <= grade1 and grade2 <= grade3 and grade2 <= grade4:
        lowest = grade2
    elif grade3 <= grade1 and grade3 <= grade2 and grade3 <= grade4:
        lowest = grade3
    else:
        lowest = grade4

    if lowest == grade1:
        average_grade = (grade2 + grade3 + grade4) / 3
    elif lowest == grade2:
        average_grade = (grade1 + grade3 + grade4) / 3
    elif lowest == grade3:
        average_grade = (grade1 + grade2 + grade4) / 3
    else:
        average_grade = (grade1 + grade2 + grade3) / 3
else:

    average_grade = (grade1 + grade2 + grade3 + grade4) / 4

print(f"{sName}'s average grade is: {average_grade:.2f}")

if average_grade >= 97.0:
    letter_grade = "A+"
elif 94.0 <= average_grade < 97.0:
    letter_grade = "A"
elif 90.0 <= average_grade < 94.0:
    letter_grade = "A-"
elif 87.0 <= average_grade < 90.0:
    letter_grade = "B+"
elif 83.0 <= average_grade < 87.0:
    letter_grade = "B"
elif 80.0 <= average_grade < 83.0:
    letter_grade = "B-"
elif 77.0 <= average_grade < 80.0:
    letter_grade = "C+"
elif 73.0 <= average_grade < 77.0:
    letter_grade = "C"
elif 70.0 <= average_grade < 73.0:
    letter_grade = "C-"
elif 67.0 <= average_grade < 70.0:
    letter_grade = "D+"
elif 63.0 <= average_grade < 67.0:
    letter_grade = "D"
elif 60.0 <= average_grade < 63.0:
    letter_grade = "D-"
else:
    letter_grade = "F"

print(f"{sName}'s letter grade is: {letter_grade}")
