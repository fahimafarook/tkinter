from tkinter import*
from tkinter import messagebox

root=Tk()
root.title("calculator")
root.geometry("250x350")

operator=""
text_input=StringVar()
row1=Frame(root,bg="grey")
row1.pack(expand=True,fill="both")
row2=Frame(root,bg="blue")
row2.pack(expand=True,fill="both")
row3=Frame(root,bg="yellow")
row3.pack(expand=True,fill="both")
row4=Frame(root,bg="black")
row4.pack(expand=True,fill="both")
row5=Frame(root,bg="black")
row5.pack(expand=True,fill="both")

text_disp=Entry(row1,textvariable=text_input,font=("teletype",18),justify="right")
text_disp.pack(expand=True,fill="both")

def which_is_pressed(val):
    global operator
    if(val==15):
        max = -1000000
        i = sum = 0
        s = operator
        s = '+' + s
        l = len(s) - 1
        while (i < l):
            if (s[i] == '+'):
                sum = sum + int(s[i + 1])
            else:
                 sum = sum - int(s[i + 1])
            i = i + 2
        if sum > max:
            max = sum
        print(max)
        operator=max
        text_input.set(operator)
    elif(val==14):
        temp=""
        temp=operator
        l=(len(temp))-1
        operator=""
        operator=temp[0:l]
        text_input.set(operator)
    elif(val == 10):
        operator = operator + '+'
        text_input.set(operator)
    elif (val == 11):
        operator = operator + '-'
        text_input.set(operator)
    elif (val == 12):
        operator = operator + '*'
        text_input.set(operator)
    elif (val == 13):
        operator = operator + '/'
        text_input.set(operator)
    else:
        operator=operator+str(val)
        text_input.set(operator)
    if(val==1):
        print(1)
    elif(val==2):
        print(2)
    elif (val == 3):
        print(3)
    elif (val == 4):
        print(4)
    elif (val == 5):
        print(5)
    elif (val == 6):
        print(6)
    elif (val == 7):
        print(7)
    elif (val == 8):
        print(8)
    elif (val == 9):
        print(9)
one= Button(row2, text="1", font=("teletype",18),command=lambda:which_is_pressed(1), activeforeground="red", activebackground="pink",bg="black",fg="white",relief=GROOVE,border=0,)
two= Button(row2, text="2", font=("teletype",18),command=lambda:which_is_pressed(2), activeforeground="red", activebackground="pink",bg="black",fg="white",relief=GROOVE,border=0)
three= Button(row2, text="3", font=("teletype",18),command=lambda:which_is_pressed(3), activeforeground="red", activebackground="pink",bg="black",fg="white",relief=GROOVE,border=0)
four= Button(row3, text="4", font=("teletype",18),command=lambda:which_is_pressed(4), activeforeground="red", activebackground="pink", bg="black",fg="white",relief=GROOVE,border=0)
five= Button(row3, text="5", font=("teletype",18),command=lambda:which_is_pressed(5), activeforeground="red", activebackground="pink", bg="black",fg="white",relief=GROOVE,border=0)
six= Button(row3, text="6", font=("teletype",18),command=lambda:which_is_pressed(6), activeforeground="red", activebackground="pink", bg="black",fg="white",relief=GROOVE,border=0)
seven= Button(row4 ,text="7",font=("teletype",18), command=lambda:which_is_pressed(7), activeforeground="red", activebackground="pink",bg="black",fg="white",relief=GROOVE,border=0)
eight= Button(row4, text="8",font=("teletype",18), command=lambda:which_is_pressed(8), activeforeground="red", activebackground="pink",bg="black",fg="white",relief=GROOVE,border=0)
nine= Button(row4, text="9", font=("teletype",18),command=lambda:which_is_pressed(9), activeforeground="red", activebackground="#616D7E",bg="black",fg="white",relief=GROOVE,border=0)
plus= Button(row2, text="+", font=("teletype",18),command=lambda:which_is_pressed(10), activeforeground="red", activebackground="pink", bg="black",fg="white",relief=GROOVE,border=0)
minus= Button(row3, text="-",font=("teletype",18), command=lambda:which_is_pressed(11), activeforeground="red", activebackground="pink",bg="black",fg="white",relief=GROOVE,border=0)
mul= Button(row4, text="*", font=("teletype",18),command=lambda:which_is_pressed(12), activeforeground="red", activebackground="pink", bg="black",fg="white",relief=GROOVE,border=0)
divide= Button(row5, text="/", font=("teletype",18),command=lambda:which_is_pressed(13), activeforeground="red", activebackground="pink", bg="black",fg="white",relief=GROOVE,border=0)
clear= Button(row5, text="c", font=("teletype",18),command=lambda:which_is_pressed(14), activeforeground="red", activebackground="pink",bg="#2C090A",fg="white",relief=GROOVE,border=0)
equal= Button(row5, text="=",font=("teletype",18), command=lambda:which_is_pressed(15), activeforeground="red", activebackground="pink",bg="#2c3539",fg="white",relief=GROOVE,border=0)
zero= Button(row5, text="0", font=("teletype",18),command=lambda:which_is_pressed(0), activeforeground="red", activebackground="pink",bg="black",fg="white",relief=GROOVE,border=0)
#text1.grid(row=1,column=1)
'''
one.grid(row=2,column=1)
two.grid(row=2,column=2)
three.grid(row=2,column=3)0
four.grid(row=3,column=1)
five.grid(row=3,column=2)
six.grid(row=3,column=3)
seven.grid(row=4,column=1)
eight.grid(row=4,column=2)
nine.grid(row=4,column=3)
'''
one.pack(side="left",expand=True,fill="both")
two.pack(side="left",expand=True,fill="both")
three.pack(side="left",expand=True,fill="both")
plus.pack(side="left",expand=True,fill="both")

four.pack(side="left",expand=True,fill="both")
five.pack(side="left",expand=True,fill="both")
six.pack(side="left",expand=True,fill="both")
minus.pack(side="left",expand=True,fill="both")

seven.pack(side="left",expand=True,fill="both")
eight.pack(side="left",expand=True,fill="both")
nine.pack(side="left",expand=True,fill="both")
mul.pack(side="left",expand=True,fill="both")

clear.pack(side="left",expand=True,fill="both")
zero.pack(side="left",expand=True,fill="both")
equal.pack(side="left",expand=True,fill="both")
divide.pack(side="left",expand=True,fill="both")
mainloop()

