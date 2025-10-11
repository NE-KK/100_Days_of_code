# 100 Days of code by Angela Yu
# Day 9 - Challenge 1 - Gradient Program

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

def grades(score):
    if score >= 91:
        return "Outstanding"
    elif score >= 81:
        return "Exceeds Expectations"
    elif score >= 71:
        return "Acceptable"
    else:
        return "Fail"
    
for student in student_scores:
    get_score = student_scores[student]
    student_grades.update({student: grades(get_score)})

print(student_grades)
