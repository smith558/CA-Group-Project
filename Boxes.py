﻿import Tkinter
import tkMessageBox

main_window = Tkinter.Tk()

w = Tkinter.Label(main_window, text="Vs")
w.grid(row=1,column=10,)
f = Tkinter.Label(main_window, text="Vr")
f.grid(row=3,column=10)
g = Tkinter.Label(main_window, text="Vl")
g.grid(row=5,column=10)
h = Tkinter.Label(main_window, text="Vc")
h.grid(row=7,column=10)
e = Tkinter.Label(main_window, text="Xc")
e.grid(row=9,column=10)
i = Tkinter.Label(main_window, text="Xl")
i.grid(row=11,column=10)
a = Tkinter.Label(main_window, text="R")
a.grid(row=1,column=17)
b = Tkinter.Label(main_window, text="Z")
b.grid(row=3,column=17)
c = Tkinter.Label(main_window, text="f")
c.grid(row=5,column=17)
d = Tkinter.Label(main_window, text="C")
d.grid(row=7,column=17)
j = Tkinter.Label(main_window, text="L")
j.grid(row=9,column=17)
k = Tkinter.Label(main_window, text="θ")
k.grid(row=11,column=17)

m = Tkinter.Label(main_window, text="V")
m.grid(row=1,column=12,)
l = Tkinter.Label(main_window, text="V")
l.grid(row=3,column=12)
z = Tkinter.Label(main_window, text="V")
z.grid(row=5,column=12)
t = Tkinter.Label(main_window, text="V")
t.grid(row=7,column=12)
y = Tkinter.Label(main_window, text="Ω")
y.grid(row=9,column=12)
o = Tkinter.Label(main_window, text="Ω")
o.grid(row=11,column=12)
p = Tkinter.Label(main_window, text="Ω")
p.grid(row=1,column=19)
s = Tkinter.Label(main_window, text="Ω")
s.grid(row=3,column=19)
q = Tkinter.Label(main_window, text="Hz")
q.grid(row=5,column=19)
x = Tkinter.Label(main_window, text="H")
x.grid(row=7,column=19)
u = Tkinter.Label(main_window, text="F")
u.grid(row=9,column=19)
v = Tkinter.Label(main_window, text="°")
v.grid(row=11,column=19)

name = Tkinter.Entry(main_window)
name.grid(row=1,column=11)
name = Tkinter.Entry(main_window)
name.grid(row=3,column=11)
name = Tkinter.Entry(main_window)
name.grid(row=5,column=11)
name = Tkinter.Entry(main_window)
name.grid(row=7,column=11)
name = Tkinter.Entry(main_window)
name.grid(row=9,column=11)
name = Tkinter.Entry(main_window)
name.grid(row=11,column=11)
name = Tkinter.Entry(main_window)
name.grid(row=1,column=18)
name = Tkinter.Entry(main_window)
name.grid(row=3,column=18)
name = Tkinter.Entry(main_window)
name.grid(row=5,column=18)
name = Tkinter.Entry(main_window)
name.grid(row=7,column=18)
name = Tkinter.Entry(main_window)
name.grid(row=9,column=18)
name = Tkinter.Entry(main_window)
name.grid(row=11,column=18)

hello = Tkinter.Button(main_window, text="Calculator",)
hello.grid(row=13,column=14)

main_window.mainloop()