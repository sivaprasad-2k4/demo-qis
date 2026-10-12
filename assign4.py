# Assignment 4 – Inventory File System
# Build a program that reads employee attendance data from a text/CSV file (each line containing employee name, date and status: Present/Absent) and analyzes attendance patterns, producing a full report.
# Requirements:
# •	Read attendance records from a file attendance.csv using the csv module or manual line parsing.
# •	Calculate the total number of present and absent days for each employee.
# •	Identify and report any employee whose attendance percentage is below 75%.
# •	Write a summary report back out to a new file (attendance_report.txt) using the with statement in write mode.
# •	Provide a way to append a new day's attendance data to the source file without overwriting existing records.
# •	Handle missing files or malformed lines gracefully using appropriate checks.





import csv

with open("attendance.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Employee", "Date", "Status"])
    writer.writerow(["Arun", "2026-10-01", "Present"])
    writer.writerow(["Arun", "2026-10-02", "Absent"])
    writer.writerow(["Anu", "2026-10-01", "Absent"])
    writer.writerow(["Rahul", "2026-10-01", "Present"])

attendance = {}

with open("attendance.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        name = row["Employee"]
        status = row["Status"]

        if status not in ["Present", "Absent"]:
            print("Invalid record:", row)
            continue

        if name not in attendance:
            attendance[name] = {"Present": 0, "Absent": 0}

        attendance[name][status] += 1

with open("attendance_report.txt", "w") as file:
    for name, data in attendance.items():
        present = data["Present"]
        absent = data["Absent"]
        percentage = present / (present + absent) * 100

        report = (
            f"Employee: {name}\n"
            f"Present: {present}\n"
            f"Absent: {absent}\n"
            f"Attendance: {percentage:.2f}%\n"
        )

        if percentage < 75:
            report += "Attendance below 75%!\n"

        print(report)
        file.write(report + "\n")

print("Report created successfully!")

name = input("Enter employee name: ")
date = input("Enter date: ")
status = input("Enter status (Present/Absent): ").capitalize()

if name.strip() and date.strip() and status in ["Present", "Absent"]:
    with open("attendance.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, date, status])
    print("Attendance added successfully!")
else:
    print("Invalid input!")
    


