import tkinter as tk

def button_click(value):
    textColm.insert(tk.END, str(value))

def backspace():
    textColm.delete(len(textColm.get())-1,'end')
    
def cleartxt():
    textColm.delete(0,'end')

def solveBtn():
    #for error handling
    try:
        n=eval(textColm.get())
        cleartxt()
        button_click(n)
    except Exception as e:
        errorScreen = tk.Tk()
        errorScreen.title("Error")
        errorLabel=tk.Label(errorScreen,text=str(e))
        errorLabel.pack()
        errorScreen.mainloop()



root = tk.Tk()
root.title("Simple Calculator")
textColm = tk.Entry(root, width=20)
textColm.grid(row=0, column=1, columnspan=2)
cButton=tk.Button(root,text='C',height=3,width=10,command=cleartxt).grid(row=0,column=0)

lst = []
a = 1
# Create buttons from 1-9
for i in range(3):
    lst2 = []
    for j in range(3):
        btn = tk.Button(root, text=str(a), height=3, width=10, command=lambda val=a: button_click(val))
        btn.grid(row=i+1, column=j)
        lst2.append(btn)
        a += 1
    lst.append(lst2)

subButton=tk.Button(root,text='-',height=3,width=10,command=lambda val='-': button_click(val)).grid(row=1,column=3)

addButton=tk.Button(root,text='+',height=3,width=10,command=lambda val='+': button_click(val)).grid(row=2,column=3)

mulButton=tk.Button(root,text='*',height=3,width=10,command=lambda val='*': button_click(val)).grid(row=3,column=3)

divButton=tk.Button(root,text='/',height=3,width=10,command=lambda val='/': button_click(val)).grid(row=4,column=3)

backButton=tk.Button(root,text='<-',height=3,width=10,command=backspace).grid(row=0,column=3)

eqlButton=tk.Button(root,text='=',height=3,width=10,command=solveBtn).grid(row=4,column=2)

zeroButton=tk.Button(root,text='0',height=3,width=10,command=lambda val='0': button_click(val)).grid(row=4,column=1)

decButton=tk.Button(root,text='.',height=3,width=10,command=lambda val='.': button_click(val)).grid(row=4,column=0)

root.mainloop()
