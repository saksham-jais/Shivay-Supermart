from tkinter import *
from tkinter import messagebox
import os
import mysql.connector as sqltor

root = Tk()


def forgetpass():
     os.system('forgetpass.py')



def homepage():
    if username.get()=='' or password.get() == '':
        messagebox.showerror('Error' , 'All Fields are Required!')
    else:
        try:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger')
            mycursor = main_con.cursor()
        except:
            messagebox.showerror('Error' , 'Failed to Fetch Data from Database')
            return
        query = 'use shivay_supermart'
        mycursor.execute(query)
        query = 'select * from userdata where username = %s and password = %s'
        mycursor.execute(query , (username.get() , password.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error' , 'Invalid Username or Password')
        else:
            messagebox.showinfo('Welcome' , 'Login Successful')
            usernameeee = username.get()
            query = 'select * from userdata where username = %s and password = %s'
            mycursor.execute(query , (username.get() , password.get()))
            acc = mycursor.fetchone()
            for i in acc:
                if acc[4] == 'Admin':
                    try:
                        root.destroy()
                        import homepage
                    except:
                        pass

                elif acc[4] == 'Seller':
                    try:
                        mycursor.execute('use shivay_supermart')
                        root.destroy()
                        import billing
                    except Exception as e:
                        print(f"An error occured {str(e)}")


root.iconbitmap('logo.ico')
root.title('   Grocery Management System ')

root.resizable(False,False)

root.geometry('750x600+230+50')
mainimage = PhotoImage(file = "sign in 2.png")
bg = Label(root , image=mainimage)
bg.pack()



# text = Label(root , text='USER LOGIN' , font=('Microsoft Yahei UI  Light' , 20 , 'bold') , bg = 'white' , fg = '#00008B')
# text.place(x = 465 , y = 100)
a = []
username = Entry(root ,width = 30 , font=('Microsoft Yahei UI Light' , 10 , 'bold') , bd = 0 ,  bg = '#f8f7da' ,  fg = '#eb5653')
username.place(x = 100 , y = 240)
username.insert(0 , 'Username' )
# a.append(username.get())
# print(a)
def on_click(a):
    if username.get() == 'Username':
        username.delete(0,END)
username.bind('<FocusIn>' , on_click)



lineframe = Frame(root , width=250 , height=2 , bg = '#eb5653')
lineframe.place(x = 100 , y=270 )


password =   Entry(root ,width = 30 , font=('Microsoft Yahei UI Light' , 10 , 'bold') , bd = 0 ,  bg = '#f8f7da' ,  fg = '#eb5653')
password .place(x = 100 , y = 310)
password.insert(0 , 'Password')

def on_click(a):
    if password.get() == 'Password':
        password.delete(0,END)
password.bind('<FocusIn>' , on_click)


lineframe = Frame(root , width=250 , height=2 , bg = '#eb5653')
lineframe.place(x = 100 , y = 340)

c_eye = PhotoImage(file='closeye.png')
o_eye = PhotoImage(file='openeye.png')

def hide():
    o_eye.config(file = 'closeye.png')
    password.config(show='*')
    privacybutton.config(command=show)

def show():
    o_eye.config(file='openeye.png')
    password.config(show='')
    privacybutton.config(command=hide)


privacybutton = Button(root , image = o_eye , bd = 0 , bg = '#f8f7da' , activebackground='#f8f7da' , cursor='hand2' , command=hide)

privacybutton.place(x=320 , y = 310)

fpass = Button(root , text= 'Forgot Your Password?' , bd=0 , bg='#f8f7da' , fg = '#eb5653' ,cursor='hand2' ,font=('Microsoft Yahei UI Light' , 7 , 'bold'), activebackground='#f8f7da' , activeforeground='#eb5653' , command = forgetpass)
fpass.place(x= 230 , y = 350)

login_button = Button(root, text='Login' , bg ='#eb5653' , fg='white' , font=('Open Sans' , 16 , 'bold') , activeforeground='white' , activebackground='#eb5653' , cursor='hand2' , bd=0 , width=18 , command=homepage)
login_button.place(x = 100 , y = 380)

signup_label1 = Label(root , text = 'Do not have an account ? ' , bg = '#f8f7da' , fg='#eb5653')
signup_label1.place(x = 410 , y = 510)


def signuppage():
    root.withdraw()
    os.system('signuppage.py')


signup_label2 = Button(root , text = 'Sign up Now ' , bg = '#f8f7da' , fg='blue' , cursor='hand2' , bd=0,  activeforeground='blue' , activebackground='#f8f7da' , font= ('Microsoft Yahei UI  Light' , 8 , 'bold underline'), command=signuppage)
signup_label2.place(x = 550 , y = 510)
root.mainloop()