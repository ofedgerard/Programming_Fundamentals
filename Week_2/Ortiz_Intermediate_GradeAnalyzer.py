'''
Author: Gerard Ortiz
Date: 9/6/2026
Tier Level: Intermediate

Description:
This program collects name and grade information for 2 students exactly.
A grade report and comparison report is generated using 
input(), print(), conditional logic (if/elif/else), lists, tuples, and several string functions
'''
#Collects student first and last names. Cleans the name and creates a formated full name"
def add_name():
    #print("Student Grade Analyzer")
    studentLName = input("Student Last Name: ").strip().title()
    studentFName = input("Student First Name: ").strip().title()
    studentFull = studentFName+" "+studentLName[0] +"."
    print(studentFull+" is added","\n")
    return studentFull

#collects student score and returns a list of the sudent's scores
def add_score():
    student_scores = []
    print("Enter Test Scores e.g. 88, 92, 75")
    new_grade1 = int(input("Enter Grade No. 1: " ))
    student_scores.append(new_grade1)
    new_grade2 = int(input("Enter Grade No. 2: " ))
    student_scores.append(new_grade2)
    new_grade3 = int(input("Enter Grade No. 3: " ))
    student_scores.append(new_grade3)
    new_grade4 = int(input("Enter Grade No. 4: " ))
    student_scores.append(new_grade4)
    new_grade5 = int(input("Enter Grade No. 5: " ))
    student_scores.append(new_grade5)
    print()
    return(student_scores)

#takes in the the grades collected from add_score() and assigns the average a letter grade from the lettergrades tuple
def letter_grade (student_score):
    letterGrades = ("A","B", "C", "D", "F")
    avg_grade = sum(student_score)/len(student_score)
    highest_grade = max(student_score)
    lowest_grade = min(student_score)
    if avg_grade >= 90:
        return letterGrades[0], avg_grade, highest_grade, lowest_grade
    elif avg_grade >= 80:
        return letterGrades[1], avg_grade, highest_grade, lowest_grade
    elif avg_grade >= 70:
        return letterGrades[2], avg_grade, highest_grade, lowest_grade
    elif avg_grade >= 60:
        return letterGrades[3], avg_grade, highest_grade, lowest_grade
    else:
        return letterGrades[4], avg_grade, highest_grade, lowest_grade
    
#creates the student grade report with the letter grade
def createReport(student_score,studentName, letter_grade, avg_grade, max_grade, min_grade):
    print("="*5+" Grade Report "+"="*5)
    print("Student: "+studentName)
    print("Score: ", end=" ")
    print(student_score)
    print("Highest Score: ", max_grade)
    print("Lowest Score: ", min_grade)
    print("Average: ", end=" ")
    print(avg_grade)
    if letter_grade == "A":
        print("Grade: A")
        print("Remarks: "+ "Outstanding!")
    elif letter_grade == "B":
        print("Grade: B")
        print("Remarks: "+ "Wonderfull Job!")
    elif letter_grade == "C":
        print("Grade: C")
        print("Remarks: "+ "Great Effort!")
    elif letter_grade == "D":
        print("Grade: D")
        print("Remarks: "+ "Room For Improvement!")
    else:
        print("Grade: F")
        print("Remarks: "+ "Review Foundations")
    print("="*24)
    print()

#creates the comparison feature with both students max, avg, min, and letter grades. 
#displays which student has the higher scores or tie
def compare(student_name1, student_letter1, avg_grade1, max_grade1, low_grade1, student_name2, student_letter2, avg_grade2, max_grade2, low_grade2):
    highest_grade1 = max_grade1
    lowest_grade1 = low_grade1
    highest_grade2 = max_grade2
    lowest_grade2 = low_grade2
    letter_grade1 = student_letter1
    letter_grade2 = student_letter2
    print("="*8+" Comparison Report "+"="*8)
    print(" "*16 + student_name1 + " "*9 +student_name2)    
    print("Average"+" "*9+ str(avg_grade1)+" "*14+str(avg_grade2))
    print("Highest Score"+" "*3+str(highest_grade1)+" "*16+str(highest_grade2))
    print("Lowest Score"+" "*4+str(lowest_grade1)+" "*16+str(lowest_grade2))
    print("Letter Grade"+" "*4+ letter_grade1+" "*17+ letter_grade2+"\n")
    if avg_grade1 > avg_grade2:
        print(student_name1+" Outperformed "+student_name2+" by "+ str(avg_grade1-avg_grade2) +" points")
        print("="*37)
    elif avg_grade1 < avg_grade2:
        print("Overall: "+student_name2+" Outperformed "+student_name1+" by "+ str(avg_grade2-avg_grade1) + " points")
        print("="*37)
    else:
        print("Overall: "+student_name2+" and "+student_name1+" have the same average score at "+ str(avg_grade1) + " points")
        print("="*37)
'''
Compparison report sample dispaly
======== Comparison Report ========
                Gerard O.         Jay Ann O.
Average         10.0              10
Highest Score   10                10
Lowest Score    10                10
Letter Grade    A                 A

Remarks: 
===================================
========== End of Report ==========

'''


print("Student Grade Aanalyzer\n", "="*24)
print("Enter Student 1")
student_name1 = add_name() #collect student 1 name
student_grades1 = add_score() #collect student 1 grades
student1_letter_grade, avg_grade1, max_grade1, low_grade1 = letter_grade(student_grades1) #create the grade spread of student 1

print("Enter Student 2")
student_name2 = add_name() #collect student 2 name
student_grades2 = add_score() #collect student 2 grades
student2_letter_grade, avg_grade2, max_grade2, low_grade2 = letter_grade(student_grades2) #create the grade spread of student 2

#creates the report for each student
print(("*" + "\n") * 5)
createReport(student_grades1,student_name1,student1_letter_grade, avg_grade1, max_grade1, low_grade1)
createReport(student_grades2,student_name2,student2_letter_grade, avg_grade2, max_grade2, low_grade2)
print(("*" + "\n") * 5)

#create the comparison report for both students
compare(student_name1,student1_letter_grade,avg_grade1, max_grade1, low_grade1, student_name2,student2_letter_grade, avg_grade2, max_grade2, low_grade2)
print("="*10, "End of Report ","="*10)