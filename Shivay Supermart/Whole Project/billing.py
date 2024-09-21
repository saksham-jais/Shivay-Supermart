import time
from tkinter import *
from PIL import Image ,ImageTk
import os
from tkinter import messagebox
import datetime as dt
import mysql.connector as sqltor
from tkinter import ttk
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from tkinter import filedialog


root = Tk()
root.iconbitmap('logo.ico')
main_con = sqltor.connect(host='localhost', user='root', password='tiger')
mycursor = main_con.cursor()
root.title('Shivay Supermart Billing Desk')


def clearbutton():
    for widgets in billarea.winfo_children():
        widgets.destroy()
    for widgets in frame3.winfo_children():
        widgets.destroy()
    after_clear_bill_area()

    aentry1.delete(0,END)
    aentry2.delete(0,END)
    aentry3.delete(0,END)
    aentry4.delete(0,END)
    aentry1.insert(0,0)
    aentry2.insert(0,0)
    aentry3.insert(0,0)
    aentry4.insert(0,0)
    entry1.delete(0,END)
    entry2.delete(0,END)
    entry3.delete(0,END)
    customer_name_var.set("")
    phone_number_var.set("")

style = ttk.Style()
style.theme_use('clam')
def logout():
    ans = messagebox.askyesno('Exit', 'Do you want to Log Out?')
    if ans == True:
        root.withdraw()
        os.system('signinpage.py')
    else:
        pass

def add_to_bill(tree, bill_text , aentry1, aentry2, aentry3, aentry4):

    selected_item = tree.selection()

    if selected_item == ():
        messagebox.showwarning('Warning' , 'Select Product First')
    else:
        item_values = tree.item(selected_item, 'values')

        if not item_values or len(item_values) < 2:
            return

        product_name, price = item_values[2], item_values[3]
        price = float(price)

        current_text = bill_text.get(1.0, END)
        bill_text.config(state=NORMAL)
        bill_text.delete(1.0, END)
        bill_text.insert(END, f"   {current_text}     {product_name}             \t 1           \t {price:.2f}")
        bill_text.config(state=DISABLED)


        past_quan = aentry1.get()
        past_quan = int(past_quan) + 1
        aentry1.delete(0, "end")
        aentry1.insert(0, past_quan)

        subtotal = aentry2.get()
        subtotal = float(subtotal) + price
        totalsubtotal = subtotal
        aentry2.delete(0, "end")
        aentry2.insert(1, f"{subtotal}")

        subtax = aentry3.get()
        subtax = float(subtax) + 0.18 * price
        totalsubtax = subtax
        aentry3.delete(0, "end")
        aentry3.insert(0, f"{subtax:.2f}")

        totall = aentry4.get()
        totall = float(aentry2.get()) +float(aentry3.get())
        aentry4.delete(0, "end")
        aentry4.insert(0, f"{totall:.2f}")

        main_con = sqltor.connect(host='localhost', user='root', password='tiger')
        mycursor = main_con.cursor()
        mycursor.execute('use shivay_supermart')
        a = [item_values[0]]
        query = 'update products set quantity = quantity - 1 where product_id = %s'
        mycursor.execute(query , a)
        main_con.commit()
        main_con.close()



def remove_selected_text(bill_text):
    if bill_text.tag_ranges(SEL):
        selected_text = bill_text.get(SEL_FIRST, SEL_LAST)

        bill_text.config(state=NORMAL)
        bill_text.delete(SEL_FIRST, SEL_LAST)
        bill_text.config(state=DISABLED)

        past_quantity = int(aentry1.get())
        price = float(selected_text.split()[-1])
        subtotal = float(aentry2.get())
        subtax = float(aentry3.get())
        total = float(aentry4.get())

        past_quantity -= 1
        aentry1.delete(0, END)
        aentry1.insert(0, past_quantity)

        subtotal -= price
        aentry2.delete(0, END)
        aentry2.insert(1, f"{subtotal:.2f}")

        subtax -= 0.18 * price
        aentry3.delete(0, END)
        aentry3.insert(0, f"{subtax:.2f}")

        total -= (price + 0.18 * price)
        aentry4.delete(0, END)
        aentry4.insert(0, f"{total:.2f}")
    else:
        messagebox.showerror('Error' , 'No Product Selected')


def bill_search():
    bill_name = entry3.get()
    bill_directory = "C://Users//shiva//Desktop//Bills"
    bill_path = os.path.join(bill_directory, f"{bill_name}.txt")

    if os.path.exists(bill_path):
        bill_text.config(state=NORMAL)
        bill_text.delete(1.0, "end")
        with open(bill_path, "r") as file:
            bill_content = file.read()
            bill_text.insert("1.0", bill_content)
        bill_text.config(state=DISABLED)
    else:
        messagebox.showerror('Error', 'No Bill Found')

root.geometry('1290x768+0+0')
root.resizable(False,False)
image = PhotoImage(file="billing.png")
frame = Label(root, image = image )
frame.pack()

def update_bill_text(*args):
    customer_name = customer_name_var.get()
    phone_number = phone_number_var.get()

    bill_text.config(state=NORMAL)
    bill_text.delete(1.0, END)
    bill_text.insert(END, f"\t\t**SHIVAY SUPERMART**\n\n")
    bill_text.insert(END, f"  Bill Number : {bill_no}\n")
    bill_text.insert(END, f"  Customer Name : {customer_name}\n")
    bill_text.insert(END, f"  Phone Number : {phone_number}\n")
    bill_text.insert(END, '\n\n  ==============================================\n')
    bill_text.insert(END, '     Product        \t Quantity        \t Price\n')
    bill_text.insert(END, '  ==============================================\n')


    bill_text.config(state=DISABLED)


head1 = Label(root , text = 'Customer Name : ' , bg = '#409FF7' , fg = 'black' , font = ('Helvetica' , 12 , 'bold') )
head1.place(x = 360 , y = 105)
customer_name_var = StringVar()
entry1 = Entry(root , textvariable=customer_name_var,width=25 ,  borderwidth=4,font= ('Helvetica' , 12 , 'bold') )
entry1.place(x = 500 , y = 105)
customer_name_var.trace_add('write', update_bill_text)

phone_number_var = StringVar()
head2 = Label(root , text = 'Phone Number : ' , bg = '#409FF7' , fg = 'black' , font = ('Helvetica' , 12 , 'bold') )
head2.place(x = 750 , y = 105)
entry2 = Entry(root , textvariable=phone_number_var , width=20 , borderwidth=4,  font= ('Helvetica' , 12 , 'bold') )
entry2.place(x = 885 , y = 105)
phone_number_var.trace_add('write', update_bill_text)





logout = Button(root , text='Log Out ' , width=12 , borderwidth=2 , bg = 'firebrick1' , fg = 'black' , font = ('Helvetica' , 12 , 'bold') , activebackground='red' , activeforeground='black' , command=logout)
logout.place(x = 1110 , y = 101)


frame = Frame(root , width=1290 , bg = 'black' , height=35)
frame.place(x = 0 , y = 145)

head4 = Label(frame , text= 'Date : ' , bg = 'black' , fg = 'white' , font = ('Helvetica' , 12 , 'bold'))
head4.place(x = 40 , y = 5)

date = dt.datetime.now()
entry4 = Label(frame ,text=f"{date: %B %d, %Y}" , font = ('Helvetica' , 12 , 'bold') , bg = 'black' , fg = 'white')
entry4.place(x= 85 , y= 5)


head5 = Label(frame , text= 'Day : ' , bg = 'black' , fg = 'white' , font = ('Helvetica' , 12 , 'bold'))
head5.place(x = 350 , y = 5)
entry5 = Label(frame ,text=f"{date: %A}" , font = ('Helvetica' , 12 , 'bold') , bg = 'black' , fg = 'white')
entry5.place(x= 400 , y= 5)

def my_time():
    hour = time.strftime("%I")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    meridian = time.strftime("%p")
    entry6.config(text = hour + ":" + minute + ":" + second + " " + meridian)
    entry6.after(1000 , my_time)

head6 = Label(frame , text='Time : ' , bg = 'black' , fg = 'white' ,font = ('Helvetica' , 12 ,'bold'))
head6.place(x = 550 , y = 5)

entry6 = Label(frame , text = '' , font= ('Helvetica' , 12 ,'bold') , bg = 'black' , fg= 'white' , )
entry6.place(x = 620 , y = 5)

my_time()

head_inframe = Frame(root , width=950 , height = 600 , bg = '#DB00FF')
head_inframe.place(x = 0 , y= 180 )

treeview_frame = Frame(head_inframe, bg='#FFFDD8', highlightthickness=2,highlightbackground='black')
treeview_frame.place(x=20, y=15, width=700, height=350)
col = ['Product_ID' , 'Product_Company', 'Product_Name', 'Price']

tree = ttk.Treeview(treeview_frame, columns=col, selectmode=BROWSE, height=100)

xscroll = ttk.Scrollbar(tree, orient=HORIZONTAL, command=tree.xview)
yscroll = ttk.Scrollbar(tree, orient=VERTICAL, command=tree.yview)

xscroll.pack(side=BOTTOM, fill=X)
yscroll.pack(side=RIGHT, fill=Y)
tree.config(yscrollcommand=yscroll.set, xscrollcommand=xscroll.set)


tree.heading('Product_ID', text='Product ID', anchor=CENTER)
tree.heading('Product_Company', text='Comapny', anchor=CENTER)
tree.heading('Product_Name', text='Name', anchor=CENTER)
tree.heading('Price', text='Price', anchor=CENTER)


tree.place(y=0, x=0, relwidth=1, relheight=1, relx=0)

tree.column('#0', width=0 , minwidth=0)
tree.column('Product_ID', width=100 , minwidth=100 , anchor=CENTER)
tree.column('Product_Company', width=200 , minwidth=150, anchor=CENTER)
tree.column('Product_Name', width=200 , minwidth=180, anchor=CENTER)
tree.column('Price', width=200 , minwidth=130, anchor=CENTER)

query = 'use shivay_supermart'
mycursor.execute(query)
query = 'select product_ID , product_company , product_name , price from products'
mycursor.execute(query)
row = mycursor.fetchall()
for i in row :
    tree.insert('' , END  , values = i)

img1 = PhotoImage(file = 'right_arrow.png')
add = Button(head_inframe , image=img1 , width = 40 , bg = 'white' , bd = 0 , command=lambda: add_to_bill(tree, bill_text , aentry1, aentry2, aentry3, aentry4))
add.place(x = 750 , y = 170)

img2 = PhotoImage(file = 'left_arrow.png')
remove = Button(head_inframe , image=img2 , width = 40 , bg = 'white' , bd = 0, command=lambda: remove_selected_text(bill_text))
remove.place(x = 750 , y = 200)


label1 = Label(head_inframe , text = 'Total Quantity' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
label1.place(x = 20 , y = 375)
labelcolon = Label(head_inframe , text = ':' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
labelcolon.place(x = 130 , y = 372)
aentry1 = Entry(head_inframe , width = 16,  bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold') , bd = 0)
aentry1.place(x = 160 , y = 375)
aentry1.insert(0, 0)
entryline = Frame(head_inframe , width = 130 ,  bg = 'white', height = 1)
entryline.place(x = 160 , y = 395)

label2 = Label(head_inframe , text = 'Sub Total' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
label2.place(x = 20 , y = 410)
labelcolon = Label(head_inframe , text = ':' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
labelcolon.place(x = 130 , y = 407)
aentry2 = Entry(head_inframe , width = 16,  bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold') , bd = 0)
aentry2.place(x = 160 , y = 410)
aentry2.insert(0,0)
entryline = Frame(head_inframe , width = 130 ,  bg = 'white', height = 1)
entryline.place(x = 160 , y = 430)

label3 = Label(head_inframe , text = 'Total Tax (18%)' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
label3.place(x = 20 , y = 445)
labelcolon = Label(head_inframe , text = ':' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
labelcolon.place(x = 130 , y = 442)
aentry3 = Entry(head_inframe , width = 16,  bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold') , bd = 0)
aentry3.place(x = 160 , y = 445)
aentry3.insert(0,0)
entryline = Frame(head_inframe , width = 130 ,  bg = 'white', height = 1)
entryline.place(x = 160 , y = 465)

label4 = Label(head_inframe , text = 'Total Price' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
label4.place(x = 400 , y = 375)
labelcolon = Label(head_inframe , text = ':' , bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold'))
labelcolon.place(x = 510 , y = 372)
aentry4 = Entry(head_inframe , width = 16,  bg = '#DB00FF' , fg = 'white' , font = ('Helvetica' , 10 , 'bold') , bd = 0)
aentry4.place(x = 540 , y = 375)
aentry4.insert(0,0)
entryline = Frame(head_inframe , width = 130 ,  bg = 'white', height = 1)
entryline.place(x = 540 , y = 395)

line = Frame(root, width = 450 , height = 1)
line.place(x =848 , y = 179)
billarea = Frame(root , width=500 , height= 550 )
billarea.place(x = 850 , y = 180)
label = Label(billarea , text = 'BILL AREA' , bg = 'black' , fg= 'yellow' , font = ('Poppins' , 12 , 'bold' ) , padx=180)
label.place(x = 0 , y = 0)

header_height = 30
bill_text = Text(billarea, height=header_height, width=55)
bill_text.place(x = 0 , y = 25)

bill_scrollbar = Scrollbar(root, command=bill_text.yview)
bill_scrollbar.pack(side=RIGHT, fill=Y)

bill_text.config(yscrollcommand=bill_scrollbar.set)


bill_no = random.randint(10000, 99999)
bill_text.insert(END , '\t\t**SHIVAY SUPERMART**\n\n')
bill_text.insert(END , f"  Bill Number : {bill_no}\n")
bill_text.insert(END , f"  Customer Name : {entry1.get()}\n")
bill_text.insert(END , f"  Phone Number : {entry2.get()}\n")
bill_text.insert(END , '\n\n  ==============================================\n')
bill_text.insert(END , '     Product        \t Quantity        \t Price\n')
bill_text.insert(END , '  ==============================================\n')
bill_text.config(state=DISABLED)

def after_clear_bill_area():
    global bill_text
    label = Label(billarea, text='BILL AREA', bg='black', fg='yellow', font=('Poppins', 12, 'bold'), padx=180)
    label.place(x=0, y=0)
    bill_text = Text(billarea, height=30, width=55)
    bill_text.place(x=0, y=25)

    bill_scrollbar = Scrollbar(root, command=bill_text.yview)
    bill_scrollbar.pack(side=RIGHT, fill=Y)

    bill_text.config(yscrollcommand=bill_scrollbar.set)

    bill_text.config(state=NORMAL)
    bill_text.delete(1.0, END)
    bill_text.insert(END, '\t\t**SHIVAY SUPERMART**\n\n')
    bill_text.insert(END, f"  Bill Number : {bill_no}\n")
    bill_text.insert(END, f"  Customer Name : {customer_name_var}\n")
    bill_text.insert(END, f"  Phone Number : {phone_number_var}\n")
    bill_text.insert(END, '\n\n  ==============================================\n')
    bill_text.insert(END, '     Product        \t Quantity        \t Price\n')
    bill_text.insert(END, '  ==============================================\n')
    customer_name_var.set("")
    phone_number_var.set("")

frame3 = Frame(root , width=850 , height= 500 , background='black')
frame3.place(x = 0 , y = 660)

def email():
    emailframe =  Frame(head_inframe , width=700, height=350 , bg= 'black')
    emailframe.place(x=20, y=15)

    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            attachment_path.set(file_path)
            attachment_label.config(text=f"Attached File: {file_path}")
            attachment_label.config(font=('Helvetica', 8, 'bold'))
            attachment_button.place(x = 570 , y = 258)

    def send_email():
        sender_email = sender_entry.get()
        sender_password = 'aazc vboy nxnq igoy'

        receiver_email = receiver_entry.get()
        subject = head_entry.get()
        body = body_entry.get("1.0", "end-1c")

        if sender_email=='' or receiver_email=='' or subject == '' or body == '':
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

            file_path = attachment_path.get()
            with open(file_path, 'rb') as file:
                attachment = MIMEApplication(file.read(), _subtype="txt")
                attachment.add_header('Content-Disposition', 'attachment', filename="attached_file.txt")
                msg.attach(attachment)
            msg.attach(MIMEText(body, 'plain'))
            server.sendmail(sender_email, receiver_email, msg.as_string())
            server.quit()
            messagebox.showinfo('Success!' , f"Email sent successfully to {receiver_email}")

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    sender_label = Label(emailframe, text="Sender's Gmail            :", bg = 'black' , fg = 'white' , font = ('Helvetica' , 12 , 'bold'))
    sender_label.place(x = 20 , y = 20)
    sender_entry = Entry(emailframe , bg = 'white' , fg = 'black' , width = 30 , font = ('Helvetica' , 10 , 'bold'))
    sender_entry.place(x = 250 , y = 20)
    sender_entry.insert(0, 'shivaysupermart0@gmail.com')

    receiver_label = Label(emailframe, text="Receiver's Gmail         :", bg='black', fg='white', font=('Helvetica', 12, 'bold'))
    receiver_label.place(x=20, y=50)
    receiver_entry = Entry(emailframe, bg='white', fg='black', width=30, font=('Helvetica', 10, 'bold'))
    receiver_entry.place(x=250, y=50)

    head_label = Label(emailframe, text="Heading                         :", bg='black', fg='white', font=('Helvetica', 12, 'bold'))
    head_label.place(x=20, y=80)
    head_entry = Entry(emailframe, bg='white', fg='black', width=50, font=('Helvetica', 10, 'bold'))
    head_entry.place(x=250, y=80)
    head_entry.insert(0, f"Hi {entry1.get()}")

    body_label = Label(emailframe, text="Body                               :", bg='black', fg='white', font=('Helvetica', 12, 'bold'))
    body_label.place(x=20, y=110)
    body_entry = Text(emailframe, height=7, width=50)
    body_entry.place(x=250, y=110)
    text = 'This is an auto generated copy of your bill. Please do not reply to this email. '
    body_entry.insert(1.0 , text)

    attachment_label = body_label = Label(emailframe, text="Attachment                          :", bg='black', fg='white', font=('Helvetica', 12, 'bold'))
    body_label.place(x=20, y=260)
    attachment_path = StringVar()
    attachment_button = Button(emailframe, text="Attach File", width= 12 , bg='white', fg='black', font=('Helvetica', 9, 'bold') ,command=browse_file)
    attachment_button.place(x = 370 , y =260)
    attachment_label = Label(emailframe, text="No file attached" , bg='black', fg='white', font=('Helvetica', 10, 'bold'))
    attachment_label.place(x = 250 , y = 260)


    send_email_button = Button(emailframe, text="Send Email", width = 12,  font=('Helvetica', 10, 'bold') , bg = 'white' , bd = 0, activebackground='white' , fg ='black' , activeforeground='black', command=send_email)
    send_email_button.place(x = 340 , y = 300)

    def cancel():
        emailframe.destroy()

    cancel_button = Button(emailframe, text="Cancel", width=12, font=('Helvetica', 10, 'bold'), bg='white', bd= 0,
                           activebackground='white', fg='black', activeforeground='black', command = cancel)
    cancel_button.place(x=450, y=300)

def savebill():
    ask = messagebox.askyesno('Save' , 'Do u want to save the bill ?')
    if ask == True:
        bill_content = bill_text.get("1.0", END)

        bill_number = bill_no
        save_directory = "C://Users//shiva//Desktop//Bills"
        if not os.path.exists(save_directory):
            os.makedirs(save_directory)
        file_path = os.path.join(save_directory, f"{bill_number}.txt")
        with open(file_path, "w") as file:
            file.write(bill_content)
        messagebox.showinfo('Saved', f"Bill saved successfully with Bill Number: {bill_number}")
    else:
        pass




def billkaro():
    if entry1.get() == '':
        messagebox.showerror('Error' , 'Enter Customer Name')
    elif entry2.get() == '':
        messagebox.showerror('Error' , 'Enter Phone Number')
    else:
        bill_text.config(state=NORMAL)
        bill_text.insert(END, ' \n  ==============================================\n')
        bill_text.insert(END , f"    Total Quantity: \t\t\t\t\t {aentry1.get()}\n")
        bill_text.insert(END , f"    Sub Total: \t\t\t\t\t {aentry2.get()}\n")
        bill_text.insert(END , f"    Total Tax: \t\t\t\t\t {aentry3.get()}\n")
        bill_text.insert(END , f"    Total: \t\t\t\t\t {aentry4.get()}\n")
        bill_text.insert(END, ' \n  ==============================================\n\n')
        bill_text.insert(END, '             **Thanks for Shopping**\n')
        bill_text.insert(END, '                 **Visit Again**\n\n')
        bill_text.config(state=DISABLED)
        bill_text.yview(END)
        savebill()

        query = 'use shivay_supermart'
        mycursor.execute(query)
        query = 'insert into customer (Customer_Name , Phone_Number) values (%s,%s)'
        mycursor.execute(query, [entry1.get(),entry2.get()])
        main_con.commit()
        main_con.close()

emailbutton = Button(head_inframe , text = 'Email' , width = 13 , fg = 'white' , bg = 'black' , activeforeground='white' , activebackground='black'  , font = ('Helvetica' , 10 , 'bold'), command = email)
emailbutton.place(x = 420 , y = 440)

savebutton = Button(head_inframe, text='Save', width=13, fg='white', bg='black', activeforeground='white',
activebackground='black', font=('Helvetica', 10, 'bold'), command = savebill)
savebutton.place(x=550, y=440)

billbutton = Button(head_inframe ,text = 'Bill' , width = 13 , fg = 'white' , bg = 'black' , activeforeground='black' , activebackground='white'  , font = ('Helvetica' , 10 , 'bold'), command = billkaro)
billbutton.place(x = 420 , y = 405)

clear_button = Button(head_inframe ,text = 'Clear' , width = 13 , fg = 'white' , bg = 'black' , activeforeground='white' , activebackground='black'  , font = ('Helvetica' , 10 , 'bold') , command = clearbutton)
clear_button.place(x = 550 , y = 405)

head3 = Label(frame , text= 'Bill Number : ' , bg = 'black' , fg = 'white' , font = ('Helvetica' , 12 , 'bold'))
head3.place(x = 870 , y = 5)
entry3 = Entry(frame , width= 20 , borderwidth=2 , font = ('Helvetica' , 12 , 'bold'))
entry3.place(x = 980 , y = 5)
search_button = Button(frame , text = 'Search' ,  width = 10  , bg = 'red' , fg = 'white' , activeforeground='white' , activebackground='firebrick2' , bd = 0 , font = ('Calibri' , 10 , 'bold'), command=bill_search)
search_button.place(x = 1180 , y = 6)


root.mainloop()