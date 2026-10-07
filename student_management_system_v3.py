import json


def load_students():

    try:

        with open("students.json", "r") as file:
            students = json.load(file)

        return students

    except FileNotFoundError:
        return []


def save_students(students):

    with open("students.json", "w") as file:
        json.dump(students, file, indent=4)


def show_menu():

    print()
    print("--------------------------------")
    print("STUDENT MANAGEMENT SYSTEM")
    print("--------------------------------")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Show statistics")
    print("5. Show passing students")
    print("6. Remove student")
    print("7. Exit")


def get_valid_name():

    while True:

        name = input("Student name: ").strip()

        if name != "":
            return name.title()

        print("Name cannot be empty.")


def get_valid_score():

    while True:

        try:

            score = float(input("Score: "))

            if 0 <= score <= 100:
                return score

            print("Score must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")


def student_exists(students, name):

    for student in students:

        if student["name"].lower() == name.lower():
            return True

    return False


def add_student(students):

    print()
    print("--- ADD STUDENT ---")

    name = get_valid_name()

    if student_exists(students, name):
        print("A student with that name already exists.")
        return

    score = get_valid_score()

    student = {
        "name": name,
        "score": score
    }

    students.append(student)

    save_students(students)

    print("Student added and saved.")


def view_students(students):

    print()
    print("--- ALL STUDENTS ---")

    if len(students) == 0:
        print("No students recorded.")
        return

    for student in students:
        print(f"{student['name']} — {student['score']:.2f}")


def search_student(students):

    print()
    print("--- SEARCH STUDENT ---")

    if len(students) == 0:
        print("No students recorded.")
        return

    target = input("Student name: ").strip().lower()

    for student in students:

        if student["name"].lower() == target:

            print("Student found.")
            print(f"Name: {student['name']}")
            print(f"Score: {student['score']:.2f}")

            return

    print("Student not found.")


def show_statistics(students):

    print()
    print("--- STUDENT STATISTICS ---")

    if len(students) == 0:
        print("No students recorded.")
        return

    total = 0

    highest_student = students[0]
    lowest_student = students[0]

    for student in students:

        total += student["score"]

        if student["score"] > highest_student["score"]:
            highest_student = student

        if student["score"] < lowest_student["score"]:
            lowest_student = student

    average = total / len(students)

    print(f"Number of students: {len(students)}")
    print(f"Average score: {average:.2f}")

    print(
        f"Highest: {highest_student['name']} "
        f"({highest_student['score']:.2f})"
    )

    print(
        f"Lowest: {lowest_student['name']} "
        f"({lowest_student['score']:.2f})"
    )


def show_passing_students(students):

    print()
    print("--- PASSING STUDENTS ---")

    if len(students) == 0:
        print("No students recorded.")
        return

    passed = 0
    failed = 0

    for student in students:

        if student["score"] >= 40:

            print(
                f"{student['name']} — "
                f"{student['score']:.2f}"
            )

            passed += 1

        else:
            failed += 1

    print()
    print(f"Number passed: {passed}")
    print(f"Number failed: {failed}")


def remove_student(students):

    print()
    print("--- REMOVE STUDENT ---")

    if len(students) == 0:
        print("No students recorded.")
        return

    target = input("Student name: ").strip().lower()

    for student in students:

        if student["name"].lower() == target:

            students.remove(student)

            save_students(students)

            print("Student removed and changes saved.")

            return

    print("Student not found.")



# MAIN PROGRAM


students = load_students()


while True:

    show_menu()

    choice = input("\nChoose: ").strip()

    if choice == "1":
        add_student(students)

    elif choice == "2":
        view_students(students)

    elif choice == "3":
        search_student(students)

    elif choice == "4":
        show_statistics(students)

    elif choice == "5":
        show_passing_students(students)

    elif choice == "6":
        remove_student(students)

    elif choice == "7":
        print("Goodbye.")
        break

    else:
        print("Invalid option. Choose 1-7.")