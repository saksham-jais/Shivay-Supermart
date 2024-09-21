import datetime as dt
from tkinter import *
from tkinter import ttk
from PIL import Image ,ImageTk
from tkinter import filedialog
import os
import time
from tkinter import messagebox
import time
import mysql.connector as sqltor
from tkcalendar import DateEntry
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random
import string
import tempfile
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.base import MIMEBase
from email import encoders
import mimetypes


root = Tk()
global canvas

style = ttk.Style()
style.theme_use('clam')

main_con = sqltor.connect(host='localhost', user='root', password='tiger')
mycursor = main_con.cursor()

mycursor.execute('use shivay_supermart')
query = 'select distinct category_name from product_category'
mycursor.execute(query)
row = mycursor.fetchall()
values_list = [value[0] for value in row]


def dashboard():
    for widget in root.winfo_children():
        if isinstance(widget, Frame):
            widget.destroy()

def products():

    def add():
        if category.get() == 'Select' or sub_head0_entry.get() == ''   or sub_head2_entry.get() == '' or sub_head3_entry.get() == '' or   sub_head4_entry.get() =='' or sub_head5_entry.get() == '' or  status_category.get()=='Select' :
            messagebox.showerror('Error' , 'All Fields are Required')
        else:
            try:
                main_con = sqltor.connect(host='localhost', user='root', password='tiger')
                mycursor = main_con.cursor()
            except:
                messagebox.showerror('Error', 'Failed to add data')
                return



            query = 'use shivay_supermart'
            mycursor.execute(query)
            query = 'select product_ID from products'
            mycursor.execute(query)
            row = mycursor.fetchall()
            jaishreeram = [value[0] for value in row]
            if sub_head0_entry.get() in jaishreeram :
                messagebox.showerror('Error' , 'Product ID Exist')

            else:
                query = 'insert into products (Product_ID  , Category,  Product_Company , Product_Name , Price , quantity , product_Status) values (%s , %s , %s, %s, %s , %s ,%s )'
                mycursor.execute(query, (
                    sub_head0_entry.get(), category.get() , sub_head2_entry.get(), sub_head3_entry.get(),
                    sub_head4_entry.get(), sub_head5_entry.get(), status_category.get()))

                query = 'update product_category set total_products = total_products+1 where category_name = %s'

                mycursor.execute(query , [category.get()])
                main_con.commit()
                messagebox.showinfo('Success', 'Product Added')
                tree.insert(parent='', index='end', values=(
                    sub_head0_entry.get(), category.get(), sub_head2_entry.get(), sub_head3_entry.get(),
                    sub_head4_entry.get(), sub_head5_entry.get(), status_category.get()))
                main_con.close()



    def update():
        list = [sub_head0_entry.get(), category.get(), sub_head2_entry.get(), sub_head3_entry.get(), sub_head4_entry.get(),
         sub_head5_entry.get(), status_category.get(), sub_head0_entry.get()]

        if category.get() == 'Select' or sub_head0_entry.get() == ''   or sub_head2_entry.get() == '' or sub_head3_entry.get() == '' or   sub_head4_entry.get() =='' or sub_head5_entry.get() == '' or  status_category.get()=='Select' :
            messagebox.showerror('Error' , 'Please Select Product to Update')
        else:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger')
            mycursor = main_con.cursor()
            query = 'use shivay_supermart'
            mycursor.execute(query)

            query = ' select * from products where Product_ID = %s '
            mycursor.execute(query , [sub_head0_entry.get()])
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error' , "Invalid Product! Product ID Exist")
                return
            else:
                 query = 'update products set Product_ID= %s  , category= %s ,  product_company= %s  , product_name = %s , price= %s  , quantity = %s ,product_status = %s where product_ID = %s'
                 mycursor.execute(query , list)
                 main_con.commit()

                 for item in tree.get_children():
                     tree.delete(item)

                 query = 'select * from products'
                 mycursor.execute(query)
                 all = mycursor.fetchall()
                 for val in all:
                     tree.insert(parent='', index='end', values=val)

                 messagebox.showinfo('Updated', f'Product {sub_head0_entry.get()} is modified')

    def clear():
        if category.get() == 'Select' and sub_head0_entry.get() == '' and sub_head2_entry.get() == '' and sub_head3_entry.get() == '' and sub_head4_entry.get() == '' and sub_head5_entry.get() == '' and sub_head6_entry.get() == '' and status_category.get() == 'Select':
            pass
        else:
            category.set('Select')
            sub_head0_entry.delete(0,END)
            sub_head2_entry.delete(0,END)
            sub_head3_entry.delete(0,END)
            sub_head4_entry.delete(0,END)
            sub_head5_entry.delete(0,END)
            status_category.set('Select')


    def delete():

        if category.get() == 'Select' or sub_head0_entry.get() == '' or sub_head2_entry.get() == '' or sub_head3_entry.get() == '' or sub_head4_entry.get() == '' or sub_head5_entry.get() == '' or status_category.get() == 'Select':
            messagebox.showerror('Error' , 'Please select Product to Delete')
        else:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger')
            mycursor = main_con.cursor()
            query = 'use shivay_supermart'
            mycursor.execute(query)

            query = ' select * from products where Product_ID = %s '
            mycursor.execute(query, [sub_head0_entry.get()])
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', "No Product Found")
                return
            else:
                query = 'delete from products where product_ID = %s'
                mycursor.execute(query, [sub_head0_entry.get()])
                query = 'update product_category set total_products = total_products - 1 where category_name = %s'
                mycursor.execute(query, [category.get()])
                main_con.commit()

                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from products'
                mycursor.execute(query)
                all = mycursor.fetchall()
                for val in all:
                    tree.insert(parent='', index='end', values=val)

                messagebox.showinfo('Deleted', f'Product {sub_head0_entry.get()} is Deleted')


    a = Frame(root, bg="#ff8210" ,  height=726, width=950)
    a.place(x=350,y=0)
    head = Frame(a , bg = 'black' , width=1400, height=90 )
    head.place(x=0,y=0)
    head_label = Label(a , text = 'Manage Products' , fg = 'white' , bg = 'black' , font= ('goudy old style' , 40 , 'bold'))
    head_label.place(x=290 , y = 10)


    details_frame = Frame(a , bg = '#FFFDD8' , width = 320 , height = 520 , highlightthickness=2 , highlightbackground='black')
    details_frame.place(x = 8 , y = 130)

    sub_head0 = Label(details_frame, text='Product ID   : ', bg='#FFFDD8', fg='black', font=('Arial', 13, 'bold'))
    sub_head0.place(x=20, y=110)
    sub_head0_entry = Entry(details_frame, width=16, bg='#FFFDD8', fg='black', bd=0, font=('Arial', 12, 'bold'))
    sub_head0_entry.place(x=140, y=110)
    sub_head0_entry_line = Frame(details_frame, bg='black', width=140, height=2)
    sub_head0_entry_line.place(x=140, y=128)


    sub_head1 = Label(details_frame , text='Category      :' , bg = '#FFFDD8' , fg = 'black' , font=('Arial' , 13 , 'bold') )
    sub_head1.place(x=20 , y=23)
    category = ttk.Combobox(details_frame  ,state='readonly' ,width = 22 , height =1)
    category.config(values = values_list)
    category.place(x = 135 , y = 25)
    category.set('Select')


    sub_head2 = Label(details_frame , text='Company     : ' , bg = '#FFFDD8' , fg = 'black' ,font=('Arial' , 13 , 'bold'))
    sub_head2.place(x = 20 , y = 160)
    sub_head2_entry = Entry(details_frame , width = 16 , bg = '#FFFDD8' , fg = 'black' , bd = 0 , font=('Arial' , 12 , 'bold'))
    sub_head2_entry.place(x = 140 , y = 160)
    sub_head2_entry_line = Frame(details_frame ,bg = 'black', width = 140 , height = 2)
    sub_head2_entry_line.place(x = 140 , y = 178)


    sub_head3 = Label(details_frame , text = 'Name           : ' ,bg = '#FFFDD8' , fg = 'black' ,font=('Arial' , 13 , 'bold'))
    sub_head3.place(x = 20 , y = 210)
    sub_head3_entry = Entry(details_frame, width=16, bg='#FFFDD8', fg='black', bd=0, font=('Arial', 12, 'bold'))
    sub_head3_entry.place(x=140, y=210)
    sub_head3_entry_line = Frame(details_frame, bg='black', width=140, height=2)
    sub_head3_entry_line.place(x=140, y=228)
    sub_head4 = Label(details_frame, text='Price           : ' , bg='#FFFDD8', fg='black', font=('Arial', 13, 'bold'))
    sub_head4.place(x=20, y=260)
    sub_head4_entry = Entry(details_frame, width=16, bg='#FFFDD8', fg='black', bd=0, font=('Arial', 12, 'bold' ))
    sub_head4_entry.place(x=140, y=260)
    sub_head4_entry_line = Frame(details_frame, bg='black', width=140, height=2)
    sub_head4_entry_line.place(x=140, y=278)

    sub_head5 = Label(details_frame, text='Quantity      : ',  bg='#FFFDD8', fg='black', font=('Arial', 13, 'bold'))
    sub_head5.place(x=20, y=310)
    sub_head5_entry = Entry(details_frame, width=16, bg='#FFFDD8', fg='black', bd=0, font=('Arial', 12, 'bold'))
    sub_head5_entry.place(x=140, y=310)
    sub_head5_entry_line = Frame(details_frame, bg='black', width=140, height=2)
    sub_head5_entry_line.place(x=140, y=328)

    sub_head6 = Label(details_frame, text='Status         : ', bg='#FFFDD8', fg='black', font=('Arial', 13, 'bold'))
    sub_head6.place(x=20, y=350)
    status = ['Available' , 'Not Available']
    status_category = ttk.Combobox(details_frame, values=status, state='readonly', width=25)
    status_category.place(x=135, y=350)
    status_category.set('Select')

    sub_head_button_1_frame = Frame(details_frame , bg = 'black' , width = 112, height = 35)
    sub_head_button_1_frame.place(x = 30 , y = 427)
    sub_head_button_1 = Button(details_frame , text='Add' , bg='red', fg='black', font=('Arial', 13, 'bold') , activebackground='red' , activeforeground='black',width = 10 , bd =0 , command=add )
    sub_head_button_1.place(x=33 , y = 430)

    sub_head_button_2_frame = Frame(details_frame, bg='black', width=112, height=35)
    sub_head_button_2_frame.place(x=167, y=427)
    sub_head_button_2 = Button(details_frame, text='Update', bg='Yellow', fg='black', font=('Arial', 13, 'bold'),activebackground='Yellow', activeforeground='black', width=10 , bd=0 , command = update)
    sub_head_button_2.place(x=170, y=430)

    sub_head_button_3_frame = Frame(details_frame, bg='black', width=112, height=35)
    sub_head_button_3_frame.place(x=30, y=472)
    sub_head_button_3 = Button(details_frame, text='Clear', bg= 'light green', fg='black', font=('Arial', 13, 'bold'),activebackground='light Green', activeforeground='black', width=10, bd=0  , command = clear)
    sub_head_button_3.place(x=33, y=475)

    sub_head_button_4_frame = Frame(details_frame, bg='black', width=112, height=35)
    sub_head_button_4_frame.place(x=167, y=472)
    sub_head_button_4 = Button(details_frame, text='Delete', bg='cyan', fg='black', font=('Arial', 13, 'bold'),activebackground='cyan', activeforeground='black', width=10, bd=0 , command=delete)
    sub_head_button_4.place(x=170, y=475)


    def search(a):
        try:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger')
            mycursor = main_con.cursor()
            query = 'use shivay_supermart'
            mycursor.execute(query)
            query = "select * from products where product_name LIKE '%"+var_search.get()+"%'"
            mycursor.execute(query)
            row = mycursor.fetchall()
            if len(row) > 0:
                tree.delete(*tree.get_children())
                for i in row:
                    tree.insert('',END,values=i)
            else:
                tree.delete(*tree.get_children())

        except :
            messagebox.showerror('Error', "Error")


    def on_click(a):
        if search_entry.get() == '   Search by Product Name':
                search_entry.delete(0, END)

    var_search = StringVar()
    search_entry = Entry(a , width = 23 , font = ('poppins', 9  ) ,textvariable=var_search,  bg = 'white' , fg = 'black')
    search_entry.place(x = 730 , y = 110)
    search_entry.insert(0, '   Search by Product Name')
    search_entry.bind("<Key>" , search)
    search_entry.bind('<FocusIn>', on_click)

    treeview_frame = Frame(a, bg='#FFFDD8', highlightthickness=2,
                           highlightbackground='black')  # , width=570, height=510,
    treeview_frame.place(x=340, y=135, width=570, height=510)
    col = ['Product_ID', 'Product_Category' , 'Product_Company', 'Product_Name', 'Price', 'Quantity', 'Product_Status']

    tree = ttk.Treeview(treeview_frame, columns=col, selectmode=BROWSE, height=100)

    xscroll = ttk.Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    yscroll = ttk.Scrollbar(tree, orient=VERTICAL, command=tree.yview)

    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)


    tree.heading('Product_ID', text='Product ID', anchor=CENTER)
    tree.heading('Product_Category' , text = 'Product Category' , anchor=CENTER)
    tree.heading('Product_Company', text='Comapny', anchor=CENTER)
    tree.heading('Product_Name', text='Name', anchor=CENTER)
    tree.heading('Price', text='Price', anchor=CENTER)
    tree.heading('Quantity', text='Quantity', anchor=CENTER)
    tree.heading('Product_Status', text='Status', anchor=CENTER)

    tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

    tree.column('#0', width=0 , minwidth=0)
    tree.column('Product_ID', width=100 , minwidth=100 , anchor=CENTER)#
    tree.column('Product_Category', width=150 , minwidth=150 , anchor=CENTER)#
    tree.column('Product_Company', width=140 , minwidth=140, anchor=CENTER)  # product company
    tree.column('Product_Name', width=140 , minwidth=140, anchor=CENTER)  # product name
    tree.column('Price', width=80 , minwidth=80, anchor=CENTER)  # price
    tree.column('Quantity', width=80 , minwidth=80, anchor=CENTER)  # quantity
    tree.column('Product_Status', width=140 , minwidth=140, anchor=CENTER)  # product status

    def selected_item_clear():

        category.set('Select')
        sub_head0_entry.delete(0, END)
        sub_head2_entry.delete(0, END)
        sub_head3_entry.delete(0, END)
        sub_head4_entry.delete(0, END)
        sub_head5_entry.delete(0, END)
        status_category.set('Select')



    def display_selected_item(a):
        selected_item_clear()
        selecteditem = tree.selection()
        sub_head0_entry.insert(0, tree.item(selecteditem)['values'][0])
        category.set(tree.item(selecteditem)['values'][1])
        sub_head2_entry.insert(0, tree.item(selecteditem)['values'][2])
        sub_head3_entry.insert(0, tree.item(selecteditem)['values'][3])
        sub_head4_entry.insert(0, tree.item(selecteditem)['values'][4])
        sub_head5_entry.insert(0, tree.item(selecteditem)['values'][5])
        status_category.set(tree.item(selecteditem)['values'][6])


    tree.bind("<<TreeviewSelect>>", display_selected_item)

    main_con = sqltor.connect(host='localhost', user='root', password='tiger')
    mycursor = main_con.cursor()
    query = 'use shivay_supermart'
    mycursor.execute(query)
    query2 = 'select Product_ID , Category ,  Product_Company , Product_Name , Price , Quantity , Product_Status  from products'
    mycursor.execute(query2)
    row = mycursor.fetchall()
    for rows in row:
        tree.insert("", "end", values=rows)

def Products_Categories():

    a = Frame(root, bg="#FF30AC", height=726, width=950)
    a.place(x=350, y=0)

    head = Frame(a, bg='black', width=1400, height=90)
    head.place(x=0, y=0)
    label = Label(a, text='Manage Categories', bg='black', fg='white', font=('goudy old style', 40, 'bold'))
    label.place(x=250, y=10)

    treeview_frame = Frame(a, bg='#FFFDD8', highlightthickness=2,
                           highlightbackground='black')  # , width=570, height=510,
    treeview_frame.place(x=30, y=100, width=860, height=310)

    col = ['Serial_Number' , 'Product_Category' , 'Total_Products' , 'Description']

    tree = ttk.Treeview(treeview_frame, columns=col, selectmode=BROWSE, height=100)

    xscroll = ttk.Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    yscroll = ttk.Scrollbar(tree, orient=VERTICAL, command=tree.yview)

    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

    tree.heading('Serial_Number', text='S. No.', anchor=CENTER)
    tree.heading('Product_Category', text='Product Category', anchor=CENTER)
    tree.heading('Total_Products', text='Total Products', anchor=CENTER)
    tree.heading('Description', text='Description', anchor=CENTER)

    tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

    tree.column('#0', width=0, minwidth=0)
    tree.column('Serial_Number', width=100, minwidth=100, anchor=CENTER)
    tree.column('Product_Category', width=250, minwidth=250, anchor=CENTER)
    tree.column('Total_Products', width=150, minwidth=150, anchor=CENTER)
    tree.column('Description', width=2000, minwidth=2000, anchor=W)

    query = "use shivay_supermart"
    mycursor.execute(query)
    query = 'select * from product_category'
    mycursor.execute(query)
    row = mycursor.fetchall()
    for values in row:
        tree.insert('',END,values=values)

    category_frame = Frame(a, bg='#FFFFCC', highlightthickness=2,
                           highlightbackground='black')  # , width=570, height=510,
    category_frame.place(x=30, y=420, width=860, height=250)

    label = Label(category_frame , text = 'Add Category' , bg = 'black', width=100,fg = 'white' , font=('Helvetica',11 , 'bold'))
    label.place(x = 0 , y = 0)

    def ad():
        if text0entry.get()=='' or text1entry.get() == ''  :
            messagebox.showerror('Error' , 'All Fields are required')
        else:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger')
            mycursor = main_con.cursor()
            query = 'use shivay_supermart'
            mycursor.execute(query)
            query = 'select serial_number from product_category'
            mycursor.execute(query)
            row = mycursor.fetchall()
            jaishreeram = [value[0] for value in row]
            if text0entry.get() in jaishreeram:
                messagebox.showerror('Error', 'Serial Number Exist')
            else :
                query = 'insert into product_category (serial_number , category_name , total_products , description) values (%s , %s , %s, %s)'
                mycursor.execute(query, (
                text0entry.get(), text1entry.get(), text2entry.get(), text3entry.get()))
                main_con.commit()
                values_list.append(text1entry.get())
                messagebox.showinfo('Success', 'Category Added')

                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from product_category'
                mycursor.execute(query)
                row = mycursor.fetchall()
                for i in row:
                    tree.insert(parent='', index='end', values=i)
                main_con.close()

    def selected_item_clear():

        text0entry.delete(0,END)
        text1entry.delete(0,END)
        text2entry.delete(0,END)
        text3entry.delete(0,END)

    def display_selected_item(a):
        selected_item_clear()
        selecteditem = tree.selection()[0]
        text0entry.insert(0, tree.item(selecteditem)['values'][0])
        text1entry.insert(0, tree.item(selecteditem)['values'][1])
        text2entry.insert(0, tree.item(selecteditem)['values'][2])
        text3entry.insert(0, tree.item(selecteditem)['values'][3])

    tree.bind("<<TreeviewSelect>>", display_selected_item)

    def modify():
        list = [text1entry.get(), text2entry.get(), text3entry.get(), text0entry.get()]

        if text1entry.get() =='' or text0entry.get()=='' or text2entry.get()=='' :
            messagebox.showerror('Error', 'Please Select Product to Update')
        else:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger')
            mycursor = main_con.cursor()
            query = 'use shivay_supermart'
            mycursor.execute(query)

            query = ' select * from product_category where serial_number = %s '
            mycursor.execute(query, [text0entry.get()])
            row = mycursor.fetchone()
            if row == None:
                messagebox.showerror('Error', "Invalid Product! Product ID Exist")
                return
            else:
                query = 'update product_category set category_name = %s, total_products = %s , description = %s where serial_number = %s'
                mycursor.execute(query, list)
                main_con.commit()

                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from product_category'
                mycursor.execute(query)
                all = mycursor.fetchall()
                for val in all:
                    tree.insert(parent='', index='end', values=val)

                messagebox.showinfo('Modified', f'Product {text0entry.get()} is modified')


    text0 = Label(category_frame, text='Serial Number', fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'))
    text0.place(x=40, y=50)
    textcolon = Label(category_frame, text=':', fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'))
    textcolon.place(x=170, y=47)
    text0entry = Entry(category_frame, width=20, fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'), bd=0)
    text0entry.place(x=200, y=50)
    text0entryline = Frame(category_frame, bg='black', width=200)
    text0entryline.place(x=200, y=75)

    text1 = Label(category_frame , text='Category' , fg = 'black' , bg = '#FFFFCC' , font = ('Calibri' , 15, 'bold'))
    text1.place(x = 40 , y = 90)
    textcolon = Label(category_frame , text=':' , fg = 'black' , bg = '#FFFFCC' , font = ('Calibri' , 15, 'bold'))
    textcolon.place(x=140 , y = 87)
    text1entry = Entry(category_frame , width=20 , fg = 'black' , bg = '#FFFFCC' , font = ('Calibri' , 15, 'bold'), bd = 0)
    text1entry.place(x = 170 , y = 90)
    text1entryline = Frame(category_frame, bg = 'black' , width = 200)
    text1entryline.place(x = 170 , y = 115)

    text2 = Label(category_frame, text='Total Products', fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'))
    text2.place(x=400, y=90)
    textcolon = Label(category_frame, text=':', fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'))
    textcolon.place(x=560, y=87)
    text2entry = Entry(category_frame, width=20, fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'), bd=0)
    text2entry.place(x=590, y=90)
    text2entryline = Frame(category_frame, bg='black', width=200)
    text2entryline.place(x=590, y=115)

    text3 = Label(category_frame, text='Description', fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'))
    text3.place(x=40, y=130)
    textcolon = Label(category_frame, text=':', fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'))
    textcolon.place(x=140, y=127)
    text3entry = Entry(category_frame, width=60 ,fg='black', bg='#FFFFCC', font=('Calibri', 15, 'bold'), bd=0)
    text3entry.place(x=170, y=130)
    text3entryline = Frame(category_frame, bg='black', width=600)
    text3entryline.place(x=170, y=155)

    frame1 = Frame(category_frame, bg='black', width=93, height=37)
    frame1.place(x=290, y=190)
    button1 = Button(category_frame, text='Add', width=10, background='#FF4040', activebackground='#FF1818', bd=0,foreground='black', activeforeground='black', font=('Calibri', 12, 'bold'), command = ad)
    button1.place(x=293, y=194)

    frame2 = Frame(category_frame, bg='black', width=93, height=37)
    frame2.place(x=395, y=190)
    button2 = Button(category_frame, text='Modify', width=10, background='#67E0F8', activebackground='#3FD9F8', bd=0,foreground='black', activeforeground='black', font=('Calibri', 12, 'bold'), command = modify)
    button2.place(x=398, y=194)

def Sellers():
    def add_emp():

        add = Frame(a , width=850 , height = 500, bg = '#E17AFF' , highlightthickness=2 , highlightbackground='black')
        add.place(x=35 , y =110)

        label1 = Label(add, text = 'Employee ID' , bg = '#E17AFF' , fg = 'black', font = ('goudy old style' , 15 , 'bold' ))
        label1.place(x = 30 , y= 15)
        labelcolon = Label(add, text = ':' , bg = '#E17AFF' , fg = 'black', font = ('dspijdsdj' , 15 ,'bold'))
        labelcolon.place(x = 180 , y= 13)
        entry1 = Entry(add , width = 15, bg = '#E17AFF' , fg = 'black' , font = ('goudy old style' , 15 , 'bold' ) , bd = 0)
        entry1.place(x=210 , y = 15)
        entry1line = Frame(add, width = 155 , height = 2 , bg = 'black')
        entry1line.place(x = 210 , y = 40)

        label2 = Label(add, text='First Name', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label2.place(x=30, y=65)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=180, y=63)
        entry2 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
        entry2.place(x=210, y=65)
        entry2line = Frame(add, width=155, height=2, bg='black')
        entry2line.place(x=210, y=90)

        label3 = Label(add, text='Last Name', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label3.place(x=30, y=105)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=180, y=103)
        entry3 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
        entry3.place(x=210, y=105)
        entry3line = Frame(add, width=155, height=2, bg='black')
        entry3line.place(x=210, y=130)

        label4 = Label(add, text='Date of Birth', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label4.place(x=30, y=145)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=180, y=143)
        entry4 = DateEntry(add,state = 'readonly', height = 0, font=('goudy old style', 10, 'bold'), date_pattern = 'yyyy/mm/dd')
        entry4.place(x=210, y=168)

        label5 = Label(add, text='Gender', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label5.place(x=30, y= 185)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=180, y=183)
        gender = ['Male', 'Female']
        entry5 = ttk.Combobox(add, values = gender , state='readonly', width = 20)
        entry5.place(x=210, y=197)
        entry5.set('Select')

        username = Label(add, text='Username', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        username.place(x=30, y=225)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=180, y=223)
        username = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
        username.place(x=210, y=225)
        usernameline = Frame(add, width=155, height=2, bg='black')
        usernameline.place(x=210, y=250)


        address_label = Label(add, text='Address', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        address_label.place(x=30, y=265)
        addresscolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        addresscolon.place(x=180, y=263)
        address = Text(add, width=55, height = 6 , fg='black', font=('goudy old style', 15, 'bold'))
        address.place(x=210, y=265)


        label6 = Label(add, text='Date of Joining', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label6.place(x=420, y=15)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=570, y=13)
        entry6 = DateEntry(add, state='readonly', height=0, font=('goudy old style', 10, 'bold'),
                           date_pattern='yyyy/mm/dd')
        entry6.place(x=600, y=18)

        label7 = Label(add, text='Job Type', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label7.place(x=420, y=65)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=570, y=63)
        gender = ['Admin','Seller']
        entry7 = ttk.Combobox(add, values=gender, state='readonly', width=20)
        entry7.place(x=600, y=68)
        entry7.set('Select')

        label8 = Label(add, text='Salary', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label8.place(x=420, y=105)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=570, y=103)
        entry8 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
        entry8.place(x=600, y=105)
        entry8line = Frame(add, width=155, height=2, bg='black')
        entry8line.place(x=600, y=130)

        label9 = Label(add, text='Email', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label9.place(x=420, y=145)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=570, y=143)
        entry9 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
        entry9.place(x=600, y=145)
        entry9line = Frame(add, width=155, height=2, bg='black')
        entry9line.place(x=600, y=170)

        label10 = Label(add, text='Phone Number', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        label10.place(x=420, y=185)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=570, y=183)
        entry10 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
        entry10.place(x=600, y=185)
        entry10line = Frame(add, width=155, height=2, bg='black')
        entry10line.place(x=600, y=210)

        password = Label(add, text='Password', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
        password.place(x=420, y=225)
        labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
        labelcolon.place(x=570, y=223)
        password = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
        password.place(x=600, y=225)
        passwordline = Frame(add, width=155, height=2, bg='black')
        passwordline.place(x=600, y=250)

        def back():
            add.destroy()

        def ad():
            if entry1.get() =='' or entry2.get() == '' or entry3.get()  == '' or entry5.get == 'Select' or address.get("1.0", "end-1c") == '' or entry7.get == 'Select' or entry8.get() == '' or entry9.get() == '' or entry10.get() == '' or address.get("1.0", "end-1c") == '':
                messagebox.showerror('Error' , 'All Fields are Required')
            elif len(entry10.get()) != 10:
                messagebox.showerror('Error' , 'Invalid Phone Number')
            else :
                try:
                    main_con = sqltor.connect(host='localhost', user='root', password='tiger')
                    mycursor = main_con.cursor()
                except:
                    messagebox.showerror('Error', 'Failed to connect to Database')
                    return

                query = 'use shivay_supermart'
                mycursor.execute(query)
                query = 'select employeeID from employee'
                mycursor.execute(query)
                row = mycursor.fetchall()
                jaishreeram = [value[0] for value in row]
                if entry1.get() in jaishreeram:
                    messagebox.showerror('Error', 'Employee ID Exist')

                else:
                    query = 'insert into employee (EmployeeID , FirstName , lastname , dateofbirth , gender, hiredate , jobtitle , salary , email , phonenumber , address) values (%s , %s , %s, %s, %s , %s ,%s ,%s, %s , %s ,%s )'
                    mycursor.execute(query, (entry1.get() , entry2.get() , entry3.get() , entry4.get() , entry5.get() , entry6.get() , entry7.get() , entry8.get() , entry9.get() , entry10.get() , address.get("1.0", "end-1c")))
                    messagebox.showinfo('Success', 'Employee Added')
                    add.destroy()

                    for item in tree.get_children():
                        tree.delete(item)
                    query = 'select * from employee'
                    mycursor.execute(query)
                    row = mycursor.fetchall()

                    for i in row:
                        tree.insert(parent='', index='end', values=i)
                    main_con.commit()
                    main_con.close()

        addbuttonframe = Frame(add, bg='black', width=93, height=37)
        addbuttonframe.place(x=287, y=435)
        addbutton = Button(add, text='Add', width=10, background='#FF4040', activebackground='#FF1818', bd=0,foreground='black', activeforeground='black', font=('Calibri', 12, 'bold'), command=ad)
        addbutton.place(x=290, y=439)

        backbuttonframe = Frame(add, bg='black', width=93, height=37)
        backbuttonframe.place(x=397, y=435)
        backbutton = Button(add, text='Back', width=10, background='#5519FF', activebackground='#4508F4', bd=0,foreground='black', activeforeground='black', font=('Calibri', 12, 'bold'),
                            command=back)
        backbutton.place(x=400, y=439)

    def update_empl():
        selecteditem = tree.selection()
        if selecteditem == ():
            messagebox.showerror('error', 'Please select Employee to Update')
        else:
            add = Frame(a, width=850, height=500, bg='#E17AFF', highlightthickness=2, highlightbackground='black')
            add.place(x=35, y=110)

            label1 = Label(add, text='Employee ID', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label1.place(x=30, y=15)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=180, y=13)
            entry1 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            entry1.place(x=210, y=15)
            entry1line = Frame(add, width=155, height=2, bg='black')
            entry1line.place(x=210, y=40)

            label2 = Label(add, text='First Name', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label2.place(x=30, y=65)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=180, y=63)
            entry2 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            entry2.place(x=210, y=65)
            entry2line = Frame(add, width=155, height=2, bg='black')
            entry2line.place(x=210, y=90)

            label3 = Label(add, text='Last Name', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label3.place(x=30, y=105)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=180, y=103)
            entry3 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            entry3.place(x=210, y=105)
            entry3line = Frame(add, width=155, height=2, bg='black')
            entry3line.place(x=210, y=130)

            label4 = Label(add, text='Date of Birth', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label4.place(x=30, y=145)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=180, y=143)
            entry4 = DateEntry(add, state='readonly', height=0, font=('goudy old style', 10, 'bold'),
                               date_pattern='yyyy/mm/dd')
            entry4.place(x=210, y=168)

            label5 = Label(add, text='Gender', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label5.place(x=30, y=185)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=180, y=183)
            gender = ['Male', 'Female']
            entry5 = ttk.Combobox(add, values=gender, state='readonly', width=20)
            entry5.place(x=210, y=197)
            entry5.set('Select')

            username = Label(add, text='Username', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            username.place(x=30, y=225)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=180, y=223)
            usernameentry = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            usernameentry.place(x=210, y=225)
            usernameline = Frame(add, width=155, height=2, bg='black')
            usernameline.place(x=210, y=250)

            address_label = Label(add, text='Address', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            address_label.place(x=30, y=265)
            addresscolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            addresscolon.place(x=180, y=263)
            address = Text(add, width=55, height=6, fg='black', font=('goudy old style', 15, 'bold'))
            address.place(x=210, y=265)

            label6 = Label(add, text='Date of Joining', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label6.place(x=420, y=15)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=570, y=13)
            entry6 = DateEntry(add, state='readonly', height=0, font=('goudy old style', 10, 'bold'),
                               date_pattern='yyyy/mm/dd')
            entry6.place(x=600, y=18)

            label7 = Label(add, text='Job Type', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label7.place(x=420, y=65)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=570, y=63)
            gender = ['Admin', 'Seller']
            entry7 = ttk.Combobox(add, values=gender, state='readonly', width=20)
            entry7.place(x=600, y=68)
            entry7.set('Select')

            label8 = Label(add, text='Salary', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label8.place(x=420, y=105)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=570, y=103)
            entry8 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            entry8.place(x=600, y=105)
            entry8line = Frame(add, width=155, height=2, bg='black')
            entry8line.place(x=600, y=130)

            label9 = Label(add, text='Email', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label9.place(x=420, y=145)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=570, y=143)
            entry9 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            entry9.place(x=600, y=145)
            entry9line = Frame(add, width=155, height=2, bg='black')
            entry9line.place(x=600, y=170)

            label10 = Label(add, text='Phone Number', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            label10.place(x=420, y=185)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=570, y=183)
            entry10 = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            entry10.place(x=600, y=185)
            entry10line = Frame(add, width=155, height=2, bg='black')
            entry10line.place(x=600, y=210)

            password = Label(add, text='Password', bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'))
            password.place(x=420, y=225)
            labelcolon = Label(add, text=':', bg='#E17AFF', fg='black', font=('dspijdsdj', 15, 'bold'))
            labelcolon.place(x=570, y=223)
            passwordentry = Entry(add, width=15, bg='#E17AFF', fg='black', font=('goudy old style', 15, 'bold'), bd=0)
            passwordentry.place(x=600, y=225)
            passwordline = Frame(add, width=155, height=2, bg='black')
            passwordline.place(x=600, y=250)

            entry1.insert(0 , tree.item(selecteditem)['values'][0])
            entry2.insert(0 , tree.item(selecteditem)['values'][1])
            entry3.insert(0 , tree.item(selecteditem)['values'][2])
            usernameentry.insert(0, tree.item(selecteditem)['values'][3])
            passwordentry.insert(0 , tree.item(selecteditem)['values'][4])
            dob = tree.item(selecteditem, "values")[5]
            entry4.set_date(dob)
            entry5.set(tree.item(selecteditem)['values'][6])
            doj = tree.item(selecteditem, "values")[7]
            entry6.set_date(doj)
            entry7.set( tree.item(selecteditem)['values'][8])
            entry8.insert(0 , tree.item(selecteditem)['values'][9])
            entry9.insert(0 , tree.item(selecteditem)['values'][10])
            entry10.insert(0 , tree.item(selecteditem)['values'][11])
            address.insert(1.0 , tree.item(selecteditem)['values'][12])
            why = entry1.get()

            def update():
                list = [entry1.get(), entry2.get(), entry3.get(), entry4.get(), entry5.get(), entry6.get(), entry7.get(), entry8.get(), entry9.get(), entry10.get(), address.get("1.0", "end-1c") , usernameentry.get() , passwordentry.get() ,why]

                if entry1.get() =='' or entry2.get() == '' or entry3.get()  == '' or entry5.get == 'Select' or address.get("1.0", "end-1c") == '' or entry7.get == 'Select' or entry8.get() == '' or entry9.get() == '' or entry10.get() == '' or address.get("1.0", "end-1c") == '':
                    messagebox.showerror('Error', 'Missing Details')
                else:
                    main_con = sqltor.connect(host='localhost', user='root', password='tiger')
                    mycursor = main_con.cursor()
                    query = 'use shivay_supermart'
                    mycursor.execute(query)

                    query = 'select * from employee where employeeID = %s'
                    mycursor.execute(query, [entry1.get()])
                    row = mycursor.fetchone()
                    if row == None:
                        messagebox.showerror('Error', "Invalid Product! Employee ID Exist")
                        return
                    else:
                        query = 'update employee set employeeID = %s , Firstname = %s , LastName = %s , DateofBirth = %s , Gender = %s , Hiredate = %s , jobtitle = %s , salary = %s , email = %s , phonenumber = %s , address = %s , username = %s , password = %s  where employeeID = %s'
                        mycursor.execute(query, list)

                        list2 = [usernameentry.get(), entry9.get()]
                        query = 'update userdata set username = %s where email = %s'
                        mycursor.execute(query, list2)

                        list3 = [ passwordentry.get() , usernameentry.get()]
                        query = 'update userdata set password = %s where username = %s'
                        mycursor.execute(query , list3)
                        main_con.commit()

                        for item in tree.get_children():
                            tree.delete(item)

                        query = 'select * from employee'
                        mycursor.execute(query)
                        all = mycursor.fetchall()
                        for val in all:
                            tree.insert(parent='', index='end', values=val)

                        messagebox.showinfo('Updated', f'Employee {entry1.get()} is modified')
                        add.destroy()

            updatebuttonframe = Frame(add, bg='black', width=93, height=37)
            updatebuttonframe.place(x=287, y=435)
            updatebutton = Button(add, text='Update', width=10, background='#FF4040', activebackground='#FF1818', bd=0, foreground='black', activeforeground='black', font=('Calibri', 12, 'bold'), command=update)
            updatebutton.place(x=290, y=439)

            def back():
                add.destroy()

            backbuttonframe = Frame(add, bg='black', width=93, height=37)
            backbuttonframe.place(x=397, y=435)
            backbutton = Button(add, text='Back', width=10, background='#5519FF', activebackground='#4508F4', bd=0,foreground='black', activeforeground='black', font=('Calibri', 12, 'bold'), command=back)
            backbutton.place(x=400, y=439)


    def delete():
        selecteditem = tree.selection()
        if selecteditem == ():
            messagebox.showerror('error', 'Please select Employee to Delete')
        else:
            ask = messagebox.askyesno('Delete', '    Delete Record?')
            if ask == True:

                a = tree.item(selecteditem)['values'][0]
                b = tree.item(selecteditem)['values'][3]
                main_con = sqltor.connect(host='localhost', user='root', password='tiger')
                mycursor = main_con.cursor()
                query = 'use shivay_supermart'
                mycursor.execute(query)

                query = 'delete from employee where employeeID = %s'
                mycursor.execute(query, [a])
                query = 'delete from userdata where username = %s'
                mycursor.execute(query, [b] )

                main_con.commit()

                for item in tree.get_children():
                    tree.delete(item)

                query = 'select * from employee'
                mycursor.execute(query)
                all = mycursor.fetchall()
                for val in all:
                    tree.insert(parent='', index='end', values=val)

                messagebox.showinfo('Deleted', f'Employee {a} is Deleted')

            else:
                return




    a = Frame(root , width = 950  , height=720 , bg = '#86C5FF')
    a.place(x =350 , y = 0)

    head = Frame(a, bg='black', width=1400, height=90)
    head.place(x=0, y=0)
    label = Label(a , text = 'Manage Employees' , bg = 'black' , fg = 'white'  , font = ('goudy old style' , 40 , 'bold'))
    label.place(x=250 , y = 10)

    treeview_frame = Frame(a, bg='#FFFDD8', highlightthickness=2,
                           highlightbackground='black')  # , width=570, height=510,
    treeview_frame.place(x=35, y=110, width=850, height=500)
    col = ['Employee_ID' , 'FName' , 'LName' , 'Username' , 'Password' ,  'DOB' , 'Gender' , 'Hiredate' , 'JobTitle' , 'Salary' , 'Email' , 'PNO', 'add']



    tree = ttk.Treeview(treeview_frame, columns=col, selectmode=BROWSE, height=100)

    xscroll = ttk.Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    yscroll = ttk.Scrollbar(tree, orient=VERTICAL, command=tree.yview)

    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

    tree.heading('Employee_ID', text='ID', anchor=CENTER)
    tree.heading('FName', text='First Name', anchor=CENTER)
    tree.heading('LName', text='Last Name', anchor=CENTER)
    tree.heading('Username', text='Username', anchor=CENTER)
    tree.heading('Password', text='Password', anchor=CENTER)
    tree.heading('DOB', text='Date Of Birth', anchor=CENTER)
    tree.heading('Gender', text='Gender', anchor=CENTER)
    tree.heading('Hiredate', text='Date of Joining', anchor=CENTER)
    tree.heading('JobTitle', text='Job Type', anchor=CENTER)
    tree.heading('Salary', text='Salary ', anchor=CENTER)
    tree.heading('Email', text='Email ', anchor=CENTER)
    tree.heading('PNO', text='Phone Number ', anchor=CENTER)
    tree.heading('add', text='Address', anchor=CENTER)

    tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)


    tree.column('#0' , width=0 , minwidth=0)
    tree.column('Employee_ID', width=100, minwidth=100, anchor=CENTER)
    tree.column('FName', width=150, minwidth=150, anchor=CENTER)
    tree.column('LName', width=150, minwidth=150, anchor=CENTER)
    tree.column('Username', width=150, minwidth=150, anchor=CENTER)
    tree.column('Password', width=150, minwidth=150, anchor=CENTER)
    tree.column('DOB', width=150, minwidth=150, anchor=CENTER)
    tree.column('Gender', width=80, minwidth=80, anchor=CENTER)
    tree.column('Hiredate', width=150, minwidth=150, anchor=CENTER)
    tree.column('JobTitle', width=120, minwidth=120, anchor=CENTER)
    tree.column('Salary', width=100, minwidth=100, anchor=CENTER)
    tree.column('Email', width=200, minwidth=200, anchor=CENTER)
    tree.column('PNO', width=130, minwidth=130, anchor=CENTER)
    tree.column('add', width=200, minwidth=200, anchor=CENTER)

    query = 'use shivay_supermart'
    mycursor.execute(query)
    query = 'Select * from Employee'
    mycursor.execute(query)
    row = mycursor.fetchall()
    for rows in row:
        tree.insert('' , END , values=rows)

    frame1 = Frame(a , width = 125  , height=40, bg = 'black')
    frame1.place(x= 60 , y = 620)
    button1 = Button(a , text = 'Add Employee' , fg = 'black' , bg = '#FFDE59' , font=('Arial', 11, 'bold'),activebackground='#FFDE39', activeforeground='black', width=12 , bd=0 ,command = add_emp)
    button1.place(x = 65, y =626)

    frame2 = Frame(a, width=125, height=40, bg='black')
    frame2.place(x=200, y=620)
    button2 = Button(a, text='Update Record', fg='black', bg='#C7FF80', font=('Arial', 11, 'bold'),activebackground='#C7FF60', activeforeground='black', width=12, bd=0 , command  = update_empl)
    button2.place(x=205, y=626)

    frame3 = Frame(a, width=143, height=40, bg='black')
    frame3.place(x=340, y=620)
    button3 = Button(a, text='Delete Employee', fg='black', bg='#FF89D2', font=('Arial', 11, 'bold'),
                     activebackground='#FF69D2', activeforeground='black', width=14, bd=0 , command = delete)
    button3.place(x=345, y=626)

    def search(a):
        try:
            main_con = sqltor.connect(host='localhost', user='root', password='tiger')
            mycursor = main_con.cursor()
            query = 'use shivay_supermart'
            mycursor.execute(query)
            if combobox.get() == 'ID':
                query = "select * from employee where EmployeeID LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'FName':
                query = "select * from employee where FirstName LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'LName':
                query = "select * from employee where LastName LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Username':
                query = "select * from employee where username LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Password':
                query = "select * from employee where password LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Date of Birth':
                query = "select * from employee where DateofBirth LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Gender':
                query = "select * from employee where Gender LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Date of Joining':
                query = "select * from employee where Hiredate LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Job Type':
                query = "select * from employee where JobTitle LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Salary':
                query = "select * from employee where salary LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Email':
                query = "select * from employee where email LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            elif combobox.get() == 'Phone Number':
                query = "select * from employee where phonenumber LIKE '%" + var_search.get() + "%'"
                mycursor.execute(query)
                row = mycursor.fetchall()
                if len(row) > 0:
                    tree.delete(*tree.get_children())
                    for i in row:
                        tree.insert('',END,values=i)
                else:
                    tree.delete(*tree.get_children())

            else:
                pass

        except :
            messagebox.showerror('Error', "Error")

    table_category = ('ID' , 'FName' , 'LName', 'Username' , 'Password'  , 'Date of Birth' , 'Gender' , 'Date of Joining' , 'Job Type' , 'Salary' , 'Email' , 'Phone Number')
    combobox = ttk.Combobox(a , values = table_category ,state='readonly' ,width = 15 , height =10)
    combobox.set('Select')
    combobox.place(x = 580 , y = 630)

    var_search = StringVar()
    search_entry = Entry(a , width = 20, font = ('poppins', 11 ) ,textvariable=var_search,  bg = 'white' , fg = 'black')
    search_entry.place(x = 700 , y = 630)
    search_entry.bind("<Key>" , search)

    search_label = Label(a , text = 'Sort By :' , bg = '#86C5FF' , fg = 'black' , font = ('Binate' ,11 , 'bold'))
    search_label.place(x=500 , y = 630)

    search_icon_image = PhotoImage(file='text.png')
    search_icon = Label(a , image=search_icon_image , bg = '#86C5FF')
    search_icon.place(x = 870 , y = 628)

    search_icon.image = search_icon_image


def Finance():
    a = Frame(root, bg="#FFF08A", height=726, width=950)
    a.place(x=350, y=0)

    head = Frame(a, bg='black', width=1400, height=90)
    head.place(x=0, y=0)
    label = Label(a, text='Calculate Profit/Loss', bg='black', fg='white', font=('goudy old style', 40, 'bold'))
    label.place(x=250, y=10)

    detail = Frame(a, width=350, height=500, bg='firebrick1' , border=2)
    detail.place(x=30, y=140)

    last = []
    first = []
    value = ['January' , 'February' , 'March' , 'April' , 'May' , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December']

    comb = Label(detail, text='Month                  :', bg='firebrick1', fg='white', font=('Calibri', 12, 'bold'))
    comb.place(x=20, y=10)

    combbo = ttk.Combobox(detail, values=value, state='readonly', width=20 , height =2)
    combbo.place(x = 170 , y =10)
    combbo.set('Select Month')

    graph = Frame(a, width=500, height=500, bg='black', highlightthickness=2, highlightbackground='black')
    graph.place(x=400, y=140)




    sales = Label(detail, text='Total Sales           :' , bg = 'firebrick1' , fg='white' , font=('Calibri', 12 , 'bold'))
    sales.place(x=20 , y=110)
    salesentry = Entry(detail , width = 15 , fg = 'white' , bg = 'firebrick1', bd = 0, font=('Calibri', 12 , 'bold') )
    salesentry.place(x = 170 , y = 110)
    salesentryline = Frame(detail , width = 140 , height=1, bg = 'white')
    salesentryline.place(x= 170 , y = 130)

    expense = Label(detail, text='Total Expense      :', bg='firebrick1', fg='white', font=('Calibri', 12, 'bold'))
    expense.place(x=20, y=150)
    expenseentry = Entry(detail, width=15, fg='white', bg='firebrick1', bd=0, font=('Calibri', 12, 'bold'))
    expenseentry.place(x=170, y=150)
    expenseentryline = Frame(detail, width=140, height=1, bg='white')
    expenseentryline.place(x=170, y=170)

    profit = Label(detail, text='Total Profit/Loss :', bg='firebrick1', fg='white', font=('Calibri', 12, 'bold'))
    profit.place(x=20, y=190)
    profitentry = Entry(detail, width=15, fg='white', bg='firebrick1', bd=0, font=('Calibri', 12, 'bold'))
    profitentry.place(x=170, y=190)
    profitentryline = Frame(detail, width=140, height=1, bg='white')
    profitentryline.place(x=170, y=210)

    def clearbutton1():
        salesentry.delete(0,END)
        expenseentry.delete(0,END)
        profitentry.delete(0,END)

    clearbutton = Button(detail, text='Clear', bg='white', fg='black', border=0, activeforeground='white',activebackground='grey', width = 12, font=('Calibri', 12, 'bold'), command=clearbutton1)
    clearbutton.place(x=180, y=250)

    profit1 = Label(detail, text='Profit/Loss 1 :', bg='firebrick1', fg='white', font=('Calibri', 10, 'bold'))
    profit1.place(x=20, y=300)
    entry1 = Entry(detail, width=20, bg='white', fg='black')
    entry1.place(x=110, y=300)

    profit2 = Label(detail, text='Profit/Loss 2 :', bg='firebrick1', fg='white', font=('Calibri', 10, 'bold'))
    profit2.place(x=20, y=325)
    entry2 = Entry(detail, width=20, bg='white', fg='black')
    entry2.place(x=110, y=325)

    profit3 = Label(detail, text='Profit/Loss 3 :', bg='firebrick1', fg='white', font=('Calibri', 10, 'bold'))
    profit3.place(x=20, y=350)
    entry3 = Entry(detail, width=20, bg='white', fg='black')
    entry3.place(x=110, y=350)

    profit4 = Label(detail, text='Profit/Loss 4 :', bg='firebrick1', fg='white', font=('Calibri', 10, 'bold'))
    profit4.place(x=20, y=375)
    entry4 = Entry(detail, width=20, bg='white', fg='black')
    entry4.place(x=110, y=375)

    profit5 = Label(detail, text='Profit/Loss 5 :', bg='firebrick1', fg='white', font=('Calibri', 10, 'bold'))
    profit5.place(x=20, y=400)
    entry5 = Entry(detail, width=20, bg='white', fg='black')
    entry5.place(x=110, y=400)

    def calculatebutton():
        if combbo.get() == 'Select Month':
            messagebox.showerror('Error' , 'Select Month')
        else:
            try:
                try:
                    sales = float(salesentry.get())
                    expense = float(expenseentry.get())
                    profit = sales - expense
                    profitentry.delete(0,END)
                    profitentry.insert(0, f"{profit:.2f}")

                except ValueError:
                    profitentry.insert(0, 'Invalid Input')
                if entry1.get() == '':
                    if combbo.get() not in last:
                        entry1.insert(0, f"{profit:.2f}")
                        first.append(entry1.get())
                        if len(last) < 5:
                            last.append(combbo.get())
                        else:
                            messagebox.showerror('Error', 'Maximum of 5 datas can be plotted')
                    else:
                        messagebox.showerror('Error', f"Data of month {combbo.get()} is inserted")
                elif entry2.get() == '':
                    if combbo.get() not in last:
                        entry2.insert(  0, f"{profit:.2f}")
                        first.append(entry2.get())
                        if len(last) < 5:
                            last.append(combbo.get())
                        else:
                            messagebox.showerror('Error', 'Maximum of 5 datas can be plotted')
                    else:
                        messagebox.showerror('Error' , f"Data of month {combbo.get()} is inserted")
                elif entry3.get() == '':
                    if combbo.get() not in last:
                        entry3.insert(  0, f"{profit:.2f}")
                        first.append(entry3.get())
                        if len(last) < 5:
                            last.append(combbo.get())
                        else:
                            messagebox.showerror('Error', 'Maximum of 5 datas can be plotted')
                    else:
                        messagebox.showerror('Error' , f"Data of month {combbo.get()} is inserted")
                elif entry4.get() == '':
                    if combbo.get() not in last:
                        entry4.insert(0, f"{profit:.2f}")
                        first.append(entry4.get())
                        if len(last) < 5:
                            last.append(combbo.get())
                        else:
                            messagebox.showerror('Error', 'Maximum of 5 datas can be plotted')
                    else:
                        messagebox.showerror('Error', f"Data of month {combbo.get()} is inserted")
                elif entry5.get() == '':
                    if combbo.get() not in last:
                        entry5.insert(0, f"{profit:.2f}")
                        first.append(entry5.get())
                        if len(last) < 5:
                            last.append(combbo.get())
                        else:
                            messagebox.showerror('Error', 'Maximum of 5 datas can be plotted')
                    else:
                        messagebox.showerror('Error', f"Data of month {combbo.get()} is inserted")
                else:
                    if len(last) < 5:
                        last.append(combbo.get())
                    else:
                        messagebox.showerror('Error', 'Maximum of 5 datas can be plotted')

            except:
                print('Fields are Empty')
            print(first)
            print(last)

    calculatebutton = Button(detail , text = 'Calculate', bg = 'white', fg = 'black' , border=0 , activeforeground='white' , activebackground='grey' , width = 12, font = ('Calibri', 12, 'bold'), command = calculatebutton)
    calculatebutton.place(x = 70 , y = 250)

    fig, ax = plt.subplots(figsize=(5, 5))

    def clear_graph():
        for widget in graph.winfo_children():
            widget.destroy()


    def showgraph():
        clear_graph()
        if len(last) == 0 or len(first) == 0:
            messagebox.showerror('Error' , 'No data available to plot the graph')
        else:
            plt.plot(range(len(last)), [float(value) for value in first], marker = 'o' , markeredgecolor = 'r')
            plt.xticks(range(len(last)), last, rotation=0)
            plt.xlabel("Months")
            plt.ylabel("Profit/Loss")
            canvas = FigureCanvasTkAgg(plt.gcf(), master=graph)
            canvas.draw()
            canvas.get_tk_widget().pack()

            def generate_random_filename():
                filename = ''.join(random.choice(string.digits) for _ in range(3))
                return f"graph_{filename}.pdf"

            def save():
                savedir = filedialog.askdirectory()
                if savedir:
                    random_filename = generate_random_filename()
                    plt.savefig(os.path.join(savedir, random_filename))
                    messagebox.showinfo('Success', f"Graph saved as '{os.path.join(savedir, random_filename)}'")
                else:
                     return

            savebutton = Button(graph , text = 'Save' , bg = 'firebrick2' , fg = 'black' , activebackground='firebrick1' , activeforeground='black' , font = ('Calibri' ,10, 'bold'), width=11, bd=0 , highlightbackground='black' , highlightthickness=2 , command=save)
            savebutton.place(x = 415 , y = 476)


    showgraphbutton = Button(detail, text='Show Graph', bg='white', fg='black', border=0, activeforeground='white',activebackground='grey', width=12, font=('Calibri', 12, 'bold') , command=showgraph)
    showgraphbutton.place(x=50, y=450)

    def clearbutton2():
        for widget in graph.winfo_children():
            widget.destroy()
        entry1.delete(0,END)
        entry2.delete(0,END)
        entry3.delete(0,END)
        entry4.delete(0,END)
        entry5.delete(0,END)
        last.clear()
        first.clear()




    clearbutton = Button(detail, text='Clear', bg='white', fg='black', border=0, activeforeground='white',
                         activebackground='grey', width=12, font=('Calibri', 12, 'bold'), command=clearbutton2)
    clearbutton.place(x=160, y=450)




def email():
    a = Frame(root, bg="#ff8210", height=726, width=950)
    a.place(x=350, y=0)
    head = Frame(a, bg='black', width=1400, height=90)
    head.place(x=0, y=0)
    label = Label(a, text='Send Email', bg='black', fg='white', font=('goudy old style', 40, 'bold'))
    label.place(x=300, y=10)

    emailframe = Frame(a, width=850, height=550, bg='black')
    emailframe.place(x=40, y=110)

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("All files", "*.*")])
        if file_path:
            attachment_path.set(file_path)
            attachment_label1.config(text=f"Attached File: {file_path}")
            attachment_label1.config(font=('Helvetica', 8, 'bold'))
            attachment_button.place(x=670, y=448)

    def send_email():
        sender_email = sender_entry.get()
        sender_password = 'aazc vboy nxnq igoy'
        receiver_email = receiver_entry.get()
        subject = head_entry.get()
        body = body_entry.get("1.0", "end-1c")

        if sender_email == '' or receiver_email == '' or subject == '' or body == '':
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        try:
            smtp_server = 'smtp.gmail.com'
            smtp_port = 587
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            file_path = attachment_path.get()
            if file_path:
                # Determine MIME type based on file extension
                mime_type, _ = mimetypes.guess_type(file_path)
                if mime_type is None:
                    mime_type = 'application/octet-stream'

                with open(file_path, 'rb') as file:
                    attachment = MIMEBase(*mime_type.split('/'))
                    attachment.set_payload(file.read())
                    encoders.encode_base64(attachment)
                    attachment.add_header('Content-Disposition', f'attachment; filename={file_path}')
                    msg.attach(attachment)
                attachment_label1.config(text=f"Attached File: {file_path}")
            else:
                attachment_label1.config(text="No file attached")

            # Send the email
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            messagebox.showinfo('Success!', f"Email sent successfully to {receiver_email}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    sender_label = Label(emailframe, text="Sender's Gmail            :", bg='black', fg='white',
                         font=('Helvetica', 12, 'bold'))
    sender_label.place(x=20, y=20)
    sender_entry = Entry(emailframe, bg='white', fg='black', width=40, font=('Helvetica', 10, 'bold'))
    sender_entry.place(x=250, y=20)
    sender_entry.insert(0, 'shivaysupermart0@gmail.com')

    receiver_label = Label(emailframe, text="Receiver's Gmail         :", bg='black', fg='white',font=('Helvetica', 12, 'bold'))
    receiver_label.place(x=20, y=50)
    receiver_entry = Entry(emailframe, bg='white', fg='black', width=40, font=('Helvetica', 10, 'bold'))
    receiver_entry.place(x=250, y=50)

    head_label = Label(emailframe, text="Heading                         :", bg='black', fg='white',font=('Helvetica', 12, 'bold'))
    head_label.place(x=20, y=80)
    head_entry = Entry(emailframe, bg='white', fg='black', width=60, font=('Helvetica', 10, 'bold'))
    head_entry.place(x=250, y=80)

    body_label = Label(emailframe, text="Body                               :", bg='black', fg='white',font=('Helvetica', 12, 'bold'))
    body_label.place(x=20, y=110)
    body_entry = Text(emailframe, height=20, width=70)
    body_entry.place(x=250, y=110)
    text = 'This is an auto generated sample text. Please clear the fields before writing.'
    body_entry.insert(1.0, text)

    attachment_label = body_label = Label(emailframe, text="Attachment                       :", bg='black',fg='white', font=('Helvetica', 12, 'bold'))
    body_label.place(x=20, y=450)
    attachment_path = StringVar()
    attachment_button = Button(emailframe, text="Attach File", width=12, bg='white', fg='black',font=('Helvetica', 9, 'bold'), command=browse_file)
    attachment_button.place(x=370, y=450)
    attachment_label1 = Label(emailframe, text="No file attached", bg='black', fg='white',font=('Helvetica', 10, 'bold'))
    attachment_label1.place(x=250, y=450)

    send_email_button = Button(emailframe, text="Send Email", width=12, font=('Helvetica', 10, 'bold'), bg='white',bd=0, activebackground='white', fg='black', activeforeground='black', command=send_email)
    send_email_button.place(x=410, y=500)

    def clear_email():
        receiver_entry.delete(0,END)
        head_entry.delete(0,END)
        if body_entry.insert(index = 1.0 , chars = 'This is an auto generated sample text. Please clear the fields before writing.'):
            pass
        else:
            body_entry.insert(1.0,'This is an auto generated sample text. Please clear the fields before writing.')


    clear_button = Button(emailframe, text="Clear", width=12, font=('Helvetica', 10, 'bold'), bg='white',
    bd=0, activebackground='white', fg='black', activeforeground='black', command=clear_email)
    clear_button.place(x=525, y=500)

def logout():
    ans = messagebox.askyesno('Exit', 'Do you want to Log Out?')
    if ans == True:
        root.withdraw()
        os.system('signinpage.py')
    else:
        pass



def customer():
    a = Frame(root, bg="#ff8210", height=726, width=950)
    a.place(x=350, y=0)
    head = Frame(a, bg='black', width=1400, height=90)
    head.place(x=0, y=0)
    label = Label(a, text='Total Customers', bg='black', fg='white', font=('goudy old style', 40, 'bold'))
    label.place(x=300, y=10)

    treeview_frame = Frame(a, bg='#FFFDD8', highlightthickness=2,highlightbackground='black')  # , width=570, height=510,
    treeview_frame.place(x=30, y=130, width=870, height=500)
    col = ['Customer Name' , 'Phone Number']

    tree = ttk.Treeview(treeview_frame, columns=col, selectmode=BROWSE, height=100)

    xscroll = ttk.Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
    yscroll = ttk.Scrollbar(tree, orient=VERTICAL, command=tree.yview)

    xscroll.pack(side=BOTTOM, fill=X)
    yscroll.pack(side=RIGHT, fill=Y)
    tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)

    tree.heading('Customer Name', text='Customer Name', anchor=CENTER)
    tree.heading('Phone Number', text='Phone Number', anchor=CENTER)

    tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

    tree.column('#0', width=0, minwidth=0)
    tree.column('Customer Name', width=400, minwidth=400, anchor=CENTER)
    tree.column('Phone Number', width=450, minwidth=400, anchor=CENTER)

    query = 'use shivay_supermart'
    mycursor.execute(query)
    query = 'select * from customer'
    mycursor.execute(query)
    row = mycursor.fetchall()
    for i in row:
        tree.insert('',END,values=i)



root.title('Grocery Managment System')
root.iconbitmap('logo.ico')
root.geometry('1290x768+0+0')
root.resizable(False , False)
root.minsize(width=1290 , height=768)

bg = PhotoImage(file='homepage_admin.png')
window = Label(root , image = bg)
window.pack()

dashboard_button_0 = Button(root , text = 'Dashboard' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 12 , 'bold') , width=15 , height= 1 , activeforeground='white' , activebackground='#ff8210' ,bd=0 , command=dashboard)
dashboard_button_0.place(x = 100 , y = 223)

dashboard_button_1 = Button(root , text = 'Products' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 12 , 'bold') , width=15 , height = 1 , activeforeground='white' , bd = 0, activebackground='#ff8210' , border=0 , command = products)
dashboard_button_1.place(x = 100 , y = 280)

dashboard_button_2 = Button(root , text = 'Products Categories' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 13 , 'bold') , width=18 , height = 1 , activeforeground='white' , activebackground='#ff8210' , bd = 0 ,command=Products_Categories)
dashboard_button_2.place(x = 100 , y = 335)

dashboard_button_3 = Button(root , text = 'Sellers' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 13 , 'bold') , width=18 , height = 1 , activeforeground='white' , activebackground='#ff8210' ,bd = 0 ,command=Sellers )
dashboard_button_3.place(x = 100 , y = 390)

dashboard_button_4 = Button(root , text = 'Finance' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 13 , 'bold') , width=18 , height = 1 , activeforeground='white' , activebackground='#ff8210' , bd = 0,command = Finance )
dashboard_button_4.place(x = 100, y = 447)

dashboard_button_5 = Button(root , text = 'E-Mail' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 12 , 'bold') , width=15 , height = 1 , activeforeground='white' , activebackground='#ff8210' , bd = 0,command = email)
dashboard_button_5.place(x = 100 , y = 502)

dashboard_button_6 = Button(root , text = 'Customers' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 12 , 'bold') , width=15 , height = 1 , activeforeground='white' , activebackground='#ff8210' , bd = 0,command = customer)
dashboard_button_6.place(x = 100 , y = 561)

dashboard_button_7 = Button(root , text = 'Log Out' , bg = '#ff8210' , fg = 'white' , font=('Aileron' , 12 , 'bold') , width=15 , height = 1 , activeforeground='white' , activebackground='#ff8210' , bd = 0,command = logout)
dashboard_button_7.place(x = 100 , y = 625)

def btn1_click():
   a= []
   b= []
   query= 'select count(*) from products'
   mycursor.execute(query)
   all= mycursor.fetchone()
   a.append(all)
   for i in a:
       b.append(i[0])
   if bt['text']== "Total Products":
       bt.config(text= f"Total Products :- {b[0]}")
       bt.place(x= 510, y= 315)
   else:
       bt.config(text= "Total Products")
       bt.place(x= 540, y= 315)




def btn2_click():
   a= []
   b= []
   query= 'select count(*) from product_category'
   mycursor.execute(query)
   all= mycursor.fetchone()
   a.append(all)
   for i in a:
       b.append(i[0])
   if btn2['text']== "Total Product Categories":
       btn2.config(text= f"Total Product Categories :- {b[0]}")
       btn2.place(x= 900, y= 320)
   else:
       btn2.config(text= "Total Product Categories")
       btn2.place(x= 930, y= 320)


def btn3_click():
   a= []
   b= []
   query= 'select count(*) from employee'
   mycursor.execute(query)
   all= mycursor.fetchone()
   a.append(all)
   for i in a:
       b.append(i[0])
   if btn3['text']== "Total Employee":
       btn3.config(text= f"Total Employee :- {b[0]}")
       btn3.place(x= 500, y= 612)
   else:
       btn3.config(text= "Total Employee")
       btn3.place(x= 520, y= 612)


def btn4_click():
   a= []
   b= []
   query= 'select count(*) from customer'
   mycursor.execute(query)
   all= mycursor.fetchone()
   a.append(all)
   for i in a:
       b.append(i[0])
   if btn4['text']== "Total Customers":
       btn4.config(text= f"Total Customers :- {b[0]}")
       btn4.place(x= 920, y= 612)
   else:
       btn4.config(text= "Total Customers")
       btn4.place(x= 930, y= 612)

bt = Button(root , text= "Total Products", bg= "#FF8210", bd= 0, font= ("Arial", 18,"bold" ), activebackground= "#FF8210", command=btn1_click)
bt.place(x= 540, y= 315)
btn2= Button(root, text= "Total Product Categories", bg= "#FF8210", bd= 0, font= ("Arial", 15, "bold"), activebackground= "#FF8210", command=btn2_click)
btn2.place(x= 930,y= 320)
btn3= Button(root, text= "Total Employee", bg= "#FF8210", bd= 0, font= ("Arial", 18, "bold"), activebackground= "#FF8210" , command=btn3_click)
btn3.place(x= 520, y= 612)
btn4= Button(root, text= "Total Customers", bg= "#FF8210", bd= 0, font= ("Arial", 18, "bold"), activebackground= "#FF8210", command=btn4_click)
btn4.place(x= 930,y= 612)

date = dt.datetime.now()
entrydate = Label(root ,text=f"{date: %B %d, %Y}" , font = ('Helvetica' , 12 , 'bold') , bg = 'black' , fg = 'white')
entrydate.place(x= 540 , y=94)

def my_time():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    meridian = time.strftime("%p")
    entrytime.config(text = hour + ":" + minute + ":" + second + " " + meridian)
    entrytime.after(1000 , my_time)

entrytime = Label(root , text = '' , font= ('Helvetica' , 12 ,'bold') , bg = 'black' , fg= 'white' , )
entrytime.place(x = 1000 , y = 94)

my_time()
root.mainloop()