attendance = {}
n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    status = input("Enter attendance (P/A): ").upper()
    attendance[name] = status

print("\nAttendance Report")
for name, status in attendance.items():
    if status == "P":
        print(name, "- Present")
    else:
        print(name, "- Absent")
