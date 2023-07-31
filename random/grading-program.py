student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Herminone": 99,
    "Draco": 74,
    "Neville": 62
}

student_grades = {}
for score in student_scores:
    grade = student_scores[score]
    if grade >= 91:
        grade = "Outstanding"
    elif grade >= 81 and grade <= 90: 
        grade = "Exceeds Expectations"
    elif grade >= 71 and grade <= 80:
        grade = "Acceptable"
    else:
        grade = "Fail"
    print(grade)
