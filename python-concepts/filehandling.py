with open("students.txt", "r") as file:
    for student in file:
        print(student.strip())