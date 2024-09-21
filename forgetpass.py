from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os
from PIL import Image , ImageTk
import mysql.connector as sqltor

root = Tk()
root.iconbitmap('logo.ico')
root.title('Grocery Managment System')
root.geometry('600x300+350+150')
# root.overrideredirect(True)
root.maxsize(width=600 , height=300)
bg = PhotoImage(file='forget pass bg.png')

def change():
    if usernameentry.get() == '' or new_password_entry =='' or confirm_new_password == '':
        messagebox.showerror('Error' , 'All Fields are Required')
    elif new_password_entry.get() != confirm_new_password.get():
        messagebox.showerror('Error' , 'Passwords do not match')
    else:
        try:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger', database='shivay_supermart')
            mycursor = main_con.cursor()
            query = 'SELECT * FROM userdata WHERE username = %s'
            mycursor.execute(query, [usernameentry.get()])
            row = mycursor.fetchone()

            if row is None:
                messagebox.showerror('Error', 'Invalid User')
            else:
                query = 'UPDATE userdata SET password = %s WHERE username = %s'
                mycursor.execute(query, [new_password_entry.get(), usernameentry.get()])
                query = 'UPDATE employee SET password = %s WHERE username = %s'
                mycursor.execute(query, [new_password_entry.get(), usernameentry.get()])
                main_con.commit()
                main_con.close()
                messagebox.showinfo('Success', 'Password Updated. Please login with the new Password')
                root.destroy()

        except sqltor.Error as e:
            print(f"Error: {e}")
            messagebox.showerror('Error', 'An error occurred. Please try again later.')

head = Label(root , image=bg)
head.pack()
usernameentry = Entry(root , width= 19 ,  font=('Microsoft Yahei UI Light' , 10 , 'bold') , bd = 0 , bg = '#f8f7da')
usernameentry.place( x = 425 , y = 128)
lineroot = Frame(root , width=150 , bg = 'black')
lineroot.place(x = 425, y = 148)

new_password_entry = Entry(root , width= 19 ,  font=('Microsoft Yahei UI Light' , 10 , 'bold') , bd = 0 , bg = '#f8f7da')
new_password_entry.place( x = 425 , y = 170 )

lineroot = Frame(root , width=150 , height=1 , bg = 'black')
lineroot.place(x = 425 , y = 190)


confirm_new_password = Entry(root , width= 19 ,  font=('Microsoft Yahei UI Light' , 10 , 'bold') , bd = 0 , bg = '#f8f7da')
confirm_new_password.place( x = 425 , y = 210 )
#
lineroot = Frame(root , width=150 , height=1 , bg = 'black')
lineroot.place(x = 425 , y = 230)

submit = Button(root , text = 'Submit' , bg = '#ff8210' , fg = 'white' , font= ('Microsoft Yahei UI Light' , 10 , 'bold') , activeforeground='white' , activebackground='#ff8210' , bd = 0 , width=10 ,  command=change)
submit.place(x = 480 , y = 250)
root.mainloop()