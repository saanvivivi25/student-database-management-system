#student database with USN, Name, and marks in 3 subjects

students = {
    "Arun": (101, 85, 78, 90),
    "Divya": (102, 65, 70, 68),
    "Kiran": (103, 45, 50, 48),
    "Sneha": (104, 92, 88, 95),
    "Rahul": (105, 55, 60, 58),
    "Anjali": (106, 73, 75, 70),
    "Vijay": (107, 35, 40, 38),
    "Meena": (108, 80, 82, 78),
    "Ravi": (109, 67, 64, 69),
    "Pooja": (110, 49, 52, 47)
}

search = input("Enter Name or USN: ")

for name in students:
    usn, m1, m2, m3 = students[name]

    if search.lower() == name.lower() or search == str(usn):

        average = (m1 + m2 + m3) / 3

        if average >= 90:
            grade = "A"
        elif average >= 80:
            grade = "B"
        elif average >= 70:
            grade = "C"
        elif average >= 60:
            grade = "D"
        else:
            grade = "Satisfied"

        print("USN:", usn)
        print("Name:", name)
        print("Marks:", m1, m2, m3)
        print("Average:", average)
        print("Grade:", grade)