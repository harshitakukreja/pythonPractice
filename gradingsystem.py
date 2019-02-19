from statistics import mean

admins = {'Harshita': 'Pass@123', 'Teacher': 'Teach@123'}

studentDict = {'Ankur': [78, 88, 93],
               'Dhyara': [92, 76, 88],
               'Jai': [89, 92, 93],
               'Shree': [69, 82, 94]}


def enterGrade():
    nameToEnter = input('Student Name: ')
    gradeToEnter = input('Grade: ')

    if nameToEnter in studentDict:
        print('Adding the Grade...')
        studentDict[nameToEnter].append(float(gradeToEnter))
    else:
        print('This student does not exist.')

    print(studentDict)


def removeStudent():
    nameToRemove = input('What student do you want to remove?: ')
    if nameToRemove in studentDict:
        print('Removing Student...')
        del studentDict[nameToRemove]

    print(studentDict)


def studentAvg():
    for eachStudent in studentDict:
        gradeList = studentDict[eachStudent]
        avgGrade = mean(gradeList)

        print(eachStudent, 'has an average grade of:', avgGrade)


def main():
    print("""
    Welcome to the grading Portal
    1 - Enter Grades of a Student
    2 - Remove a Student
    3 - Find Average Grades of a Student
    4 - Exit
    """)

    action = input('What would you like to do? (Enter a number) ')

    if action == '1':
        enterGrade()
    elif action == '2':
        removeStudent()
    elif action == '3':
        studentAvg()
    elif action == '4':
        exit()
    else:
        print('No valid choice was given, try again')


login = input('Username: ')
passw = input('Password: ')

if login in admins:
    if admins[login] == passw:
        print('Welcome,', login)
        while True:
            main()
    else:
        print('Invalid password, please enter the correct password.')
else:
    print('Invalid username, try again with a valid username.')













