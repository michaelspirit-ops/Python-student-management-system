import csv


# the main menu
def main():
    records = []

    while True:
        print("\n==============Student Management System==============\n")
        print("1. View students' list")
        print("2. Add student")
        print("3. Remove student")
        print("4. Find student")
        print("5. Update student records")
        print("6. Clear list")
        print("7. Save records(CSV)")
        print("8. Open records(CSV)")
        print("9. Exit")

        choice = input("\nYour choice: ")

        print("\n=====================================================")

        match choice:
            case "1":
                view_list(records)
            case "2":
                records = add_student(records)
            case "3":
                records = remove_student(records)
            case "4":
                find_student(records)
            case "5":
                records = update_info(records)
            case "6":
                clear_list(records)
            case "7":
                save_records(records)
            case "8":
                open_records(records)
            case "9":
                if confirm_exit():
                    break
                else:
                    continue
            case _:
                print("Enter a number ranging from 1 and 9")


# view the names of students in the list
def view_list(me):
    if me:
        print("\n----------------------Students-----------------------")

        for student in me:
            print(student.get("Name", ""))

        print("-----------------------------------------------------")
    else:
        print("\nList is empty")


# add student(s) to the list
def add_student(to):
    while True:
        try:
            number = int(input("\nHow many students are you adding? ").strip())
            break
        except ValueError:
            print("Please input a number")

    for i in range(number):
        while True:
            name = input(f"\nName of student {i + 1}: ").strip().title()
            already = False

            for search in to:
                if name == search.get("Name", ""):
                    already = True
                    print("Student is already in the list")

            if not already:
                break

        info = {
            "English language": 0,
            "Science": 0,
            "Core Mathematics": 0,
            "Social studies": 0,
            "Chemistry": 0,
            "Biology": 0,
            "Physics": 0,
            "ICT": 0,
        }

        for subject in info:
            while True:
                try:
                    score = int(input(f"Enter score for {subject}: ").strip())

                    if 0 <= score <= 100:
                        info[subject] += score
                        break
                    else:
                        print("Score must between 0 and 100")
                except ValueError:
                    print("Score must be a number between 0 and 100 inclusive")

        grade = calculate_grade(sum(info.values()))

        info.update({"Name": name, "Grade": grade})
        to.append(info)

    print("\nRecords have been saved")

    return to


# remove a student from the list
def remove_student(here):
    student = input("\nEnter name of student to remove: ").strip().title()

    for search in here:
        if student == search.get("Name"):
            here.pop(here.index(search))
            print(f"{student} has been removed successfully")
            return here

    print("Student not found")

    return here


# find a student in the list
def find_student(here):
    find = input("\nEnter the name of the student: ").strip().title()
    found = False

    for student in here:
        if find == student.get("Name", ""):
            print("\n-----------------------------------------------------", end="")
            print(
                "\n" f"Name: {find}",
                f"English language: {student["English language"]}",
                f"Science: {student["Science"]}",
                f"Core Mathematics: {student["Core Mathematics"]}",
                f"Social studies: {student["Social studies"]}",
                f"Chemistry: {student["Chemistry"]}",
                f"Biology: {student["Biology"]}",
                f"Physics: {student["Physics"]}",
                f"ICT: {student["ICT"]}",
                f"Grade: {student["Grade"]}",
                sep="\n",
            )
            print("-----------------------------------------------------")
            
            found = True

    if not found:
        print("Student not found")


# update the records of a student
def update_info(here):
    name = input("\nWhat's the name of the student to update his or her records? ").strip().title()
    found = False

    for search in here:
        if name == search.get("Name", ""):
            record = here[here.index(search)]
            total = 0
            found = True

    if not found:
        print("Student not found")
        return here

    for subject, value in record.items():
        if str(value).isnumeric():
            while True:
                try:
                    score = int(input(f"\nEnter score for {subject}: ").strip())

                    if 0 <= score <= 100:
                        record[subject] = score
                        total += int(score)
                        break
                    else:
                        print("Score must be between 0 and 100")
                except ValueError:
                    print("Score must be a number between 0 and 100 inclusive")

    record["Grade"] = calculate_grade(total)

    print(f"\n{name}'s records have been updated successfully")

    return here


# find the grade of a student
def calculate_grade(total):
    average = total / 8

    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"


# delete every student in the list
def clear_list(me):
    while True:
        choice = input("\nClear every student from the list(y/n)? ").lower()

        if choice == "y" or choice == "yes":
            print("List have been cleared")
            return me.clear()
        elif choice == "n" or choice == "no":
            return me
        else:
            print("Pick yes or no")


# save the records in the list as a CSV file
def save_records(to):
    name = input("\nType a name for the records: ")

    if not name.endswith(".csv"):
        name = name + ".csv"

    with open(name, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "Name",
                "English language",
                "Science",
                "Core Mathematics",
                "Social studies",
                "Chemistry",
                "Biology",
                "Physics",
                "ICT",
                "Grade",
            ],
        )
        writer.writeheader()

        for student in to:
            writer.writerow(
                {
                    "Name": student["Name"],
                    "English language": student["English language"],
                    "Science": student["Science"],
                    "Core Mathematics": student["Core Mathematics"],
                    "Social studies": student["Social studies"],
                    "Chemistry": student["Chemistry"],
                    "Biology": student["Biology"],
                    "Physics": student["Physics"],
                    "ICT": student["ICT"],
                    "Grade": student["Grade"],
                }
            )

    print(f"Records have been saved as {name}")


# load a CSV file containing the records of students into the list
def open_records(here):
    if here:
        while True:
            choice = input("\nReplace current records with new records(y/n)? ")

            if choice == "y":
                name = input("\nEnter name of the records to open: ").strip()
                break
            elif choice == "n":
                return
    else:
        name = input("\nEnter name of the records to open: ").strip()

    if not name.endswith(".csv"):
        name = name + ".csv"

    try:
        with open(name, "r", newline="") as file:
            reader = csv.DictReader(file)
            here.clear()

            for row in reader:
                here.append(row)

            print("Records have been loaded into memory")
    except FileNotFoundError:
        print("\nFile not found")
        print("Try putting the file in the same folder as this program")
        return


# confirm exit of program
def confirm_exit():
    while True:
        choice = input("\nClose the program?(y/n)? ").lower()

        if choice == "y" or choice == "yes":
            return True
        elif choice == "n" or choice == "no":
            return False
        else:
            print("Pick yes or no")


if __name__ == "__main__":
    main()
