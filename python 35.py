def calculate_grade(marks):
    total_marks = sum(marks)
    aggregate = total_marks / len(marks)

    if aggregate > 75:
        return "Distinction"
    elif aggregate >= 60:
        return "First Division"
    elif aggregate >= 50:
        return "Second Division"
    elif aggregate >= 40:
        return "Third Division"
    else:
        return "Fail"

if __name__ == "__main__":
    subjects = ['Subject 1', 'Subject 2', 'Subject 3', 'Subject 4']
    marks = []

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    total_marks = sum(marks)
    aggregate = total_marks / len(marks)
    grade = calculate_grade(marks)

    print("\nTotal marks:", total_marks)
    print("Aggregate:", aggregate)
    print("Grade:", grade)
