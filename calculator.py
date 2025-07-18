from tkinter import *

root = Tk()
root.title('Simple_Calculator')
root.geometry('570x600+100+200')
root.resizable(False,False)
root.configure(bg='#17161b')

equation= ""

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation=""
    label_result.config(text=equation)

def calculate():
    global equation
    result=""
    if equation != "":
        try:
            result=eval(equation)
        except:
            result="error"
            equation=""
    label_result.config(text=result)


label_result=Label(root,width=32,height=2,text='',font=('arial',30))
label_result.pack()


Button(root,text='c',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='#2a75f7',fg='white',command=lambda: clear()).place(x=10,y=100)
Button(root,text='/',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('/')).place(x=150,y=100)
Button(root,text='%',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('%')).place(x=290,y=100)
Button(root,text='*',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('*')).place(x=430,y=100)

Button(root,text='7',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('7')).place(x=10,y=200)
Button(root,text='8',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('8')).place(x=150,y=200)
Button(root,text='9',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('9')).place(x=290,y=200)
Button(root,text='-',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('-')).place(x=430,y=200)

Button(root,text='4',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('4')).place(x=10,y=300)
Button(root,text='5',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('5')).place(x=150,y=300)
Button(root,text='6',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('6')).place(x=290,y=300)
Button(root,text='+',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('+')).place(x=430,y=300)

Button(root,text='1',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('1')).place(x=10,y=400)
Button(root,text='2',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('2')).place(x=150,y=400)
Button(root,text='3',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('3')).place(x=290,y=400)
Button(root,text='0',width=13,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('0')).place(x=10,y=500)

Button(root,text='.',width=5,height=2,font=('arial',30,"bold"),bd=1,bg='gray',fg='white',command=lambda: show('.')).place(x=290,y=500)
Button(root,text='=',width=5,height=5,font=('arial',30,"bold"),bd=1,bg='#ff5f03',fg='white',command=lambda: calculate()).place(x=430,y=400)
root.mainloop()
