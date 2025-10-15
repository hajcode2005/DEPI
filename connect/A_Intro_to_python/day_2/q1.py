students = {}

def add_student():
    name = input("enter student name : ").strip()
    if  name == name.isdigit() or len(name) < 2:
        print("please enter a valid name.")
        return
    
    grade_input = input("enter your grade: ").strip()
    
    if grade_input.isdigit():
        grade = float(grade_input)
        if 0 <= grade <= 100:
            students[name] = grade
            print(f"name:{name} his grade :{grade}")
        else:
            print("the grade must be between 0 and 100.")
    else:
        print("please enter a valid number for the grade.")

def search_student():
    name = input("enter student name : ").strip()
    if name in students:
        print(f"name: {name} grade: {students[name]}")
    else:
        print("student not found.")

def calculate_average():
    if not students:
        print("no students available to calculate average.")
        return
    avg = sum(students.values()) / len(students)
    print(f"avg = {avg:.2f} (number of students : {len(students)})")

def menu():
    while True:
        print("\n--- Student Grade System ---")
        print("1. Add student")
        print("2. Search student")
        print("3. Calculate average grade")
        print("4. Exit")
        choice = input("choose from 1:4 ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            search_student()
        elif choice == "3":
            calculate_average()
        elif choice == "4":
            print("you exited the program.")
            break
        else:
            print("please enter a valid choice.")


if __name__ == "__main__":
    menu()