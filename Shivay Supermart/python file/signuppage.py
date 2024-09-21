import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as sqltor
import os

root = Tk()
root.iconbitmap('logo.ico')
root.title('   Grocery Management System ')


def clear():
     button1.delete(0,END)
     button2.delete(0,END)
     button3.delete(0,END)
     button4.delete(0,END)


def clear():
     button1.delete(0, END)
     button2.delete(0, END)
     button3.delete(0, END)
     button4.delete(0, END)
     try:
          root.destroy()
          os.system('signinpage.py')
     except:
          pass



def error():
     if button1.get()=='' or button2.get()=='' or button3.get()=='' or button4.get()=='':
          messagebox.showerror('Error' , 'All Fields are Required')
     elif button3.get() != button4.get():
          messagebox.showerror('Error' , 'Passwords do not match')
     elif a.get()==0:
          messagebox.showerror('Error' , 'Please accept Terms and Conditions')
     elif account_type_button.get() == '':
          messagebox.showerror('Error' , 'Please Select Account Type')

     else:
          try:
               main_con = sqltor.connect(host = 'localhost' , user = 'root' , password = 'tiger')
               mycursor = main_con.cursor()
          except:
               messagebox.showerror('Error' , 'Database Connectivity Failed ! Please Try Again')
               return

          try:
               query = 'create database shivay_supermart'
               mycursor.execute(query)
               query = 'use shivay_supermart'
               mycursor.execute(query)
               query = 'create table userdata(id int auto_increment primary key not null , email varchar(50) ,username varchar(100) , password varchar(50) , account_type varchar(20))'
               mycursor.execute(query)
          except:
               query = 'use shivay_supermart'
               mycursor.execute(query)
          query = 'select * from userdata where username = %s'
          mycursor.execute(query , [button2.get()])

          row = mycursor.fetchone()
          if row != None:
               messagebox.showerror('Error', 'Username Already exists')
          else:

               aloo = random.randint(300, 900)
               query = 'insert into userdata(email , username , password , account_type ) values (%s,%s,%s,%s)'
               mycursor.execute(query,(button1.get() , button2.get() , button3.get() , account_type_button.get()))

               query = 'insert into employee(employeeID , email , username , password , Jobtitle , dateofbirth , Hiredate) values (%s, %s, %s ,%s,%s,%s,%s)'
               mycursor.execute(query, [aloo, button1.get(), button2.get(), button3.get(), account_type_button.get() , '2024-01-01' , '2024-01-01'])

               main_con.commit()
               main_con.close()
               messagebox.showinfo('Success' , 'Registration Successful')
               clear()




def loginpage():
     root.withdraw()
     os.system('signinpage.py')

root.resizable(False,False)
root.geometry('750x600+230+50')
root.maxsize(width=750,height=600)
image = PhotoImage(file="sign up 2.png")
bg_image = Label(root, image=image)
bg_image.pack()

label1 = Label(root, text='Email :' , bg = '#f8f7da' , fg= '#eb5653' , font= ('Microsoft Yahei UI  Light' , 13 , 'bold'))
label1.place(x = 100 , y = 145)

button1 = Entry(root , width = 45 , bg = '#eb5653' , fg = '#f8f7da' )
button1.place(x=100 , y = 175)


label2 = Label(root, text='Username :' , bg = '#f8f7da' , fg= '#eb5653' , font= ('Microsoft Yahei UI  Light' , 13, 'bold'))
label2.place(x = 100 , y = 205)

button2 = Entry(root , width = 45 , bg = '#eb5653' , fg = '#f8f7da' )
button2.place(x=100 , y = 235)

label3 = Label(root, text='Password : ' , bg = '#f8f7da' , fg= '#eb5653' , font= ('Microsoft Yahei UI  Light' , 13, 'bold'))
label3.place(x = 100 , y = 265)

button3 = Entry(root , width = 45 , bg = '#eb5653' , fg = '#f8f7da' )
button3.place(x=100 , y = 295)

label4 = Label(root, text='Confirm Password :' , bg = '#f8f7da' , fg= '#eb5653' , font= ('Microsoft Yahei UI  Light' , 13, 'bold'))
label4.place(x = 100 , y = 325)

button4 = Entry(root , width = 45 , bg = '#eb5653' , fg = '#f8f7da' )
button4.place(x=100 , y = 355)

account_type = Label(root , text='Account Type : ' , bg = '#f8f7da' , fg= '#eb5653' , font= ('Microsoft Yahei UI  Light' , 13, 'bold'))
account_type.place(x=100 , y = 385)
list = ['Admin' , 'Seller']
n = IntVar()
account_type_button = ttk.Combobox(root , textvariable=n  , values=list , state='readonly')
account_type_button.set('Admin')
account_type_button.place(x = 235 , y = 391)


a = IntVar()
checkbutton = Checkbutton(root , text='I agree to the Terms and Condition' , bg = '#f8f7da' , fg= '#eb5653' , font= ('Microsoft Yahei UI  Light' , 12, 'bold') , activebackground='#f8f7da' , activeforeground='#eb5653' , cursor='hand2' , variable=a)
checkbutton.place(x= 95 , y = 442)

signup_button = Button(root , text='SignUp' , width=13 , bg = '#eb5653' , fg= '#f8f7da' , font=('Open Sans' , 16 , 'bold') , activeforeground='#f8f7da' , activebackground='#eb5653' , command=error)
signup_button.place(x= 150 , y = 475 )


lastline1 = Label(root , text='Already Signed Up ? ' , bg = '#f8f7da' , fg= '#eb5653' , font= ('Microsoft Yahei UI  Light' , 8 , 'bold') , activebackground='#f8f7da' , activeforeground='#eb5653')
lastline1.place(x = 445 , y = 505)


lastline2 = Button(root , text='Log In Now '  , bg = '#f8f7da' , fg= 'blue' , cursor='hand2' , font= ('Microsoft Yahei UI  Light' , 8 , 'bold underline') , activebackground='#f8f7da' , activeforeground='blue' , bd=0 , command=loginpage)
lastline2.place(x = 565 , y = 505 )


root.mainloop()