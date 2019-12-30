from tkinter import *
window = Tk()
window.title("First Gui")
window.geometry("500x500+400+0")

array=["sad","hat", "tae"]

def btn_code():
    random_str.set(str(array))

btn_var = StringVar()
btn_var.set("click me")



btn1 = Button(window, textvariable=btn_var, command= btn_code)
btn1.pack()

random_str = StringVar()
random_str.set("Hi this is Label")
lbl=Label(window, textvariable=random_str)
lbl.place(x=250,y=250, anchor= CENTER)


ent_var = StringVar()
entry_box= Entry(window,textvariable=ent_var)
entry_box.pack()

window.mainloop()