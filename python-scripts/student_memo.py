names = input("Enter names: ").title().split(",")
assignments = input("Enter assignment count: ").split(",")
grades = input("Enter grades: ").split(",")
#potential_grade = grades + (assignments * 2)
place_holder = 100


message = "Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. Your current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade) + int(assignment) * 2))

