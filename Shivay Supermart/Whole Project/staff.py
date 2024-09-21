import datetime as dt
from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
import os
import time
from tkinter import messagebox
import time
import mysql.connector as sqltor
#
# def add():
#    if not vh_id.get() or not vh_no.get() or not vh_model.get() or not vh_capacity.get() or not vh_gpsid.get() or not vh_driver.get() or not dr_license.get() or not vh_conductor.get() or not cn_contact.get() or not mn_Date.get():
#        mb.showerror('Error', 'All Fields are required')
#
#
#    elif len(cn_contact.get()) != 10:
#        mb.showerror('Error', 'Invalid Contact number')
#
#
#    elif len(dr_license.get()) != 16:
#        mb.showerror('Error', 'Invalid License number')
#
#
#    else:
#        b = []
#        query = 'select * from vehicle where vehicle_id= %s'
#        mycursor.execute(query, [vh_id.get()])
#        row = mycursor.fetchone()
#        b.append(row)
#        if b[0]== None:
#            a = (vh_id.get(), vh_no.get(), vh_model.get(), vh_capacity.get(), vh_gpsid.get(), vh_driver.get(),dr_license.get(), vh_conductor.get(), cn_contact.get(), mn_Date.get())
#            query = "insert into Vehicle values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#            mycursor.execute(query, a)
#            main.commit()
#            tree.insert(parent='', index='end', values=(
#            vh_id.get(), vh_no.get(), vh_model.get(), vh_capacity.get(), vh_gpsid.get(), vh_driver.get(),
#            dr_license.get(), vh_conductor.get(), cn_contact.get(), mn_Date.get()))
#            mb.showinfo('Record Inserted', f'Record of {vh_id.get()} is inserted')
#            clear()
#
#
#        else:
#            mb.showerror('Error', 'Record  is already present')
#
#
#
#
# def clear():
#    for widget in fm1.winfo_children():
#        if isinstance(widget, Entry):
#            widget.delete(0, 'end')
#
#
#        if isinstance(widget, DateEntry):
#            widget.delete(0, 'end')


def delete():
    if vh_id.get() = ' '  or not vh_no.get() == '' or vh_driver.get() or not dr_license.get():
        mb.showerror(title="Error", message='PLEASE ENTER ALL THE NECESSARY DETAILS')


    else:
        aa = []
        query = "select * from vehicle where vehicle_id= %s"
        mycursor.execute(query, [vh_id.get()])
        all = mycursor.fetchone()
        for i in all :
            if i[0] == None:




        else:
            a = [vh_id.get()]
            sql = "delete from vehicle where vehicle_id= %s "
            mycursor.execute(sql, a)
            main.commit()
            mb.showinfo("Record Deleted", f" Record of {vh_id.get()} is Deleted")
