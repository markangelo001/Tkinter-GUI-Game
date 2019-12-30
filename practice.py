from tkinter import *

window = Tk()
window.title("Mickey Quiz")
window.resizable(width= False , height = FALSE)
window.geometry("500x620+400+0")
photo1 =PhotoImage(file="result.png")

Label(window, image= photo1, width=510).grid(row=1, columnspan=1) #lalagay para mag display .grid
Label(window, text="3",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) #lalagay para mag display .grid

window.mainloop()