students_list = ['Hermine', 'Nare', 'Anahit']
while True:
    student_name = input('Enter student name or "q" for quit: ')
    if student_name == 'q':
        break

    # for student in students_list:
    #     if student == student_name:
    #         print('Student', student_name, 'in students list')
    #         break
    # else:
    #     print('Student', student_name, 'not in students list')

    if student_name in students_list:
        print('Student', student_name, 'in students list')
    else:
        print('Student', student_name, 'not in students list')
        choice = input('Dou you want add student in students list?[y/n] ')
        if choice == 'y':
            students_list.append(student_name)
            print('Student', student_name, 'successfully added in students list.')

print(students_list)