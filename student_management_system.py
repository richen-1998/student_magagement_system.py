def show_menu():
    print("---------------------------")
    print("STUDENT MANAGEMENT SYSTEM")
    print("---------------------------")
    print()
    print('1. Add student')
    print("2. View students")
    print("3. Search student")
    print("4. Show statistics")
    print("5. Show passing students")
    print("6. Remove student")
    print("7. Exit")

students = []

def add_student(students):
    print()
    print("---- ADD STUDENT ----")

    name = input("Studen name: ").strip().title()
    score = float(input("Score: "))

    while score < 0 or score > 100:
        print("Score must be between 0 and 100.")
        score = float(input("Score: "))

    student = {
        'name' : name,
        'score' : score
    }

    students.append(student)
    print('Student added.')

def view_students(students):
    print()
    print("------ ALL STUDENTS -----")

    if len(students) == 0:
        print("No students recoreded.")
        return

    for student in students:
        print(f'{student['name']} - {student['score']:.2f}')
 



def search_student(students):

    print()
    print("----- SEARCH STUDENT ----")

    if len(students) == 0:
        print("No students recorded.")
        return

    target = input("Student name: ").strip().lower()

    for student in students:

        if student['name'].lower() == target:
            print('Student found.')
            print(f'Name: {student['name']}')
            print(f'Score: {student['score']:.2f}')
            return

        print("Student not found.")


def show_statistics(students):
    print()
    print("---- STUDENT STATISTICS ----")

    if len(students) == 0:
        print("No students recoreded.")
        return

    total = 0

    highest_student = students[0]
    lowest_student = students[0]

    for student in students:
        total += student['score']

        if student['score'] > highest_student['score']:
            highest_student = student

        if student['score'] < lowest_student['score']:
            lowest_student = student

    average = total / len(students)

    print(f'Number of students: {len(students)}')
    print(f'Average score: {average:.2f}')

    print()
    print(
        f"Highest-scoring student: "
        f"{highest_student['name']}"
    )
    print(f"Highest score: {highest_student['score']:.2f}")

    print()
    print(
        f"Lowest-scoring student: "
        f"{lowest_student['name']}"
    )
    print(f"Lowest score: {lowest_student['score']:.2f}")




def show_passing_students(students):
    print()
    print("---- PASSING STUDENTS ----")

    if len(students) == 0:
        print('No students recorded.')
        return

    passed = 0
    failed = 0

    for student in students:
        if student['score']>=40:
            print(f'{student['name']} - {student['score']:.2f}')
            passed +=1

        else:
            failed += 1


    print()
    print(f'Number passed: {passed}')
    print(f'Number failed: {failed}')

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
            print("Student removed.")
            return

    print("Student not found.")



while True:

    show_menu()

    choose_option = input("\nChoose: ").strip()

    if choose_option == "1":
        add_student(students)

    elif choose_option == "2":
        view_students(students)

    elif choose_option == "3":
        search_student(students)

    elif choose_option == "4":
        show_statistics(students)

    elif choose_option == "5":
        show_passing_students(students)

    elif choose_option == "6":
        remove_student(students)

    elif choose_option == "7":
        print("Thank you.")
        break

    else:
        print("Invalid option. Choose 1-7")

    


    