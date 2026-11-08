att={}
while True:
    print("1. Add Attendance")
    print("2. Search Attendance")
    print("3. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        date=input("Enter date (YYYY-MM-DD): ")
        absent = 0
        present = 0
        i=0
        for i in range(1,5):
            status=input(f"Enter attendance for student {i} (p/a): ")
            
            if status.lower() == 'a':
                absent += 1
            elif status.lower() == 'p':
                present += 1
            else:
                print("Invalid input. Please enter 'p' for present or 'a' for absent.")
        att[date] = {'present': present, 'absent': absent}
        print()
        print(f"no of students present: {present}")
        print(f"no of students absent: {absent}")
    elif choice==2:
        search_date=input("Enter date (YYYY-MM-DD) to search: ")
        if search_date in att:
            print(f"Attendance for {search_date}: {att[search_date]}")
        else:
            print("No attendance record found for this date.")
    elif choice==3:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")