from tkinter import*
from tkinter import ttk
import tkinter.messagebox


store_cn = []
store_p = []

store_ca1 = []
store_fp1 = []
store_po1 = []
store_cno1 = []

store_i1 = []
store_j1 = []
store_i2 = []
store_j2 = []
store_i3 = []
store_j3 = []
store_i4 = []
store_j4 = []

#Applicant's Details

store_fn_js = []
store_pw_js = []
store_a_js = []
store_ds = []
store_cno2 = []

def vacancies():
    vscreen = Toplevel()
    vscreen.title("REGISTER")
    vscreen.geometry("1366x768+0+0")
    vscreen.resizable(width=FALSE, height=FALSE)
    vscreen.configure(background='powder blue')

    Label(vscreen, text="JOB VACANCIES PORTAL", font = ("Bahnschrift", 20, "bold"), bg = "powder blue", fg = "navy blue").place(rely=.1, relx=.5, anchor=CENTER)

    Label(vscreen, text="COMPANY 1:", font=("Bahnschrift", 12, "bold"), bg="powder blue",fg="navy blue").place(rely=.2, relx=.1)
    store_cn[1].place(rely=.2, relx=.13)

def sign_up():
    suscreen = Toplevel()
    suscreen.title("REGISTER")
    suscreen.geometry("1366x768+0+0")
    suscreen.resizable(width=FALSE, height=FALSE)
    suscreen.configure(background='powder blue')

    scrollbar = Scrollbar(suscreen)
    scrollbar.pack(side=RIGHT, fill=Y)

# Registration Form for Employers

    company_name = StringVar()
    password_cn = StringVar()
    company_address = StringVar()
    focal_person = StringVar()
    position = StringVar()
    contact_no = IntVar()

    vacancy_slot1 = IntVar()
    positions1 = StringVar()
    vacancy_slot2 = IntVar()
    positions2 = StringVar()
    vacancy_slot3 = IntVar()
    positions3 = StringVar()
    vacancy_slot4 = IntVar()
    positions4 = StringVar()

    Label(suscreen, text="Registration Form for Employer", font = ("Bahnschrift", 15, "bold"), bg = "powder blue", fg = "navy blue").place(rely=.05, relx=.5, anchor=CENTER)

    Label(suscreen, text = "Company Name:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.1,relx=.2, anchor = CENTER)
    cn = Entry(suscreen, textvariable = company_name, width = 40)
    cn.place(rely=.1,relx=.34, anchor = CENTER)

    Label(suscreen, text = "Company Address:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.15,relx=.2, anchor = CENTER)
    ca1 = Entry(suscreen, textvariable = company_address, width = 40)
    ca1.place(rely=.15,relx=.34, anchor = CENTER)

    Label(suscreen, text = "Focal Person/HR:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.20,relx=.2, anchor = CENTER)
    fp1 = Entry(suscreen, textvariable = focal_person, width = 40)
    fp1.place(rely=.20,relx=.34, anchor = CENTER)

    Label(suscreen, text = "Position:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.25,relx=.2, anchor = CENTER)
    po1 = Entry(suscreen, textvariable = position, width = 40)
    po1.place(rely=.25,relx=.34, anchor = CENTER)

    Label(suscreen, text = "Contact Number:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.30,relx=.2, anchor = CENTER)
    cno1 = Entry(suscreen, textvariable = contact_no, width = 40)
    cno1.place(rely=.30,relx=.34, anchor = CENTER)

    Label(suscreen, text = "Password:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.35,relx=.2, anchor = CENTER)
    p = Entry(suscreen, show="•", textvariable = password_cn, width = 40)
    p.place(rely=.35,relx=.34, anchor = CENTER)

    Label(suscreen, text = "Job Vacancies", font = ("Bahnschrift", 10, "bold",), bg = "powder blue", fg = "black").place(rely=.10,relx=.6, anchor = CENTER)
    Label(suscreen, text = "No. of Vacancies:", font = ("Bahnschrift", 10, "bold",), bg = "powder blue", fg = "black").place(rely=.15,relx=.54, anchor = CENTER)
    Label(suscreen, text = "Positions:", font = ("Bahnschrift", 10, "bold",), bg = "powder blue", fg = "black").place(rely=.15,relx=.64, anchor = CENTER)

    i1 = Entry(suscreen, textvariable = vacancy_slot1, width = 10)
    i1.place(rely=.20,relx=.54, anchor = CENTER)

    j1 = Entry(suscreen, textvariable = positions1, width = 40)
    j1.place(rely=.20,relx=.68, anchor = CENTER)

    i2 = Entry(suscreen, textvariable = vacancy_slot2, width = 10)
    i2.place(rely=.25,relx=.54, anchor = CENTER)

    j2 = Entry(suscreen, textvariable = positions2, width = 40)
    j2.place(rely=.25,relx=.68, anchor = CENTER)

    i3 = Entry(suscreen, textvariable = vacancy_slot3, width = 10)
    i3.place(rely=.30,relx=.54, anchor = CENTER)

    j3 = Entry(suscreen, textvariable = positions3, width = 40)
    j3.place(rely=.30,relx=.68, anchor = CENTER)

    i4 = Entry(suscreen, textvariable = vacancy_slot4, width = 10)
    i4.place(rely=.35,relx=.54, anchor = CENTER)

    j4 = Entry(suscreen, textvariable = positions4, width = 40)
    j4.place(rely=.35,relx=.68, anchor = CENTER)

    cn = company_name.get()
    p = password_cn.get()
    ca1 = company_address.get()
    store_ca1.append(ca1)
    fp1 = focal_person.get()
    store_fp1.append(fp1)
    po1 = position.get()
    store_po1.append(po1)
    cno1 = contact_no.get()
    store_cno1.append(cno1)

    i1 = vacancy_slot1.get()
    store_i1.append(i1)
    j1 = positions1.get()
    store_j1.append(j1)
    i2 = vacancy_slot2.get()
    store_i2.append(i2)
    j2 = positions2.get()
    store_j2.append(j2)
    i3 = vacancy_slot3.get()
    store_i3.append(i3)
    j3 = positions3.get()
    store_j3.append(j3)
    i4 = vacancy_slot4.get()
    store_i4.append(i4)
    j4 = positions4.get()
    store_j4.append(j4)

    def store_employer():
        register_e = Toplevel()
        register_e.title("Registration Result")
        register_e.geometry("300x300+0+0")
        register_e.resizable(width=FALSE, height=FALSE)
        register_e.configure(background='powder blue')

        if cn in store_cn:
            Button(register_e, text="Company name already exist!", height=2, width=30, font=("Bahnschrift", 10, "bold",), bg="light green",fg="red", command=suscreen).place(relx=.5, rely=.55, anchor=CENTER)

        else:
            store_cn.append(cn)
            store_p.append(p)
            Button(register_e, text="Registration Success!", height=2, width=30, font=("Bahnschrift", 10, "bold",),bg="light green", fg="navy blue", command=log_in_e).place(relx=.5, rely=.5, anchor=CENTER)
            suscreen.destroy()

    Button(suscreen, text = "REGISTER AS EMPLOYER", height = 2, width = 30, font = ("Bahnschrift", 10, "bold",), bg = "light green", fg = "navy blue", command = store_employer).place(relx =.5, rely = .42, anchor = CENTER)

#Registration Form for Job-seekers

    full_name = StringVar()
    password_js = StringVar()
    address_js = StringVar()
    desired_position = StringVar()
    contact_no2 = IntVar()

    Label(suscreen, text="Registration Form for Job-seeker", font = ("Bahnschrift", 15, "bold"), bg = "powder blue", fg = "navy blue").place(rely=.55, relx=.50, anchor=CENTER)

    Label(suscreen, text = "Full Name:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.60,relx=.4, anchor = CENTER)
    fn_js = Entry(suscreen, textvariable = full_name, width = 40)
    fn_js.place(rely=.60,relx=.54, anchor = CENTER)

    Label(suscreen, text = "Address:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.65,relx=.4, anchor = CENTER)
    a_js = Entry(suscreen, textvariable = address_js, width = 40)
    a_js.place(rely=.65,relx=.54, anchor = CENTER)

    Label(suscreen, text = "Position:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.70,relx=.4, anchor = CENTER)
    ds = Entry(suscreen, textvariable = desired_position, width = 40)
    ds.place(rely=.70,relx=.54, anchor = CENTER)

    Label(suscreen, text = "Contact Number:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.75,relx=.4, anchor = CENTER)
    cno2 = Entry(suscreen, textvariable = contact_no2, width = 40)
    cno2.place(rely=.75,relx=.54, anchor = CENTER)

    Label(suscreen, text = "Password:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.8,relx=.4, anchor = CENTER)
    p_js = Entry(suscreen, show="•", textvariable = password_js, width = 40)
    p_js.place(rely=.8,relx=.54, anchor = CENTER)

    fn_js = full_name.get()
    p_js = password_js.get()
    a_js = address_js.get()
    store_a_js.append(a_js)
    ds = desired_position.get()
    store_ds.append(ds)
    cno2 = contact_no2.get()
    store_cno2.append(cno2)

    def store_jobseeker():
        register_js = Toplevel()
        register_js.title("Registration Result")
        register_js.geometry("300x300+0+0")
        register_js.resizable(width=FALSE, height=FALSE)
        register_js.configure(background='powder blue')

        if fn_js in store_fn_js:
            Button(register_js, text="Applicant's Name already exist!", height=2, width=30, font=("Bahnschrift", 10, "bold",), bg="light green",
                   fg="red", command=suscreen).place(relx=.5, rely=.55, anchor=CENTER)

        else:
            store_fn_js.append(fn_js)
            store_p_js.append(p_js)
            Button(register_js, text="Registration Success!", height=2, width=30, font=("Bahnschrift", 10, "bold",),
                   bg="light green", fg="navy blue", command=log_in_js).place(relx=.5, rely=.5, anchor=CENTER)
            suscreen.destroy()

    Button(suscreen, text = "REGISTER AS JOB-SEEKER", height = 2, width = 30, font = ("Bahnschrift", 10, "bold",), bg = "light green", fg = "navy blue", command = store_jobseeker).place(relx =.5, rely = .87, anchor = CENTER)


def log_in_a():
    ascreen = Toplevel()
    ascreen.title("ADMINISTRATOR'S LOG-IN")
    ascreen.geometry("1366x768+0+0")
    ascreen.resizable(width=FALSE, height=FALSE)
    ascreen.configure(background='powder blue')

    fn_admin = StringVar()

    Label(ascreen, text="Administrator's Log-in", font = ("Bahnschrift", 20, "bold"), bg = "powder blue", fg = "navy blue").place(rely=.2, relx=.5, anchor=CENTER)

    Label(ascreen, text = "Full Name:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.3,relx=.4, anchor = CENTER)
    fne_a = Entry(ascreen, textvariable = fn_admin, width = 40)
    fne_a.place(rely=.3,relx=.52, anchor = CENTER)

    p_admin = StringVar()

    Label(ascreen, text = "Password:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.35,relx=.4, anchor = CENTER)
    pw_a = Entry(ascreen, show="•", textvariable = p_admin, width = 40)
    pw_a.place(rely=.35,relx=.52, anchor = CENTER)

    Button(ascreen, text="LOG-IN AS ADMINISTRATOR", height=2, width=30, font=("Bahnschrift", 10, "bold",), bg="light green", fg="navy blue").place(relx=.5, rely=.5, anchor=CENTER)

def log_in_e():
    escreen = Toplevel()
    escreen.title("EMPLOYER'S LOG-IN")
    escreen.geometry("1366x768+0+0")
    escreen.resizable(width=FALSE, height=FALSE)
    escreen.configure(background='powder blue')

    cn_employer = StringVar()

    Label(escreen, text="Employer's Log-in", font = ("Bahnschrift", 20, "bold"), bg = "powder blue", fg = "navy blue").place(rely=.2, relx=.5, anchor=CENTER)

    Label(escreen, text = "Company Name:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.3,relx=.4, anchor = CENTER)
    cn_e = Entry(escreen, textvariable = cn_employer, width = 40)
    cn_e.place(rely=.3,relx=.53, anchor = CENTER)

    p_employer = StringVar()

    Label(escreen, text = "Password:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.35,relx=.4, anchor = CENTER)
    p_e = Entry(escreen, show="•",textvariable = p_employer, width = 40)
    p_e.place(rely=.35,relx=.53, anchor = CENTER)

    Button(escreen, text="LOG-IN AS EMPLOYER", height=2, width=30, font=("Bahnschrift", 10, "bold",), bg="light green", fg="navy blue").place(relx=.5, rely=.5, anchor=CENTER)

def log_in_js():
    jsscreen = Toplevel()
    jsscreen.title("JOB-SEEKERS' LOG-IN")
    jsscreen.geometry("1366x768+0+0")
    jsscreen.resizable(width=FALSE, height=FALSE)
    jsscreen.configure(background='powder blue')

    fn_jobseeker = StringVar()

    Label(jsscreen, text="Job-seekers' Log-in", font = ("Bahnschrift", 20, "bold"), bg = "powder blue", fg = "navy blue").place(rely=.2, relx=.5, anchor=CENTER)

    Label(jsscreen, text = "Full Name:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.3,relx=.4, anchor = CENTER)
    fne_js = Entry(jsscreen, textvariable = fn_jobseeker , width = 40)
    fne_js.place(rely=.3,relx=.52, anchor = CENTER)

    p_jobseeker = StringVar()

    Label(jsscreen, text = "Password:", font = ("Bahnschrift", 10,), bg = "powder blue", fg = "black").place(rely=.35,relx=.4, anchor = CENTER)
    pw_js = Entry(jsscreen, show="•", textvariable = p_jobseeker, width = 40)
    pw_js.place(rely=.35,relx=.52, anchor = CENTER)

    def log_in_js2():
        login_js2 = Toplevel()
        login_js2.title("Login Result")
        login_js2.geometry("300x300+0+0")
        login_js2.resizable(width=FALSE, height=FALSE)
        login_js2.configure(background='powder blue')

        if fne_js in store_fn_js:
            if pw_js in store_pw_js:
                Button(login_js2, text="Log-in Success!", height=2, width=30,font=("Bahnschrift", 10, "bold",), bg="light green", fg="red", command=vacancies).place(relx=.5,rely=.55,anchor=CENTER)
            else:
                Button(login_js2, text="Incorrect Password!", height=2, width=30, font=("Bahnschrift", 10, "bold",),bg="light green", fg="red", command=log_in_js).place(relx=.5, rely=.55, anchor=CENTER)
        elif pw_js in store_pw_js:
            if fne_js in store_fn_js:
                Button(login_js2, text="Log-in Success!", height=2, width=30, font=("Bahnschrift", 10, "bold",),bg="light green", fg="red", command=vacancies).place(relx=.5, rely=.55, anchor=CENTER)
            else:
                Button(login_js2, text="Incorrect Password!", height=2, width=30, font=("Bahnschrift", 10, "bold",),bg="light green", fg="red", command=log_in_js).place(relx=.5, rely=.55, anchor=CENTER)
        else:
            Button(login_js2, text="Incorrect Password!", height=2, width=30, font=("Bahnschrift", 10, "bold",),bg="light green", fg="navy blue", command=vacancies).place(relx=.5, rely=.5, anchor=CENTER)

    Button(jsscreen, text="LOG-IN AS JOB-SEEKER", height=2, width=30, font=("Bahnschrift", 10, "bold",), bg="light green", fg="navy blue", command = log_in_js2).place(relx=.5, rely=.5, anchor=CENTER)

window = Tk()
window.title("Employment Portal")
window.geometry("1366x768+0+0")
window.resizable(width=FALSE, height=FALSE)
window.configure(background='powder blue')


Label(window, text = "Welcome to Employment Portal!", font = ("CC-Fat-Regular", 50,), bg = "powder blue", fg = "midnight blue").place(rely=.2,relx=.5, anchor = CENTER)
Button(window, text = "JOB-SEEKER", height = 5, width = 30, font = ("Bahnschrift", 10, "bold",), bg = "light green", fg = "navy blue", command = log_in_js).place(relx =.3, rely = .5, anchor = CENTER)
Button(window, text = "EMPLOYER", height = 5, width = 30, font = ("Bahnschrift", 10, "bold",), bg = "light green", fg = "navy blue",  command = log_in_e).place(relx =.5, rely = .5, anchor = CENTER)
Button(window, text = "ADMIN", height = 5, width = 30, font = ("Bahnschrift", 10, "bold",), bg = "light green", fg = "navy blue",  command = log_in_a).place(relx =.7, rely = .5, anchor = CENTER)

Button(window, text = "SIGN-UP", height = 2, width = 20, font = ("Bahnschrift", 10, "bold",), bg = "light green", fg = "navy blue", command = sign_up).place(relx =.5, rely = .8, anchor = CENTER)

window.mainloop()