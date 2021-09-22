#CS 101 Lab
#Program 2
#Zach Opoka
# Email: zof6b@mail.umkc.edu

#Problem: Need to write a program to calculate grades for CS 101 Lab
print('**** Welcome to the Lab Grade Calculator! ****')
#Defining lab,exam, and attendance grades
name = str(input('Who are we calculating grades for?'))
lab_grade = float(input('Enter the Labs grade:'))
if lab_grade > 100:
    lab_grade = 100
    print('The lab value should have been 100 or less. It has been changed to 100.')
if lab_grade < 0:
    lab_grade = 0
    print('The lab value should have been zero or greater. It has been changed to zero.')
exam_grade = float(input('Enter the EXAMS grade:'))
if exam_grade > 100:
    exam_grade = 100
    print('The exam value should not be greater than 100. It has been changed to 100.')
if exam_grade < 0:
    exam_grade = 0
    print('The exam value should not be less than zero. It has been changed to zero.')
attendance_grade = float(input('Enter Attendance grade:'))
if attendance_grade > 100:
    attendance_grade = 100
    print('The attendance value should not be greater than 100. It has been changed to 100.')
if attendance_grade < 0:
    attendance_grade = 0
    print('The attendance value should not be less than zero. It has been changed to zero.')
#total Grade compute
ttl_grade = (0.7 * lab_grade) + (0.2 * exam_grade) + (0.1 * attendance_grade)
print('The weighted grade for {} is {:.1f}'.format(name, ttl_grade))
#percentage to letter grade
if ttl_grade >= 90:
    letter_grade = 'A'
    print('{} has a letter grade of {}'.format(name, letter_grade))
elif ttl_grade < 90:
    if ttl_grade >= 80:
        letter_grade = 'B'
        print('{} has a letter grade of {}'.format(name, letter_grade))
if ttl_grade < 90:
    if ttl_grade < 80:
        if ttl_grade >= 70:
            letter_grade = 'C'
            print('{} has a letter grade of {}'.format(name, letter_grade))
if ttl_grade < 90:
    if ttl_grade < 80:
        if ttl_grade < 70:
            if ttl_grade >= 60:
                letter_grade = 'D'
                print('{} has a letter grade of {}'.format(name, letter_grade))
if ttl_grade < 90:
    if ttl_grade < 80:
        if ttl_grade < 70:
            if ttl_grade < 60:
                letter_grade = 'F'
                print('{} has a letter grade of {}'.format(name, letter_grade))
#Print last statement
print('**** Thanks for using the lab calculator! ****')

