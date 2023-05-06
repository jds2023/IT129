import os
import csv
import json
import sqlite3
import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
from tkinter import filedialog 


class Student:
    def __init__(self, fname, lname, age, gpa):
       self.fname = fname
       self.lname = lname
       self.age = age
       self.gpa = gpa
    def insert_into_database(self, conn):
       cursor = conn.cursor()
       cursor.execute(f"INSERT INTO std(fname, lname, age, gpa) VALUES (?, ?, ?, ?)", (self.fname, self.lname, self.age, self.gpa))
       conn.commit()

def submit_form():
    text_box.insert(INSERT, "Submitting form...\n") 
    firstname = fname_entry.get()
    lastname = lname_entry.get()
    age = age_spinbox.get()
    gpa = gpa_entry.get()
    student = Student(firstname, lastname, age, gpa )
    student.insert_into_database(dbconnect)
    text_box.insert(INSERT, "One row inserted into the database\n") 
    
def upload_csv():
    csv_file = filedialog.askopenfilename()
    with open(f'{csv_file}') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            student = Student(row[1], row[2], row[3], row[4])
            student.insert_into_database(dbconnect)
            count += 1
        text_box.insert(INSERT, f"Importing CSV file {csv_file}...\n") 
        text_box.insert(INSERT, f"{count} rows inserted into the database\n") 
    
def upload_json():
    json_file = filedialog.askopenfilename()
    with open(f'{json_file}') as f:
        reader = json.load(f)
        count = 0
        for row in reader:
            student = Student(row['fname'], row['lname'], row['age'], row['gpa'])
            student.insert_into_database(dbconnect)
            count += 1
        text_box.insert(INSERT, f"Importing JSON file {json_file}...\n") 
        text_box.insert(INSERT, f"{count} rows inserted into the database\n") 
    
def delete_record():
   dump_db()
   id_string = (simpledialog.askstring('Student Id', "Enter one or more student ID (separated by comma's)"))
   
   # Convert the id_string into a list 
   id_list = id_string.split(",")  

   for i in id_list:
        id = int(i)
        cursor.execute(f"DELETE FROM std WHERE student_id = {id}")
    
def dump_db():
    clear_screen()
    text_box.insert(INSERT, "Dumping Student.db...\n") 

    for table_row in cursor.execute("SELECT * FROM std"):
         text_box.insert(INSERT, f"{table_row}\n")
           
def clear_screen():
    fname_entry.delete(0,END)
    lname_entry.delete(0,END)
    text_box.delete(1.0,END)
    gpa_entry.delete(0,END)
    age_var.set(0)
    ec_var.set("")
    title_var.set("")
    major_var.set("")

def close():
   root.destroy()
          
# Connect to database and create the std table if it doesn't already exist
dbconnect = sqlite3.connect("student.db")
cursor = dbconnect.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS std (student_id INTEGER PRIMARY KEY AUTOINCREMENT, fname TEXT NOT NULL, lname TEXT NOT NULL, age INTEGER, gpa REAL)")


# Create root window
root = tkinter.Tk()

# Create the title bar with the name of the program
root.title("DB Populator")

# Create a frame widget which is nested in the root window and use the pack layout manager 
frame = tkinter.Frame(root)
frame.pack()

# Create a label frame to store title, first name, last name, age and ethnicity
user_info_frame = tkinter.LabelFrame(frame, text="Student Information")
user_info_frame.grid(row=0, column=0, padx=20, pady=20 )

# Create a label label to store title, first and last name
title_label = tkinter.Label(user_info_frame, text="Title")
title_label.grid(row=0, column=0)
fname_label = tkinter.Label(user_info_frame, text="First Name")
fname_label.grid(row=0, column=1)
lname_label = tkinter.Label(user_info_frame, text="Last Name")
lname_label.grid(row=0, column=2)

# Create a combobox widget for title
title_var = tkinter.StringVar()
title_var.set("")
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."], textvariable=title_var)
title_combobox.grid(row=1, column=0)

# Create a entry widget for first name
fname_entry = tkinter.Entry(user_info_frame)
fname_entry.grid(row=1, column=1)

# Create a entry widget for last name
lname_entry = tkinter.Entry(user_info_frame)
lname_entry.grid(row=1, column=2)

# Create a label and spinbox widgets for age
age_var = tkinter.IntVar(root)
age_var.set(1)
age_label = tkinter.Label(user_info_frame, text="Age")
age_label.grid(row=2, column=0)
age_spinbox = tkinter.Spinbox(user_info_frame, from_= 0, to=100, textvariable=age_var)
age_spinbox.grid(row=3, column=0)

# Create a label and combobox for ethnity
ec_var = tkinter.StringVar()
ec_var.set("")
ethnicity_label = tkinter.Label(user_info_frame, text="Ethnicity")
ethnicity_label.grid(row=2, column=1)
ethnicity_combobox = ttk.Combobox(user_info_frame, values=["", "American Indian", "Asian", "Black or African American", "Latino","White", "Pacific Islander"], textvariable=ec_var)
ethnicity_combobox.grid(row=3, column=1)

# Space out all of the child widgets in the user_info_frame
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
    
# Create a label frame to store major, completed courses, and gpa
academic_frame = tkinter.LabelFrame(frame, text="")
academic_frame.grid(row=1, column=0, sticky="news", padx=20, pady=20 )

# Create a label and combobox for major
major_var = tkinter.StringVar()
major_var.set("")
major_label = tkinter.Label(academic_frame, text="Major")
major_label.grid(row=2, column=1)
major_combobox = ttk.Combobox(academic_frame, values=["", "Accounting", "Biochemisry", "Biology", "Biomedical Engineering", "Business Administration", \
    "Communication", "Computer Science", "Criminal Justice", "Economics", "Health Sciences", "Information Technology", "Mechanical Engineering", "Nursing" \
    "Neuroscience", "Politics", "Psychology"], textvariable=major_var)
major_combobox.grid(row=3, column=1)

# Create a label and entry widget for gpa
gpa_label = tkinter.Label(academic_frame, text="GPA")
gpa_label.grid(row=2, column=2)
gpa_entry = tkinter.Entry(academic_frame)
gpa_entry.grid(row=3, column=2)
    
# Space out all of the child widgets in the academic_frame
for widget in academic_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Create a label frame to store CSV, JSON, DB Dump, Delete, Exit and Clear buttons 
import_frame = tkinter.LabelFrame(frame, text="")
import_frame.grid(row=4, column=0, sticky="news", padx=20, pady=20 )

text_box = tkinter.Text(frame, height=10, width=50, padx=15, pady=15)
text_box.grid(row=2, column = 0, padx=20, pady = 20)

submit_button  = tkinter.Button(frame, text="Submit", command=submit_form)
submit_button.grid(row=3, column = 0, padx=20, pady = 20)

csv_button  = tkinter.Button(import_frame, text="Import CSV file", command=upload_csv)
csv_button.grid(row=1, column = 0, padx=20, pady = 20)

json_button  = tkinter.Button(import_frame, text="Import JSON file", command=upload_json )
json_button.grid(row=1, column = 1, padx=20, pady = 20)

db_dump_button  = tkinter.Button(import_frame, text="Display DB Records", command=dump_db)
db_dump_button.grid(row=1, column = 2, padx=20, pady = 20)

db_delete_button  = tkinter.Button(import_frame, text="Delete DB Record(s)", command=delete_record)
db_delete_button.grid(row=1, column = 3, padx=20, pady = 20)

exit_button  = tkinter.Button(import_frame, text="Exit", command=close)
exit_button.grid(row=2, column = 1, padx=20, pady = 20)

clear_button  = tkinter.Button(import_frame, text="Clear", command=clear_screen)
clear_button.grid(row=2, column = 2, padx=20, pady = 20)

root.mainloop()

dbconnect.commit()
dbconnect.close()