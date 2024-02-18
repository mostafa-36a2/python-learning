import csv
import os

print(os.getcwd())
with open("employee_file.csv", mode="w") as employee_file:
    employee_writer = csv.writer(
        employee_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL
    )

    employee_writer.writerow(["Column Header1", "Column Header2", "Column Header3"])
    employee_writer.writerow(["Content1", "Content2", "Content3"])
