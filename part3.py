from tkinter import *
import time
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas as pd
import mysql.connector 
#Functionality Part
def iexit():
    result=messagebox.askyesno('Confirm','Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass


def toplevel_data(title,button_text,command):
    global Registration_numberEntry,phoneEntry,nameEntry,emailEntry,addressEntry,genderEntry,dobEntry,cityEntry,stateEntry,branch_idEntry,screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)
    Registration_numberLabel = Label(screen, text='Registration_number', font=('times new roman', 20, 'bold'))
    Registration_numberLabel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    Registration_numberEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    Registration_numberEntry.grid(row=0, column=1, pady=15, padx=10)

    nameLabel = Label(screen, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, pady=15, padx=10)

    phoneLabel = Label(screen, text='Phone', font=('times new roman', 20, 'bold'))
    phoneLabel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    phoneEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    phoneEntry.grid(row=2, column=1, pady=15, padx=10)

    emailLabel = Label(screen, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    emailEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, pady=15, padx=10)

    addressLabel = Label(screen, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, pady=15, padx=10)

    genderLabel = Label(screen, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(row=5, column=0, padx=30, pady=15, sticky=W)
    genderEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, pady=15, padx=10)

    dobLabel = Label(screen, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(row=6, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, pady=15, padx=10)

    cityLabel = Label(screen, text='City', font=('times new roman', 20, 'bold'))
    cityLabel.grid(row=7, column=0, padx=30, pady=15, sticky=W)
    cityEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    cityEntry.grid(row=7, column=1, pady=15, padx=10)
    
    stateLabel = Label(screen, text='State', font=('times new roman', 20, 'bold'))
    stateLabel.grid(row=8, column=0, padx=30, pady=15, sticky=W)
    stateEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    stateEntry.grid(row=8, column=1, pady=15, padx=10)
    
    branch_idLabel = Label(screen, text='Branch_id', font=('times new roman', 20, 'bold'))
    branch_idLabel.grid(row=9, column=0, padx=30, pady=15, sticky=W)
    branch_idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    branch_idEntry.grid(row=9, column=1, pady=15, padx=10)
    
    student_button = ttk.Button(screen, text=button_text, command=command)
    student_button.grid(row=10, columnspan=2, pady=15)
    if title=='Update Student':
        indexing = studentTable.focus()

        content = studentTable.item(indexing)
        listdata = content['values']
        Registration_numberEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        phoneEntry.insert(0, listdata[2])
        emailEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])
        genderEntry.insert(0, listdata[5])
        dobEntry.insert(0, listdata[6])


def update_data():
    query = "update student set name=%s,phone_number=%s,email=%s,address=%s,gender=%s,dob=%s where registration_number=%s"
    mycursor.execute(
        query,
        (
            nameEntry.get(),
            phoneEntry.get(),
            emailEntry.get(),
            branch_idEntry.get(),
            genderEntry.get(),
            dobEntry.get(),
            Registration_numberEntry.get(),
        ),
    )
    con.commit()
    messagebox.showinfo(
        "Success",
        f"Id {Registration_numberEntry.get()} is modified successfully",
        parent=screen,
    )
    screen.destroy()
    show_student()


def set_column(column_headings):
    column_count = len(column_headings)
    column_ids = [str(i) for i in range(1, column_count)]
    print(column_ids)
    studentTable["columns"] = column_ids
    column_ids.insert(0, "#0")
    for id,  heading in zip(column_ids,column_headings):
        studentTable.heading(id, text=heading)
        studentTable.column(id, minwidth=0, width=100, stretch=NO)
        
# Fetch student details from the database
def show_student():
    try:
        mycursor.execute('SELECT * FROM student')
        data = mycursor.fetchall()
        # print(data)

        # Clear existing data in the Treeview
        for row in studentTable.get_children():
            studentTable.delete(row)
            
        set_column(["Registration_Number", "Name", "Email", "Phone_number", 
                     "City" , "State", "Gender", "DOB","Added_date", "Added_time", "Address", "Branch_id"])
        # Insert fetched data into the Treeview
        for i, row in enumerate(data):
            # print([Label(studentTable, text="str(i)") for i in row])
            studentTable.insert('', 'end', text=row[0], values=row[1::])
            # studentTable.insert('', 'end', values=[str(i) for i in row])
            # for ij, j in enumerate(data):
            #     studentTable.set(i, ij, str(j))
            # for j in row:
            #     studentTable.insert("", "end", values=j)

    except Exception as e:
        messagebox.showerror('Error', f'Error: {str(e)}')


def delete_student():
    indexing=studentTable.focus()
    content=studentTable.item(indexing)
    content_id=content['values'][0]
    print(f"{content_id = }")
    query='delete from student where Registration_number=%s'
    mycursor.execute(query,str(content_id))
    con.commit()
    messagebox.showinfo('Deleted',f'Registration_number {content_id} is deleted succesfully')
    query='select * from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('',END,values=data)




def search_data():
    query = (
        "select * from student "
        "where Registration_number=%s or "
        "Name=%s or Phone_number=%s or "
        "Email=%s or Branch_id=%s or Gender=%s or DOB=%s"
    )
    mycursor.execute(
        query,
        (
            Registration_numberEntry.get(),
            nameEntry.get(),
            phoneEntry.get(),
            emailEntry.get(),
            branch_idEntry.get(),
            genderEntry.get(),
            dobEntry.get() if dobEntry.get() != "" else "0001-01-01",
        ),
    )
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert("", END, values=data)





def add_data():
    if (
        Registration_numberEntry.get() == ''
        or nameEntry.get() == ''
        or emailEntry.get() == ''
        or phoneEntry.get() == ''
        or cityEntry.get() == ''
        or stateEntry.get() == ''
        or genderEntry.get() == ''
        or dobEntry.get() == ''
        or addressEntry.get() == ''
        or branch_idEntry.get() == ''
    ):
        messagebox.showerror('Error', 'All Fields are required', parent=screen)
    else:
        try:
            query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
            mycursor.execute(
                query,
                (
                    Registration_numberEntry.get(),
                    nameEntry.get(),
                    emailEntry.get(),
                    phoneEntry.get(),
                    cityEntry.get(),
                    stateEntry.get(),
                    genderEntry.get(),
                    dobEntry.get(),
                    date,
                    currenttime,
                    addressEntry.get(),
                    branch_idEntry.get(),
                ),
            )
            con.commit()
            result = messagebox.askyesno(
                'Confirm', 'Data added successfully. Do you want to clean the form?', parent=screen
            )
            if result:
                clear_form()
        except mysql.connector.IntegrityError:
            messagebox.showerror('Error', 'Registration_number cannot be repeated', parent=screen)

    fetch_and_display_data()

def clear_form():
    Registration_numberEntry.delete(0, END)
    nameEntry.delete(0, END)
    phoneEntry.delete(0, END)
    emailEntry.delete(0, END)
    addressEntry.delete(0, END)
    genderEntry.delete(0, END)
    dobEntry.delete(0, END)

def fetch_and_display_data():
    query = 'select * from student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)


# Initialize variables
count = 0
text = ''
mycursor = None
con = None
# Slider function
def slider():
    global text, count
    if count < len(s):
        text = text + s[count]
        sliderLabel.config(text=text)
        count += 1
        sliderLabel.after(300, slider)
    else:
        count = 0
        text = ''
        sliderLabel.after(300, slider)
        
        
# Clock function
def clock(): #importing clock for time
    global date,currenttime
    date=time.strftime('%d/%m/%Y')
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'   Date: {date}\nTime: {currenttime}')
    datetimeLabel.after(1000,clock)

#Connection to DB
def connect_database():
    def connect():
        global mycursor, con
        try:
            con = pymysql.connect(host=hostEntry.get(), user=usernameEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
            query = 'CREATE DATABASE IF NOT EXISTS ruas_student_management'
            mycursor.execute(query)
            query = 'Use ruas_student_management'
            mycursor.execute(query)
            query = '''
            CREATE TABLE IF NOT EXISTS student (
                Registration_number VARCHAR(50) NOT NULL PRIMARY KEY,
                Name VARCHAR(600),
                Phone_number VARCHAR(20),
                Email VARCHAR(255),
                Gender VARCHAR(10),
                DOB VARCHAR(20),
                Branch_id INT,
                Added_date VARCHAR(20),
                Added_time VARCHAR(20)
            );
            '''
            mycursor.execute(query)
            messagebox.showinfo('Success', 'Database Connection is successful', parent=connectWindow)
            connectWindow.destroy()
        except Exception as e:
            messagebox.showerror('Error', f'Error: {str(e)}', parent=connectWindow)
    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(0, 0)
    hostnameLabel = Label(connectWindow, text='Host Name', font=('arial', 20, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=20)
    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)
    usernameLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=20)
    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    usernameEntry.grid(row=1, column=1, padx=40, pady=20)
    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0, padx=20)
    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)
    connectButton = ttk.Button(connectWindow, text='CONNECT', command=connect)
    connectButton.grid(row=3, columnspan=2)   
    addstudentButton.config(state=NORMAL)
    searchstudentButton.config(state=NORMAL)
    updatestudentButton.config(state=NORMAL)
    showstudentButton.config(state=NORMAL)
    deletestudentButton.config(state=NORMAL)
 

def set_column(column_headings):
    column_count = len(column_headings)
    column_ids = [str(i) for i in range(1, column_count)]
    print(column_ids)
    studentTable["columns"] = column_ids
    column_ids.insert(0, "#0")
    for id,  heading in zip(column_ids,column_headings):
        studentTable.heading(id, text=heading)
        studentTable.column(id, minwidth=0, width=100, stretch=NO)
        
# Fetch student details from the database
def show_student_details():
    try:
        mycursor.execute('SELECT * FROM student')
        data = mycursor.fetchall()
        # print(data)

        # Clear existing data in the Treeview
        for row in studentTable.get_children():
            studentTable.delete(row)
            
        set_column(["Registration_Number", "Name", "Email", "Phone_number", 
                     "City" , "State", "Gender", "DOB","Added_date", "Added_time", "Address", "Branch_id"])
        # Insert fetched data into the Treeview
        for i, row in enumerate(data):
            # print([Label(studentTable, text="str(i)") for i in row])
            studentTable.insert('', 'end', text=row[0], values=row[1::])
            # studentTable.insert('', 'end', values=[str(i) for i in row])
            # for ij, j in enumerate(data):
            #     studentTable.set(i, ij, str(j))
            # for j in row:
            #     studentTable.insert("", "end", values=j)

    except Exception as e:
        messagebox.showerror('Error', f'Error: {str(e)}')
# Fetch branch details from the database
def show_branch_details():
    try:
        mycursor.execute('SELECT * FROM branch')
        data = mycursor.fetchall()
        #print data
    
        #Clear existing data in the treeview
        for row in studentTable.get_children():
            studentTable.delete(row)
        
        set_column(["Branch_id", "Branch_Name", "Branch_description"])
        # Insert fetched data into the Treeview
        for i, row in enumerate(data):
            # print([Label(studentTable, text="str(i)") for i in row])
            studentTable.insert('', 'end', text=row[0], values=row[1::])
            # studentTable.insert('', 'end', values=[str(i) for i in row])
            # for ij, j in enumerate(data):
            #     studentTable.set(i, ij, str(j))
            # for j in row:
            #     studentTable.insert("", "end", values=j)
    except Exception as e:
        messagebox.showerror('Error',f'Error:{str(e)}')   
# Fetch fee payments details from the database
def show_fee_payments_details():
    try:
        mycursor.execute('SELECT * FROM fee_payments')
        data = mycursor.fetchall()
        #print data
        
        #Clear existing data in the treeview
        for row in studentTable.get_children():
            studentTable.delete(row)
            
        set_column(["Payment_id", "Registration_number", "Amount","Payment_date"])
        # Insert fetched data into the Treeview
        for i, row in enumerate(data):
            # print([Label(studentTable, text="str(i)") for i in row])
            studentTable.insert('', 'end', text=row[0], values=row[1::])
            # studentTable.insert('', 'end', values=[str(i) for i in row])
            # for ij, j in enumerate(data):
            #     studentTable.set(i, ij, str(j))
            # for j in row:
            #     studentTable.insert("", "end", values=j)    
        
        
    except Exception as e:
        messagebox.showerror('Error',f'Error:{str(e)}')
# Fetch result details from the database
def show_result_details():
    try:
        mycursor.execute('SELECT * FROM results')
        data = mycursor.fetchall()
        #print data
        
        #Clear existing data in the treeview
        for row in studentTable.get_children():
            studentTable.delete(row)
            
        set_column(["Result_id", "Registration_number", "Exam_Name","Marks","Grade"])
        # Insert fetched data into the Treeview
        for i, row in enumerate(data):
            # print([Label(studentTable, text="str(i)") for i in row])
            studentTable.insert('', 'end', text=row[0], values=row[1::])
            # studentTable.insert('', 'end', values=[str(i) for i in row])
            # for ij, j in enumerate(data):
            #     studentTable.set(i, ij, str(j))
            # for j in row:
            #     studentTable.insert("", "end", values=j)      
         
    except Exception as e:
        messagebox.showerror('Error',f'Error:{str(e)}')                             
# Fetch other_info details from the database
def show_other_info_details():
    try:
        mycursor.execute('SELECT * FROM other_info')
        data = mycursor.fetchall()
        #print data
        
        #Clear existing data in the treeview
        for row in studentTable.get_children():
            studentTable.delete(row)
            
        set_column(["Scholarship_awarded", "Staying_in_hostel", "Placed_in_Company","Registration_number"])
        # Insert fetched data into the Treeview
        for i, row in enumerate(data):
            # print([Label(studentTable, text="str(i)") for i in row])
            studentTable.insert('', 'end', text=row[0], values=row[1::])
            # studentTable.insert('', 'end', values=[str(i) for i in row])
            # for ij, j in enumerate(data):
            #     studentTable.set(i, ij, str(j))
            # for j in row:
            #     studentTable.insert("", "end", values=j)      
        
    except Exception as e:
        messagebox.showerror('Error',f'Error:{str(e)}')                     

# GUI Part
root=ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('1174x680+0+0')
root.resizable(0, 0)
root.title('Student Management System')
datetimeLabel = Label(root, text='hello', font=('times new roman', 18, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s = 'Student Management System'
sliderLabel = Label(root, text=s, font=('Arial', 28, 'italic bold'), width=30)
sliderLabel.place(x=210, y=0)
slider()

connectButton = ttk.Button(root, text='Connect To Database', command=connect_database)
connectButton.place(x=987, y=0)

leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

# Correctly configure the logo_Label widget
logo_image = PhotoImage(file='university-main-logo2.png')
logo_Label = Label(leftFrame, image=logo_image)
logo_Label.grid(row=0, column=0, padx=10, pady=3)

student_details_Button = ttk.Button(leftFrame, text='Student details', width=25, command=show_student_details)
student_details_Button.grid(row=1, column=0, pady=5)

branch_details_Button = ttk.Button(leftFrame, text='Branch Details', width=25,command=show_branch_details)
branch_details_Button.grid(row=2, column=0, pady=5)

fee_payment_Button = ttk.Button(leftFrame, text='Fee Payment', width=25,command=show_fee_payments_details)
fee_payment_Button.grid(row=3, column=0, pady=5)

exam_result_Button = ttk.Button(leftFrame, text='Exam Result', width=25,command=show_result_details)
exam_result_Button.grid(row=4, column=0, pady=5)

other_info_Button = ttk.Button(leftFrame, text='Other Information', width=25,command=show_other_info_details)
other_info_Button.grid(row=5, column=0, pady=5)

addstudentButton=ttk.Button(leftFrame,text='Add Student',width=25,state=DISABLED,command=lambda:toplevel_data('Add Student','Add',add_data))
addstudentButton.grid(row=6,column=0,pady=5)

searchstudentButton=ttk.Button(leftFrame,text='Search Student',width=25,state=DISABLED,command=lambda :toplevel_data('Search Student','Search',search_data))
searchstudentButton.grid(row=7,column=0,pady=5)

deletestudentButton=ttk.Button(leftFrame,text='Delete Student',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=8,column=0,pady=5)

updatestudentButton=ttk.Button(leftFrame,text='Update Student',width=25,state=DISABLED,command=lambda :toplevel_data('Update Student','Update',update_data))
updatestudentButton.grid(row=9,column=0,pady=5)

showstudentButton=ttk.Button(leftFrame,text='Show Student',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=10,column=0,pady=5)


exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=root.destroy)
exitButton.grid(row=12, column=0, pady=5)

rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=820, height=600)

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)

studentTable=ttk.Treeview(rightFrame,columns=('Registration_Number','Name','Mobile','Email','Address','Gender',
                                 'D.O.B','Added Date','Added Time'),
                          xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)

studentTable.pack(expand=1,fill=BOTH)

root.mainloop()



