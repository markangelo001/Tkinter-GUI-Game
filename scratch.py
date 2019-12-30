from tkinter import *
from winsound import *
window = Tk()
#mainStucture of the tkinter
window.title("Mickey Quiz")
window.resizable(width= False , height = FALSE)
window.geometry("500x620+400+0")
#Insert ng mga Photos sa TKinter
photo1 =PhotoImage(file="background1.png")
photo2 =PhotoImage(file="start2.png")
photo3 =PhotoImage(file="quit1.png")
quest1 =PhotoImage(file="quest1.png")
quest2 =PhotoImage(file="quest2.png")
quest3 =PhotoImage(file="quest3.png")
quest4 =PhotoImage(file="quest4.png")
quest5 =PhotoImage(file="quest5.png")
quest6 =PhotoImage(file="quest6.png")
quest7 =PhotoImage(file="quest7.png")
quest8 =PhotoImage(file="quest8.png")
quest9 =PhotoImage(file="quest9.png")
quest10=PhotoImage(file="quest10.png")
result1= PhotoImage(file="result.png")
next=PhotoImage(file="next.png")
back=PhotoImage(file="back.png")
play = lambda: PlaySound('Sound1.wav', SND_FILENAME)
#Ano Size nila pag ka insert
Label(window, image= photo1, width=510).grid(row=1, columnspan=1) #lalagay para mag display .grid


#Commands

data=[]
data.sort(reverse = True)   
ans10 = StringVar()
def endplay():
    global ans20
    Label(window,)
    entry11=Entry(window,)
    ans20=str(ans10.get())
    print(ans20)

ans9= StringVar()
def play10():
    global ans19
    Label(window,image=quest10,width=510).grid(row=1, columnspan=1)
    entry10=Entry(window,textvariable=ans10,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=totalresult).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold",command=play9).place(x=200, y=550)
    ans19=str(ans9.get())
    print(ans19)


ans8= StringVar()
def play9():
    global ans18
    Label(window,image=quest9,width=510).grid(row=1, columnspan=1)
    entry8=Entry(window,textvariable=ans9,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play10).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold",command=play8).place(x=200, y=550)
    ans18=str(ans8.get())
    print(ans18)
    

ans7= StringVar() #Question 8
def play8():
    global ans17
    Label(window,image=quest8,width=510).grid(row=1, columnspan=1)
    entry7=Entry(window,textvariable=ans8,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play9).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold", command=play7).place(x=200, y=550)
    ans17=str(ans7.get())
    print(ans17)
ans6= StringVar()
def play7(): 
    global ans16
    Label(window,image=quest7,width=510).grid(row=1, columnspan=1)
    entry6=Entry(window,textvariable=ans7,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play8).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold", command=play6).place(x=200, y=550)
    ans16=str(ans6.get())
    print(ans16)


ans5= StringVar()
def play6(): #Question 6
    global ans15
    Label(window,image=quest6,width=510).grid(row=1, columnspan=1)
    entry6=Entry(window,textvariable=ans6,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play7).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold", command=play5).place(x=200, y=550)
    ans15=str(ans5.get())
    print(ans15)

ans4= StringVar()
def play5():    #quest 5
    global ans14
    Label(window,image=quest5,width=510).grid(row=1, columnspan=1)
    entry5=Entry(window,textvariable=ans5,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play6).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold", command=play4).place(x=200, y=550)
    ans14=str(ans4.get())
    print(ans14)

ans3 = StringVar()

def play4():#quest4
    global ans13
    Label(window,image=quest4,width=510).grid(row=1, columnspan=1)
    entry4=Entry(window,textvariable=ans4,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold", command=play5).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold", command=play3).place(x=200, y=550)
    ans13=str(ans3.get())
    print(ans13)

ans2 = StringVar()
def play3():#Question 3
    global ans12
    Label(window,image=quest3,width=510).grid(row=1, columnspan=1)
    entry3=Entry(window,textvariable=ans3,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play4).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold", command=play2).place(x=200, y=550)
    ans12=str(ans2.get())
    print(ans12)

ans1 = StringVar()
def play2():#Question 2
    global ans11
    Label(window,image=quest2,width=510).grid(row=1, columnspan=1)
    entry2=Entry(window,textvariable=ans2,width=15, font=("arial, 24"), bg="light blue").grid(row=1, columnspan=1)   
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play3).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold", command=play).place(x=200, y=550)
    ans11= str(ans1.get())
    print(ans11)

ans11= str(ans1.get())
def totalresult():
    Label(window,image=result1,width=510).grid(row=1, columnspan=1)
    endplay()
    back2= Button(window, image= back, width=90, height=35 ,bg="gold",command=main).place(x=200, y=550)
    
    score = 0
    if ans11 == "18":
        score = score + 1
    if ans12 == "10":
        score = score + 1
    if ans13 == "2":
        score = score + 1
    if ans14 == "0":
        score = score + 1
    if ans15 == "1":
        score = score + 1
    if ans16 == "2":
        score = score + 1
    if ans17 == "8":
        score = score + 1
    if ans18 == "1000":
        score = score + 1
    if ans19 == "3546":
        score = score + 1
    if ans20 == "206":
        score = score + 1
    
    global data
    data.append(score)
    display1 = StringVar()
    display1.set(str(data))
    labl = Label(window, textvariable=display1,bg="yellow",fg="blue")
    labl.place(x=250,y=350)
    Label(window, text="Your Score List ",bg="yellow",font=("tamora 10"),fg="blue").place(x=150, y=350) 
    a= StringVar()
    print(score)
    print(data)
    for a in data:
        a.set(str(a))
        labl = Label(window, textvariable=a,bg="yellow",fg="blue")

    if score == 0:
        Label(window, text="0",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score== 1:
        Label(window, text="1",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 

    elif score ==2:
        Label(window, text="2",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==3:
        Label(window, text="3",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==4:
        Label(window, text="4",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==5:
        Label(window, text="5",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==6:
        Label(window, text="6",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==7:
        Label(window, text="7",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==8:
        Label(window, text="8",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==9:
        Label(window, text="9",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 
    elif score ==10:
        Label(window, text="10",bg="yellow",font=("tamora 50"),fg="blue").place(x=250, y=190) 






    
#Question 1 yung tanong nasa picture pao a ra maganda edit

def play():
    global score
    Label(window,image=quest1,width=510).grid(row=1, columnspan=1)
    entry1= Entry(window,textvariable=ans1,width=15, font=("arial, 24"),bg="light blue").grid(row=1, columnspan=1)
    next1= Button(window, image= next, width=90, height=35 ,bg="gold",command=play2).place(x=200, y=370)
    back2= Button(window, image= back, width=90, height=35 ,bg="gold",command=main).place(x=200, y=550)

#display ng total score


#QUit
def exitProgram():
    window.destroy()
#Mainwindow if Return


def main():
    Label(window, image= photo1, width=510).grid(row=1, columnspan=1)
    start = Button(window, image= photo2, width=90, height=35 ,bg="yellow",command=play).place(x=20, y=400)
    exit = Button(window, image= photo3, width=90, height=30, bg="dark green", command=exitProgram).place(x=10, y=500)

#Menu Botton
start = Button(window, image= photo2, width=90, height=35 ,bg="yellow",command=play).place(x=20, y=400)
exit = Button(window, image= photo3, width=90, height=30, bg="dark green", command=exitProgram).place(x=10, y=500)

window.mainloop()
