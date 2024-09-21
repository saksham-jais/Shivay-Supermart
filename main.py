from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from PIL import Image , ImageTk
root = Tk()

img = ImageTk.PhotoImage(Image.open('loading grocery logo.png'))

root.iconbitmap('logo.ico')
height = 430
width = 460
x = (root.winfo_screenwidth()//2)- (width//2)
y = (root.winfo_screenheight()//2)- (height//2)
root.maxsize(width= 460 , height = 430)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(True)

root.config(background= '#2F6C60')
welcome_label1 = Label(root , text = 'WELCOME TO' , background = '#2F6C60' , font  = ('Microsoft Yahei UI Light' , 15 , 'bold') , foreground= '#ffffff')
welcome_label1.place(x = 160 , y = 20)
welcome_label2 = Label(root , text = 'SHIVAY SUPERMART' , background = '#2F6C60' , font  = ('Open Sans' , 17 , 'bold') , foreground= '#ffffff' )
welcome_label2.place(x = 117 , y = 50)
bg_label = Label(root,image= img , background = '#2F6C60')
bg_label.place(x = 78 , y = 75)

progress_label = Label(root, text='Loading...', font = ('Trebuhet MS' , 15 , 'bold') , foreground = '#ffffff' , background = '#2F6C60')
progress_label.place(x = 160 , y = 335)


progress = ttk.Style()
progress.theme_use('clam')
progress.configure('red.Horizontal.TProgressbar' , background = '#108cff')
progress = Progressbar(root , orient = HORIZONTAL , length = 400 , mode = 'determinate' , style = 'red.Horizontal.TProgressbar')
progress.place(x = 28 , y = 370)

def top():
    try:
        root.destroy()
        import signuppage
        root.withdraw()
    except :
        pass
i = 0

def load():
    global i
    if i <= 10:
        txt = 'Loading...' + (str(10*i)+'%')
        progress_label.configure(text=txt)
        progress_label.after(600 , load)
        progress['value'] = 10*i
        i +=1
    else:
        top()


load()
root.resizable(False,False)
root.mainloop()