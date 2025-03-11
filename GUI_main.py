

from tkinter import *
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk


root = tk.Tk()

root.title("Plant Classification Using Deep Learning ")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

bg = Image.open("m3.jpg")

# bg.resize((1366,500),Image.ANTIALIAS)
# print(w,h)
bg_img = ImageTk.PhotoImage(bg)
bg_lbl = tk.Label(root, image=bg_img)
bg_lbl.place(x=0, y=93, relwidth=1, relheight=1)

'''
bg = PhotoImage(file="image3.jpg")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)
'''


img1 = ImageTk.PhotoImage(Image.open("m1.jpg"))

img2 = ImageTk.PhotoImage(Image.open("m2.jpg"))

img3 = ImageTk.PhotoImage(Image.open("m5.jpg"))

#img4 = ImageTk.PhotoImage(Image.open("img7.jpg"))

logo_label = tk.Label()
logo_label.place(x=60, y=250)

x = 1


def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img1)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
     # elif x ==4:
     #    logo_label.config(image=img4)
	x = x+1
	root.after(1000, move)

# calling the function
move()


#marquee
def shift():
    x1,y1,x2,y2 = canvas.bbox("marquee")
    if(x2<0 or y1<0): #reset the coordinates
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords("marquee",x1,y1)
    else:
        canvas.move("marquee", -2, 0)
    canvas.after(1000//fps,shift)

canvas=Canvas(root,bg="black")
canvas.pack()
text_var="Medicinal Plant Classification and Plant Prescription"
text=canvas.create_text(0,-2000,text=text_var,font=('Raleway',25,'bold'),fill='white',tags=("marquee",),anchor='w')
x1,y1,x2,y2 = canvas.bbox("marquee")
width = 1600
height = 100
canvas['width']=width
canvas['height']=height
fps=40    #Change the fps to make the animation faster/slower
shift()   #Function Calling





from tkinter import messagebox as ms


def Login():
    from subprocess import call
    call(["python","login.py"])
def Register():
    from subprocess import call
    call(["python","registration.py"])

'''
w,h = root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0"%(w,h))
root.configure(background="#17202A")
'''

wlcm=tk.Label(root,text="Medicinal Plant ",font=("Roboto",22,"bold"), bg='pink')
wlcm.place(x=330,y=270)




d2=tk.Button(root,text="Login",command=Login,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
d2.place(x=1100,y=350)


d3=tk.Button(root,text="Register",command=Register,width=20,height=2,bd=0,background="#17202A",foreground="white",font=("times new roman",14,"bold"))
d3.place(x=1100,y=450)




root.mainloop()
