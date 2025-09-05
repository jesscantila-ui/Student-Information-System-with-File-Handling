print('--------------- Interactive Information System ---------------')

students = {}

def add_student(id, name, age, grades):
    try:
        if type(id) is not int:
            raise ValueError("Student ID must be an integer.")
        if type(name) is not str:
            raise ValueError("Name must be a non-empty string.")
        if type(age) is not int:
            raise ValueError("Age must be an integer.")
        if not isinstance(grades, list):
            raise ValueError("Grades must be a list.")
        if not all(type(g) is int for g in grades):
            raise ValueError("All grades must be integers.")
        if id in students:
            raise ValueError("Student ID already exists.")

        students[id] = {"name": name, "age": age, "grades": grades}
        print(f"Added student ({id}: {name})\n")

    except ValueError as e:
        print(f"Invalid input: {e}\n")


def update_student(id, name=None, age=None, grades=None):
    try:
        if id not in students:
            raise KeyError(id)
        if name is not None:
            if type(name) is not str:
                raise ValueError("Provide Name.")
            students[id]["name"] = name
        if age is not None:
            if type(age) is not int:
                raise ValueError("Age must be an integer.")
            students[id]["age"] = age
        if grades is not None:
            if not isinstance(grades, list):
                raise ValueError("Grades must be a list.")
            if not all(type(g) is int for g in grades):
                raise ValueError("All grades must be integers.")
            students[id]["grades"] = grades

        print(f"Student {id} updated!\n")

    except KeyError as e:
        print(f"Student with ID {e} not found.\n")
    except ValueError as e:
        print(f"Invalid input: {e}\n")


def delete_student(id):
    try:
        if id not in students:
            raise KeyError(id)
        del students[id]
        print(f"Student {id} deleted!\n")
    except KeyError as e:
        print(f"Student with ID {e} not found.\n")


def display_students():
    if not students:
        print("No students to display.\n")
        return
    print("Student:")
    for sid, details in students.items():
        print(f"ID: {sid}, Name: {details['name']}, Age: {details['age']}")
        print("Grades:", " ".join(map(str, details["grades"])))
        print()

def save_to_file(filename="Student Info.txt"):
    try:
        with open(filename, "w") as file:
            for sid, details in students.items():
                grades_str = ", ".join(map(str, details["grades"]))
                file.write(f"{sid}|{details['name']}|{details['age']}|{grades_str}\n")
        print("Data saved to file.\n")
    except Exception as e:
        print(f"Error saving file: {e}\n")

def load_from_file(filename="students.txt"):
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split("|")
                if len(parts) != 4:
                    continue
                sid, name, age, grades_str = parts
                sid = int(sid)
                age = int(age)
                grades = list(map(int, grades_str.split(", "))) if grades_str else []
                students[sid] = {"name": name, "age": age, "grades": grades}
        print("All data is from file.\n")
    except FileNotFoundError:
        print("No file found.\n")
    except Exception as e:
        print(f"Error loading file: {e}\n")

def main():
    load_from_file()  

    while True:  
        print("----------- Student Management Menu -----------")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Save to File")
        print("6. Load from File")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            try:
                sid = int(input("ID: "))
                name = input("Name: ")
                age = int(input("Age: "))
                grades = list(map(int, input("Enter grades (space separated): ").split()))
                add_student(sid, name, age, grades)
            except ValueError:
                print("Invalid input. Please review.\n")

        elif choice == "2":
            display_students()

        elif choice == "3":
            try:
                sid = int(input("Enter ID to update: "))
                name = input("New Name (leave blank to skip): ")
                age_input = input("New Age (leave blank to skip): ")
                grades_input = input("New Grades (space separated, leave blank to skip): ")

                name = name if name else None
                age = int(age_input) if age_input else None
                grades = list(map(int, grades_input.split())) if grades_input else None

                update_student(sid, name, age, grades)
            except ValueError:
                print("Invalid input. Please enter correct data.\n")

        elif choice == "4":
            try:
                sid = int(input("Enter ID to delete: "))
                delete_student(sid)
            except ValueError:
                print("Student ID must be an integer.\n")

        elif choice == "5":
            save_to_file()

        elif choice == "6":
            load_from_file()

        elif choice == "7":
            print("Exiting program.byers~")
            break

        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
