# program to display student's marks from record
student_name = 'Jamila'

marks = {'Kenan': 90, 'Jamila': 55, 'leyla': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')