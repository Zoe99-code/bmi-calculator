import tkinter as tk
from tkinter import *

root = tk.Tk()

root.title("BMI Calculator")

root.geometry("900x300")

frame1 = Frame(root, width="300", height="100", bd="2", relief="flat")
frame1.pack()
frame2 = Frame(root, width="300", height="100", bd="2", relief="raised")
frame2.pack()
frame3 = Frame(root, width="300", height="100", bd="2", relief="raised")
frame3.pack()


genderoptions = ["Select Gender", "Male", "Female"]

value_inside = StringVar(root)

value_inside.set("select gender")


def maleidealbmi():
    res2 = 0.5 * w.get() / ((h.get()/100)**2) + 11.5


def femaleidealbmi():
    res3 = 0.5 * w.get()/((h.get()/100)**2) + 0.03 * a.get() + 11


label = Label(frame1, text='Calculate your BMI')
label.pack()
lweight = Label(frame2, text="Weight in Kg:")
lweight.pack()
lheight = Label(frame2, text="Height in cm:")
lheight.pack()
lgender = Label(frame2, text="Gender:")
lgender.pack()
lage = Label(frame2, text="Age:")
lage.pack()

w = Entry(frame2)
w.pack()

h = Entry(frame2)
h.pack()

gender = OptionMenu(frame2, value_inside, *genderoptions)
gender.pack(side=TOP)

a = Entry(frame2)
a.pack()


def bmi():
    try:
        float(w.get())
        float(h.get())
        float(a.get())
        if value_inside.get() == "Select Gender":
            raise ValueError
        elif value_inside.get() == "Male":
            res = ((0.5 * float(w.get())) / ((float(h.get())/100) **2)) + 11.5
            res = round(res, 1)
            ibmispace.config(state='normal')
            ibmispace.insert(0, res)
            ibmispace.config(state='readonly')
            resbmi = float(w.get()) / ((float(h.get())/100) **2)
            resbmi = round(resbmi, 1)
            bmispace.config(state="normal")
            bmispace.insert(0, resbmi)
            bmispace.config(state='readonly')
        elif value_inside.get() == "Female":
            res = ((0.5 * float(w.get())) / ((float(h.get()) / 100) ** 2)) + (
                        0.03 * float(a.get())) + 11
            res = round(res, 1)
            ibmispace.config(state='normal')
            ibmispace.insert(0, res)
            ibmispace.config(state='readonly')
            resbmi = float(w.get()) / ((float(h.get()) / 100) ** 2)
            resbmi = round(resbmi, 1)
            bmispace.config(state="normal")
            bmispace.insert(0, resbmi)
            bmispace.config(state='readonly')
        if resbmi < 18.5:
            bmidesc.config(text="Underweight")
        elif 18.5 <= resbmi < 25:
            bmidesc.config(text="Healthy")
        elif 25 <= resbmi < 30:
            bmidesc.config(text="Overweight")
        elif resbmi >= 30:
            bmidesc.config(text="Obese")
    except ValueError:
        error = Label(frame3, text="error")


result = Button(frame3, text="Your BMI", command=bmi)
result.pack()

bmil = Label(frame3, text="BMI")
bmil.pack()
bmispace = Entry(frame3, state='readonly')
bmispace.pack()
ibmi = Label(frame3, text="Ideal BMI")
ibmi.pack()
ibmispace = Entry(frame3, state='readonly')
ibmispace.pack()
bmides = Label(frame3, text="You are:")
bmides.pack()
bmidesc = Entry(frame3)
bmidesc.pack()


def delete():
    w.delete(0, END)
    h.delete(0, END)
    a.delete(0, END)
    bmispace.delete(0, END)
    ibmispace.delete(0, END)
    gender.config(value_inside.set(genderoptions[0]))
    bmidesc.delete(0, END)


clear = Button(frame3, text="clear", command=delete)
clear.pack()


root.mainloop()