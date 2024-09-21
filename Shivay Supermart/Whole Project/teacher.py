import os
import tkinter as tk
from tkinter import  ttk
import tkinter.messagebox as mb
# import datetime
# from tkcalendar import DateEntry
import mysql.connector as sq


m= tk.Tk()
m.geometry("1366x768")
m.title("HOME PAGE")
m.resizable(0,0)




def dash():
    main()




def stud():
    img = tk.PhotoImage(file= "Untitled design.png")
    a = tk.Label(m, image= img).place(x=510, y=10, height=726, width=835)
    # a= tk.Frame(m, bg= "cyan").place(x= 510, y= 10, height= 726, width= 835)


def main():
    main = sq.connect(host='localhost', user='root', password='tiger', database="shivansh")
    myc1 = main.cursor()

    def btn1_click():
        a = []
        b = []
        query = 'select count(*) from userdata'
        myc1.execute(query)
        all = myc1.fetchone()
        a.append(all)
        # print(a)
        for i in a:
            b.append(i[0])
        # print(b)
        # bt.config(text=b)
        if btn1['text'] == "Total Students":
            btn1.config(text=f"Total Student:- {b[0]}")
            btn1.place(x=660, y=280)
        else:
            btn1.config(text="Total Students")
            btn1.place(x=680, y=280)



    def btn2_click():
        a = []
        b = []
        query = 'select count(*) from tdetails'
        myc1 = main.cursor()
        myc1.execute(query)
        all = myc1.fetchone()
        a.append(all)
        # print(a)
        for i in a:
            b.append(i[0])

        if btn2['text'] == "Total Teachers":
            btn2.config(text=f"Total Teacher:- {b[0]}")
            btn2.place(x=992, y=280)
        else:
            btn2.config(text="Total Teachers")
            btn2.place(x=1015, y=280)
        # print(b)
        # bt.config(text=b)
        # if btn2['text'] == "Total Teachers":
        #     btn2.config(text=f"Total Teachers:- {b[0]}")
        #     btn2.place(x=992, y=280)
        # else:
        #     btn2.config(text="Total Teachers")
        #     btn2.place(x=1015, y=280)
    img = tk.PhotoImage(file='ABC PUBLIC (1) (1).png')
    lb = tk.Label(m, image=img).place(x=0, y=0, relheight=1, relwidth=1)

    btn1 = tk.Button(text="Total Students", bg="#FFDA00", bd=0, font=("Arial", 18, "bold"),
                    activebackground="#FFDA00", command= btn1_click)
    btn1.place(x=680, y=280)
    btn2 = tk.Button(text="Total Teachers", bg="#FFDA00", bd=0, font=("Arial", 18, "bold"),
                     activebackground="#FFDA00", command= btn2_click)
    btn2.place(x=1015, y=280)
    btn3 = tk.Button(text="Total Staffs", bg="#FFDA00", bd=0, font=("Arial", 18, "bold"),
                     activebackground="#FFDA00")
    btn3.place(x=690, y=570)
    btn4= tk.Button(text="----------------", bg="#FFDA00", bd=0, font=("Arial", 18, "bold"),
                     activebackground="#FFDA00")
    btn4.place(x=1020, y=570)

    tk.Button(m, text="> Dashboard", bg="#A6D0EB", font=("Arial", 24, "bold"), bd=0, activebackground="#A6D0EB", command= dash).place(
        x=60, y=150)
    tk.Button(m, text="> Students", bg="#A6D0EB", font=("Arial", 24, "bold"), bd=0, activebackground="#A6D0EB",
              command=stud).place(x=60, y=200)
    tk.Button(m, text="> Teachers", bg="#A6D0EB", font=("Arial", 24, "bold"), bd=0, activebackground="#A6D0EB").place(
        x=60, y=250)
    tk.Button(m, text="> Staffs", bg="#A6D0EB", font=("Arial", 24, "bold"), bd=0, activebackground="#A6D0EB").place(
        x=60, y=300)
    tk.Button(m, text="> Academics", bg="#A6D0EB", font=("Arial", 24, "bold"), bd=0, activebackground="#A6D0EB").place(
        x=60, y=350)
    tk.Button(m, text="> Fees Structure", bg="#A6D0EB", font=("Arial", 24, "bold"), bd=0,
              activebackground="#A6D0EB").place(x=60, y=400)
    tk.Button(m, text="> Log Out", bg="#A6D0EB", font=("Arial", 24, "bold"), bd=0, activebackground="#A6D0EB").place(
        x=60, y=450)

    m.mainloop()


main()




