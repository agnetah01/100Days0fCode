def calculate_average_grade(scores):
    total_score = sum(scores)
    average_grade = total_score / len(scores)
    return average_grade

def main():
    print("Welcome to Grade Calculator")

    students = []
    grades = []

    num_students = int(input("Enter the number of students: "))

    for i in range(num_students):
        name = input(f"Enter name for student {i + 1}: ")
        students.append(name)

        while True:
            try:
                score = float(input(f"Enter score for {name}: "))
                if 0 <= score <= 100:
                    grades.append(score)
                    break
                else:
                    print("Invalid score! Score must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a numeric score.")

    average_grade = calculate_average_grade(grades)

    print("\n----- Grades Summary -----")
    for i in range(num_students):
        print(f"{students[i]} - Grade: {grades[i]}")

    print(f"\nAverage Grade: {average_grade:.2f}")


if __name__ == "__main__":
    main()
