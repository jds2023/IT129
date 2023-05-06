import csv
import json
import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog

########################################################################################################################################
# Define Student class and insert method
########################################################################################################################################
class Student:
    def __init__(self, title, fname, lname, age, gpa, major, courses):
       self.title = title
       self.fname = fname
       self.lname = lname
       self.age = age
       self.gpa = gpa
       self.major = major
       self.courses = courses

    def insert_into_database(self, conn):
       cursor = conn.cursor()
       cursor.execute(f"INSERT INTO std(title, fname, lname, age, gpa, major, courses) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.title, self.fname, self.lname, self.age, self.gpa, self.major, self.courses))
       conn.commit()

########################################################################################################################################=
# Declare Functions
########################################################################################################################################
def submit_form():
    text_box.insert(tk.INSERT, "Submitting form...\n")
    title = title_var.get()
    firstname = fname_entry.get()
    lastname = lname_entry.get()
    age = age_spinbox.get()
    gpa = gpa_entry.get()
    major = major_var.get()
    courses = courses_var.get()
    student = Student(title, firstname, lastname, age, gpa, major, courses)
    student.insert_into_database(dbconnect)
    text_box.insert(tk.INSERT, "One row inserted into the database\n")

def upload_csv():
    clear_screen()
    csv_file = filedialog.askopenfilename()
    with open(f'{csv_file}') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            student = Student(row[1], row[2], row[3], row[4], row[5], row[6], row[7])
            student.insert_into_database(dbconnect)
            count += 1
        text_box.insert(tk.INSERT, f"Importing CSV file {csv_file}...\n")
        text_box.insert(tk.INSERT, f"{count} rows inserted into the database\n")
    
def upload_json():
    clear_screen()
    json_file = filedialog.askopenfilename()
    with open(f'{json_file}') as f:
        reader = json.load(f)
        count = 0
        for row in reader:
            student = Student(row['title'], row['fname'], row['lname'], row['age'], row['gpa'], row['major'], row['courses'])
            student.insert_into_database(dbconnect)
            count += 1
        text_box.insert(tk.INSERT, f"Importing JSON file {json_file}...\n")
        text_box.insert(tk.INSERT, f"{count} rows inserted into the database\n")
    
def delete_record():
   dump_db()
   id_string = (simpledialog.askstring('Student Id', "Enter one or more student ID (e.g. 1,2,3,4)"))

   # Convert the id_string into a list
   id_list = id_string.split(",") 
   for i in id_list:
        id = int(i)
        cursor.execute(f"DELETE FROM std WHERE student_id = {id}")
        dump_db()

def dump_db():
    clear_screen()
    cursor.execute("SELECT * from std")
    rows = cursor.fetchall()
    if len(rows) == 0:
          text_box.insert(tk.INSERT,"Database is empty")
    else:
        for table_rows in rows:
          text_box.insert(tk.INSERT, f"{table_rows}\n")

def clear_screen():
    title_var.set("")
    fname_entry.delete(0,tk.END)
    lname_entry.delete(0,tk.END)
    age_var.set(0)
    gpa_entry.delete(0,tk.END)
    major_var.set("")
    courses_var.set(0)
    text_box.delete(1.0,tk.END)
 
def close():
   root.destroy()        

########################################################################################################################################
# Connect to database and create the std table if it doesn't already exist
########################################################################################################################################
dbconnect = sqlite3.connect("student.db")
cursor = dbconnect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS std (student_id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, fname TEXT NOT NULL, lname TEXT NOT NULL, age INTEGER, gpa REAL, major TEXT NOT NULL, courses INTEGER)")

########################################################################################################################################
# Create root window
########################################################################################################################################
root = tk.Tk()

# Create the title bar with the name of the program
root.title("DB Populator")

# Create a frame widget which is nested in the root window and use the pack layout manager
frame = tk.Frame(root)
frame.pack()
 
########################################################################################################################################
# Create a user info label frame to store title, first name, last name, and age
########################################################################################################################################
user_info_frame = tk.LabelFrame(frame, text="Student Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20 ) 

# Create a label label to store title, first and last name
title_label = tk.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=0)

fname_label = tk.Label(user_info_frame, text="First Name")
fname_label.grid(row=0, column=1)
lname_label = tk.Label(user_info_frame, text="Last Name")
lname_label.grid(row=0, column=2) 

# Create a combobox widget for title
title_var = tk.StringVar()
title_var.set("")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."], textvariable=title_var)
title_combobox.grid(row=1, column=0)

# Create a entry widget for first name
fname_entry = tk.Entry(user_info_frame)
fname_entry.grid(row=1, column=1) 

# Create a entry widget for last name
lname_entry = tk.Entry(user_info_frame)
lname_entry.grid(row=1, column=2)

# Create a label and spinbox widgets for age
age_var = tk.IntVar(root)
age_var.set(0)
age_label = tk.Label(user_info_frame, text="Age")
age_label.grid(row=0, column=4)
age_spinbox = tk.Spinbox(user_info_frame, from_= 0, to=100, textvariable=age_var)
age_spinbox.grid(row=1, column=4) 

# Space out all of the child widgets in the user_info_frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

########################################################################################################################################
# Create an academic label frame to store gpa, major, and completed courses
########################################################################################################################################
academic_frame = tk.LabelFrame(frame, text="Academic Information")
academic_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20 )

# Create a label and combobox for major
major_var = tk.StringVar()
major_var.set("")
major_label = tk.Label(academic_frame, text="Major")
major_label.grid(row=2, column=2)
major_combobox = ttk.Combobox(academic_frame, values=["", "Accounting", "Biochemisry", "Biology", "Biomedical Engineering", "Business Administration", \
    "Communication", "Computer Science", "Criminal Justice", "Economics", "Health Sciences", "Information Technology", "Mechanical Engineering", "Nursing" \
    "Neuroscience", "Politics", "Psychology"], textvariable=major_var)
major_combobox.grid(row=3, column=2)

# Create a label and entry widget for gpa
gpa_label = tk.Label(academic_frame, text="GPA")
gpa_label.grid(row=2, column=1)
gpa_entry = tk.Entry(academic_frame)
gpa_entry.grid(row=3, column=1)

# Create a label and spinbox widgets for completed
courses_var = tk.IntVar()
courses_var.set(0)
courses_label = tk.Label(academic_frame, text="Completed Courses")
courses_label.grid(row=2, column=3)
courses_spinbox = tk.Spinbox(academic_frame, from_= 0, to=100, textvariable=courses_var)
courses_spinbox.grid(row=3, column=3)

# Space out all of the child widgets in the academic_frame
for widget in academic_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

########################################################################################################################################
# Create a text box and submit button
########################################################################################################################################

text_box = tk.Text(frame, height=10, width=50, padx=15, pady=15)
text_box.grid(row=2, column = 0, padx=20, pady = 20)

submit_button  = tk.Button(frame, text="Submit", command=submit_form)
submit_button.grid(row=3, column = 0, padx=20, pady = 20)


########################################################################################################################################
# Create an import label frame to store CSV, JSON, DB Dump, Delete, Exit and Clear buttons
########################################################################################################################################

import_frame = tk.LabelFrame(frame, text="")
import_frame.grid(row=4, column=0, sticky="news", padx=20, pady=20 )

csv_button  = tk.Button(import_frame, text="Import CSV file", command=upload_csv)
csv_button.grid(row=1, column = 0, padx=20, pady = 20)

json_button  = tk.Button(import_frame, text="Import JSON file", command=upload_json )
json_button.grid(row=1, column = 1, padx=20, pady = 20)

db_dump_button  = tk.Button(import_frame, text="Display DB Records", command=dump_db)
db_dump_button.grid(row=1, column = 2, padx=20, pady = 20)
db_delete_button  = tk.Button(import_frame, text="Delete DB Record(s)", command=delete_record)
db_delete_button.grid(row=1, column = 3, padx=20, pady = 20)

exit_button  = tk.Button(import_frame, text="Exit", command=close)
exit_button.grid(row=2, column = 1, padx=20, pady = 20)

clear_button  = tk.Button(import_frame, text="Clear", command=clear_screen)
clear_button.grid(row=2, column = 2, padx=20, pady = 20)

root.mainloop()

dbconnect.commit()
dbconnect.close()