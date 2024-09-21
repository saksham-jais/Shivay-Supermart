class ScrollBar:
    def __init__(self):
        root = Tk()
        v = Scrollbar(root)
        v.pack(side=RIGHT, fill=Y)
        t = Text(root, width=15, height=15, wrap=NONE,
                 xscrollcommand=h.set,
                 yscrollcommand=v.set)
        for i in range(20):
            t.insert(END, "this is some text\n")
        t.pack(side=TOP, fill=X)
        h.config(command=t.xview)
        v.config(command=t.yview)
        root.mainloop()
s = ScrollBar()

