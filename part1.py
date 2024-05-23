from tkinter import *
from PIL import Image, ImageTk
import pymysql
from tkinter import messagebox


#Functionality Part
def login_user():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error','All fiels are required')
    else:
        try:
            con = pymysql.connect(host='localhost',user='root',password='Akshi')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection not established try again')
            return
        query='Use userdata'
        mycursor.execute(query)
        query='Select * from data where username = %s and password = %s'
        mycursor.execute(query,(usernameEntry.get(),passwordEntry.get()))
        row=mycursor.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome','Login is successful') 
            login_window.destroy()
            import part3
def hide():
    openeye.config(file='closeye (1).png')
    passwordEntry.config(show='*')
    eyeButton.config(command=show)
    
def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyeButton.config(command=hide)
    
def user_enter(event):
    if usernameEntry.get() == 'Username':
        usernameEntry.delete(0, END)
        
def password_enter(event):
    if passwordEntry.get() == 'Password':
        passwordEntry.delete(0, END)
        
login_window = Tk()
login_window.geometry('790x512+50+50')
login_window.resizable(0, 0)
login_window.title('Login Page')
bgImage = ImageTk.PhotoImage(file="1.jpg")
bgLabel = Label(login_window, image=bgImage)
bgLabel.place(x=0, y=0)
heading = Label(login_window, text='USER LOGIN', font=('Microsoft Yahei UI Light', 23, 'bold'),
                bg='white', fg='firebrick1')
heading.place(x=506, y=88)
usernameEntry = Entry(login_window, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1')
usernameEntry.place(x=488, y=172)
usernameEntry.insert(0, 'Username')
usernameEntry.bind('<FocusIn>', user_enter)
frame1 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame1.place(x=488, y=200)
passwordEntry = Entry(login_window, width=15, font=('Microsoft Yahei UI Light', 15, 'bold'), bd=0, fg='firebrick1', show='*')
passwordEntry.place(x=488, y=235)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', password_enter)
frame2 = Frame(login_window, width=250, height=2, bg='firebrick1')
frame2.place(x=488, y=263)
openeye = ImageTk.PhotoImage(file="openeye.png")
eyeButton = Button(login_window, image=openeye, bd=0, bg='white', activebackground='white', cursor='hand2',
                   command=hide)
eyeButton.place(x=708, y=236)
forgetButton = Button(login_window, text='Forgot Password?', bd=0, bg='white', activebackground='white', cursor='hand2'
                      ,font=('Microsoft Yahei UI Light', 7, 'bold'),fg='firebrick1',activeforeground='firebrick1')
forgetButton.place(x=646, y=270)
loginButton=Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',
                   bg='firebrick1',activeforeground='white',activebackground='firebrick1',cursor='hand2'
                   ,bd=0,width=19,command=login_user)
loginButton.place(x=486,y=300)
orLabel=Label(login_window,text='---------------OR-----------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=482,y=345)
facebook_logo=PhotoImage(file='facebook.png')
fbLabel=Label(login_window,image=facebook_logo,bg='white')
fbLabel.place(x=625,y=380)
google_logo=PhotoImage(file='google.png')
googleLabel=Label(login_window,image=google_logo,bg='white')
googleLabel.place(x=551,y=382)
twitter_logo=PhotoImage(file='twitter.png')
twitterLabel=Label(login_window,image=twitter_logo,bg='white')
twitterLabel.place(x=588,y=382)
signupLabel=Label(login_window,text="Don't have a account? Contact Administrator!",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signupLabel.place(x=478,y=436)
college_logo_path = 'university-main-logo.png'
college_img = Image.open(college_logo_path)
college_img = college_img.resize((390, 148))  # Replace 20 and 20 with your desired dimensions
resized_college_logo = ImageTk.PhotoImage(college_img)
collegeLabel = Label(login_window, image=resized_college_logo,bg='white')
collegeLabel.place(x=20, y=20)
login_window.mainloop()