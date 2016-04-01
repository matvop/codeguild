#student tracker created  at PDX Code Guild 3.17.2016
#will use data structures to accomplish goal - # of set students in a class
#and which students are in a particular class. this is incomplete

class_name_to_students = {}

accept_input = True
while accept_input: #enter a while loop here for finding students/classes
    print('Student name?')
    student_name = input()
    accept_input = student_name != 'done'
    print('what class is ' + student_name + ' in?')
    class_name = input()
    old_roster = set()
    class_name_to_students[class_name]
    new_roster = old_roster | {student_name}
    class_name_to_roster[class_name]


print(class_name_to_students)
