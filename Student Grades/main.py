# Look through a dict of student scores and give a grade comment based on the student's score i.e.
# 91 and above = Outstanding, 81-90 = Exceeds expectation, 71-80 = Acceptable, 70 and lower = Fail


student_scores = {
    "Karla": 90,
    "Jim": 94,
    "Casey": 80,
    "Katrice": 79,
    "Kounde": 70,
}

for key in student_scores:
    if student_scores[key] <= 71:
        student_scores[key] = "Fail"
    elif student_scores[key] >= 91:
        student_scores[key] = "Outstanding"
    elif 81 <= student_scores[key] <= 90:
        student_scores[key] = "Exceeds Expectation"
    elif 71 <= student_scores[key] <= 80:
        student_scores[key] = "Acceptable"

print(student_scores)