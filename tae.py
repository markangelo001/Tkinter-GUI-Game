from tkinter import *

window = Tk()

window.title("Hatdog")
window.geometry("500x600+400+0")

def exit1():
    window.destroy()

def back():
    text.place(x= 130, y=200)
    play.place(x= 150, y= 300)
    exit.place(x=150, y=350)
    ex1.destroy()

def start():
    play.destroy() 
    exit.destroy()
    text.place_forget()
    ex1= Button(window, text="back", width=20, bg="Yellow", command=quest)
    ex1.place(x= 250, y= 300)
    
def quest():
    main = Label(window,bg="lightblue", width=500, height= 600)
    main.pack()
    ex= Button(window, text="Play", width=20, bg="Yellow", command=back)
    ex.place(x= 150, y= 300)


main = Label(window,bg="lightblue", width=500, height= 600).pack()
text = Label(window, text=" Let's Go", font=("Arial, 40"))
text.place(x= 130, y=200)
play= Button(window, text="Play", width=20, bg="Yellow", command=start)
play.place(x= 150, y= 300)
exit = Button(window, text="Exit", width=20, bg="red", command=exit1)
exit.place(x=150, y=350)
window.mainloop()