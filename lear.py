def letter_grade(score):
    if score < 75:
        return "F"
    elif 75 <= score <= 80:
        return "D"
    elif 80 < score <= 89:
        return "C"
    elif 89 < score <= 93:
        return "B"
    elif 93 < score <= 100:
        return "A"


while True:
    try:
        student_amount = int(input("How many students are there? "))
    except ValueError:
        print("Please type a valid number")
    else:
        name_list = []
        scores = []
        for student in range(student_amount):
            student_name = input("What is the name of the student? ")
            name_list.append(student_name)
            while True:
                try:
                    student_score = int(
                        input(f"What is the score of {student_name}? "))
                    if student_score >= 0 and student_score <= 100:
                        scores.append(student_score)
                        break
                    else:
                        print("Score cannot be less than 0 or greater than 100")

                except ValueError:
                    print("Please type a valid number")

        break

student_grades = dict(zip(name_list, scores))
print("Summary Report")
for student, grade in student_grades.items():
    print(f"Name:{student} Score: {grade:02} Grade: {letter_grade(grade)}")

total_students = len(student_grades)
highest_scorer = max(student_grades, key=student_grades.get)
print(f"Class Average: {sum(scores)/total_students:.2f}")
print(f"Highest Scorer: {highest_scorer}")
