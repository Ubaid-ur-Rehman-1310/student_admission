import datetime
import mysql.connector
import pandas as pd
db=mysql.connector.connect(
    host='localhost',
    user='root',
    password='ubaid1999',
    database='student_admission'
)
mycursor=db.cursor()
mycursor.execute("""
                 CREATE TABLE IF NOT EXISTS students(
                 student_id INT AUTO_INCREMENT PRIMARY KEY,
                 first_name VARCHAR(50),
                 last_name VARCHAR(50),
                 date_of_birth DATE,
                 address VARCHAR(255),
                 email VARCHAR(100))
                """ )
def add_student():
    first_name=input('enter first name: ')
    last_name=input('enter last name: ')
    dob=input('date of birth (dd/mm/yyyy): ')
    dob = dob.split("/")
    dob = datetime.datetime(int(dob[2]), int(dob[1]), int(dob[0])) # convert date to 'YYYY-MM-DD HH:MM:SS' format
    address = input("Enter address: ")
    email=input('email: ')
    mycursor.execute("INSERT INTO students(first_name,last_name,date_of_birth,address,email) VALUES (%s,%s,%s,%s,%s)",(first_name,last_name,dob,address,email))
    db.commit()
    print('student added successfully!')
def view_all_students():
    mycursor.execute("SELECT * FROM students")
    students = mycursor.fetchall()
    if not students:
        print("No students found.")
    else:
        df = pd.DataFrame(students, columns=["Student ID", "First Name", "Last Name", "Date of Birth", "Address", "Email"])
        print(df)
def view_student():
    id=int(input('Enter the ID to search: '))
    mycursor.execute("SELECT * FROM students WHERE student_id = %s",(id,))
    result = mycursor.fetchone()
    if not result:
        print('No such record found!')
    else:
        student_data = {
            "Student ID": result[0],
            "First Name": result[1],
            "Last Name": result[2],
            "Date of Birth": result[3],
            "Address": result[4],
            "Email": result[5]
        }
        df = pd.DataFrame([student_data])
        print(df)
while True:
    print("\nStudent Admission Management System")
    print("1. Add Student")
    print("2. View all Students")
    print("3. Search a Student by ID")
    print("4. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        add_student()
    elif choice==2:
        view_all_students()
    elif choice==3:
        view_student()
    elif choice==4:
        print('Good bye!')
        break
    else:
        print("Invalid Choice! Try Again.")

        