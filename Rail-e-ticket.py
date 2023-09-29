from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import tkinter as tk
import sqlite3

database = sqlite3.connect("E-Ticket.db")

# Variables
window = Tk()
user = ''
iD = ''
win = window
titleMain = win.title
loginFont = "Agency FB"
bg = Label(window)
l1 = Label(window)
l2 = Label(window)
login = Label(window)
LabelUser = Label(window)
LabelTitle = Label(window)
Label0 = Label(window)
Label1 = Label(window)
Label2 = Label(window)
Label3 = Label(window)
Label4 = Label(window)
Label5 = Label(window)
Label6 = Label(window)
Label7 = Label(window)
Label8 = Button(window)
Label9 = Button(window)
Label10 = Button(window)
Label11 = Button(window)
Label12 = Button(window)
Label13 = Button(window)
bookButton = Button(window)
dashButton = Button(window)
clearHistoryButton = Button(window)
logoutButton = Button(window)
buttonCreate = Button(window)
purchaseButton = Button(window)
purchaseButtonState = DISABLED
Password = Entry(window)
Username = Entry(window)
buttonLogin = Button(window)
frame = Frame(window)
tree = ttk.Treeview(frame)
tree_scrollbary = Scrollbar(frame)
strSelectedFrom = ''
strSelectedDate = ''
strSelectedTo = ''
strSelectedID = ''
strSelectedTrain = ''
strSelectedClass = ''
strPrice = ''
cboFrom = ttk.Combobox(window)
cboDate = ttk.Combobox(window)
cboTo = ttk.Combobox(window)
cboClass = ttk.Combobox(window)
cboNull = ttk.Combobox(window)
create = Toplevel(window)
register = Label(window)
createUser = Entry(window)
createPass = Entry(window)
trainList = []
stationList = []
scheduleList = []
price = []
updateButton = Button(window)
cancelButton = Button(window)
stationFromLabel = Label(window)
stationToLabel = Label(window)
scheduleLabel = Label(window)
classLabel = Label(window)
saveButton = Button(window)
count = 0
Value = ''


# function to check whether entry is in the database
def clickLogin():
    global user, Username, Password, iD
    try:
        cursor = database.cursor()
        query = 'SELECT * FROM Users WHERE userName = ? and password = ?'
        cursor.execute(query, [(Username.get()), (Password.get())])
        result = cursor.fetchall()
        if result:
            for i in result:
                user = str(i[0])
                # iD = str(i[0])
                destroy()
                loginSuccess()
        else:
            messagebox.showerror("Login Error", "The username or password is incorrect. Try again.")
    except sqlite3.Error as error:
        print(str(error))


# function to add entry to database and check
def clickCreate(c, p, cc, fn, ln, b, g, ct):
    try:
        cursor = database.cursor()
        query = 'SELECT * FROM Users WHERE userName = ?'
        cursor.execute(query, [(c.get())])
        result = cursor.fetchall()
        if result:
            return messagebox.showerror("Registration Error", "Username already Exist.")

        getUser = c.get()
        getPass = p.get()
        getNameF = fn.get()
        getNameL = ln.get()
        getBirth = b.get()
        getGender = g.get()
        getContact = ct.get()

        if getUser == "Username" and getPass == "Password" or getPass == "Password" or getUser == "" or getPass == "":
            if getUser == "" or getPass == "":
                return messagebox.showerror("Registration Error", "Username and password cannot be empty.")
            return messagebox.showerror("Registration Error", "Username and password cannot be empty.")

        cursor.execute("INSERT INTO Users (userName, password)" "VALUES (?, ?)", (getUser, getPass))
        cursor.execute("INSERT INTO Passenger (userName, FirstName, LastName, PhoneNo, Birthdate, Gender)"
                       "VALUES (?, ?, ?, ?, ?, ?)", (getUser, getNameF, getNameL, getContact, getBirth, getGender))
        database.commit()
        cc.destroy()
        window.deiconify()
        return messagebox.showinfo("Successful Registration", "Account Created!")
    except sqlite3.Error as error:
        print(str(error))


# function to create an account, registration window
def createAccount():
    global loginFont, bookButton, dashButton, create, register, createUser, createPass
    window.withdraw()
    create = Toplevel(window)
    create.protocol("WM_DELETE_WINDOW", lambda: window.destroy())
    create.title("Registration")
    create.iconphoto(False, PhotoImage(file="register.png"))
    winDimension(500, 300, create)
    create.resizable(False, False)

    register = Label(create, text="R E G I S T E R", font=(loginFont, 20))
    register.place(x=180, y=5)

    createUser = Entry(create, width=30, fg="Gray")
    createUser.insert(END, 'Username')
    createUser.place(x=35, y=65, height=25)
    createUser.bind("<Button-1>", lambda e: createUser.delete(0, END))
    createUser.bind("<ButtonRelease-1>", lambda e: createUser.configure(fg="black"))

    createPass = Entry(create, width=30, fg="Gray")
    createPass.insert(END, 'Password')
    createPass.place(x=35, y=100, height=25)
    createPass.bind("<Button-1>", lambda e: createPass.delete(0, END))
    createPass.bind("<ButtonRelease-1>", lambda e: createPass.configure(fg="black", show="*"))

    entry1 = Entry(create, width=30, fg="Gray")
    entry1.insert(END, 'First Name')
    entry1.place(x=250, y=65, height=25)
    entry1.bind("<Button-1>", lambda e: entry1.delete(0, END))
    entry1.bind("<ButtonRelease-1>", lambda e: entry1.configure(fg="black"))

    entry2 = Entry(create, width=30, fg="Gray")
    entry2.insert(END, 'Last Name')
    entry2.place(x=250, y=100, height=25)
    entry2.bind("<Button-1>", lambda e: entry2.delete(0, END))
    entry2.bind("<ButtonRelease-1>", lambda e: entry2.configure(fg="black"))

    entry3 = Entry(create, width=30, fg="Gray")
    entry3.insert(END, 'Birth Date')
    entry3.place(x=250, y=135, height=25)
    entry3.bind("<Button-1>", lambda e: entry3.delete(0, END))
    entry3.bind("<ButtonRelease-1>", lambda e: entry3.configure(fg="black"))

    entry4 = Entry(create, width=30, fg="Gray")
    entry4.insert(END, 'Gender')
    entry4.place(x=250, y=170, height=25)
    entry4.bind("<Button-1>", lambda e: entry4.delete(0, END))
    entry4.bind("<ButtonRelease-1>", lambda e: entry4.configure(fg="black"))

    entry5 = Entry(create, width=30, fg="Gray")
    entry5.insert(END, 'Contact No:')
    entry5.place(x=250, y=205, height=25)
    entry5.bind("<Button-1>", lambda e: entry5.delete(0, END))
    entry5.bind("<ButtonRelease-1>", lambda e: entry5.configure(fg="black"))

    buttonC = Button(create, text="Create",
                     command=lambda c=createUser, p=createPass, cc=create, fn=entry1, ln=entry2,
                     b=entry3, g=entry4, ct=entry5: clickCreate(createUser, createPass, create, entry1,
                                                                entry2, entry3, entry4, entry5))
    buttonC.place(x=75, y=200)

    dashButton = Button(create, text="Back", command=loggedIn)
    dashButton.place(x=125, y=200)


# Clear Screen Function
def destroy():
    login.destroy()
    buttonLogin.destroy()
    Username.destroy()
    Password.destroy()
    buttonCreate.destroy()
    bg.destroy()
    Label1.destroy()
    l1.destroy()
    l2.destroy()
    LabelUser.destroy()
    LabelTitle.destroy()
    Label0.destroy()
    Label1.destroy()
    Label2.destroy()
    Label3.destroy()
    Label4.destroy()
    Label5.destroy()
    Label6.destroy()
    Label7.destroy()
    Label8.destroy()
    Label9.destroy()
    Label10.destroy()
    Label11.destroy()
    Label12.destroy()
    Label13.destroy()
    bookButton.destroy()
    dashButton.destroy()
    logoutButton.destroy()
    frame.destroy()
    cboFrom.destroy()
    cboDate.destroy()
    cboTo.destroy()
    cboClass.destroy()
    create.destroy()
    register.destroy()
    createUser.destroy()
    createPass.destroy()
    updateButton.destroy()
    cancelButton.destroy()
    stationFromLabel.destroy()
    stationToLabel.destroy()
    scheduleLabel.destroy()
    classLabel.destroy()
    saveButton.destroy()
    purchaseButton.destroy()
    clearHistoryButton.destroy()


# function to center the window on the screen
def winDimension(width, height, window):
    windowWidth = width
    windowHeight = height

    screenWidth = window.winfo_screenwidth()
    screenHeight = window.winfo_screenheight()
    screenX = (screenWidth / 2) - (windowWidth / 2)
    screenY = (screenHeight / 2) - (windowHeight / 2)

    window.geometry(f'{windowWidth}x{windowHeight}+{int(screenX)}+{int(screenY)}')


#   TICKET MANAGER FUNCTIONS
# function for updating tickets
def enable_widgets():
    global stationFromLabel, stationToLabel, cboFrom, cboTo, scheduleLabel, cboDate, classLabel, cboClass, saveButton

    stationFromLabel.config(fg='black')
    cboFrom.config(state=NORMAL)
    stationToLabel.config(fg='black')
    cboTo.config(state=NORMAL)
    scheduleLabel.config(fg='black')
    cboDate.config(state=NORMAL)
    classLabel.config(fg='black')
    cboClass.config(state=NORMAL)
    saveButton.config(state=NORMAL)


def setValues():
    global trainList, scheduleList, stationList, price

    price = [(25, 20), (45, 36), (55, 44), (20, 16), (30, 24), (15, 12)]

    trainList = ["AC", "ORDINARY"]

    scheduleList = ["2022-08-09 4:00PM", "2022-08-09 5:00PM", "2022-08-09 6:00PM", "2022-08-09 7:00PM"]

    queryStation = "SELECT DISTINCT(StationFrom) FROM Train"
    stationData = database.execute(queryStation)
    stationList = [r for r, in stationData]


def select_record(e):
    global cboFrom, cboTo, cboDate, cboClass

    # Grab record Number
    selected = tree.focus()
    # Grab record values
    values = tree.item(selected, 'values')

    # output datas to combo boxes
    cboFrom.set(values[2])
    cboTo.set(values[3])
    cboDate.set(values[4])
    cboClass.set(values[7])


def update_record():
    global database, cboFrom, cboTo, cboDate, cboClass, iD

    try:
        trainID, fare = 0, 0
        cursor = database.execute("""SELECT * FROM Train""")
        records = cursor.fetchall()
        for i in range(len(records)):
            if cboFrom.get() in (records[i][2], records[i][3]) and cboTo.get() in (records[i][2], records[i][3]):
                if cboClass.get() == 'AC':
                    fare = price[i][0]
                if cboClass.get() == "ORDINARY":
                    fare = price[i][1]

                trainID = records[i][0]

        selected = tree.focus()  # holds the row number and the value of the selected item
        temp = tree.item(selected, 'values')

        database.execute(f"""UPDATE Ticket
            SET Schedule = '{cboDate.get()}',  
            TrainID = {trainID},
            Class = '{cboClass.get()}',
            FarePrice = {fare}
            WHERE ticketID = {temp[0]}""")

        cursor = database.execute(f"""SELECT passengerID
                    FROM Passenger
                    WHERE userName = '{user}'""")
        records = cursor.fetchall()
        iD = records[0][0]

        database.execute("INSERT INTO History (HistoryInf, PassengerID)" "VALUES (?, ?)", ('Updated Ticket', iD))

        database.commit()
        get_records()
    except sqlite3.Error as error:
        print(str(error))


def delete_records():
    global database, tree, iD

    try:
        selected = tree.focus()  # holds the row number and the value of the selected item
        temp = tree.item(selected, 'values')

        database.execute(f"""DELETE FROM Ticket
            WHERE ticketID = {temp[0]}""")

        cursor = database.execute(f"""SELECT passengerID
                            FROM Passenger
                            WHERE userName = '{user}'""")
        records = cursor.fetchall()
        iD = records[0][0]

        database.execute("INSERT INTO History (HistoryInf, PassengerID)" "VALUES (?, ?)", ('Cancelled Ticket', iD))
        database.commit()
        get_records()
    except sqlite3.Error as error:
        print(str(error))


def format_treeview():
    global tree, tree_scrollbary, frame

    frame = Frame(window)
    frame.place(x=135, y=250)

    tree_scrollbary = Scrollbar(frame)
    tree_scrollbary.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(frame, yscrollcommand=tree_scrollbary.set)  # instantiate treeview
    tree.pack()

    tree_scrollbary.config(command=tree.yview)

    # gets the passengerID of the user
    cursor = database.execute(f"""SELECT passengerID
                       FROM Passenger
                       WHERE userName = '{user}'""")
    records = cursor.fetchall()
    passengerID = records[0][0]

    cursor = database.execute(f"""SELECT Ticket.TicketID, Ticket.PassengerID, Train.StationFrom, Train.StationTo,
                    Ticket.Schedule, Train.TrainID, Train.TrainName, Ticket.Class, Ticket.FarePrice
                    FROM Ticket
                    LEFT OUTER JOIN Train
                    ON Ticket.TrainID = Train.TrainID
                    WHERE Ticket.PassengerID = {passengerID};""")

    columns = tuple([description[0] for description in cursor.description])
    tree['columns'] = columns  # define our columns

    # Formatting Column
    tree.column("#0", width=0, stretch=NO)
    tree.column("TicketID", anchor=CENTER, width=70)
    tree.column("PassengerID", anchor=CENTER, width=80)
    tree.column("StationFrom", anchor=CENTER, width=100)
    tree.column("StationTo", anchor=CENTER, width=90)
    tree.column("Schedule", anchor=CENTER, width=110)
    tree.column("TrainID", anchor=CENTER, width=70)
    tree.column("TrainName", anchor=CENTER, width=90)
    tree.column("Class", anchor=CENTER, width=70)
    tree.column("FarePrice", anchor=CENTER, width=80)

    # Creating Headings
    columnNames = ["Ticket ID", "Passenger ID", "Station From", "Station To", "Schedule", "Train ID", "Train Name",
                   "Class", "Fare Price"]

    tree.heading("#0", text="", anchor=CENTER)
    for i in range(len(columns)):
        tree.heading(columns[i], text=columnNames[i], anchor=CENTER)


# function for displaying the records
def get_records():
    global count
    for item in tree.get_children():
        tree.delete(item)

    # gets the passengerID of the user
    cursor = database.execute(f"""SELECT passengerID
                    FROM Passenger
                    WHERE userName = '{user}'""")
    records = cursor.fetchall()
    passengerID = records[0][0]

    cursor = database.execute(f"""SELECT Ticket.TicketID, Ticket.PassengerID, Train.StationFrom, Train.StationTo,
                Ticket.Schedule, Train.TrainID, Train.TrainName, Ticket.Class, Ticket.FarePrice
                FROM Ticket
                LEFT OUTER JOIN Train
                ON Ticket.TrainID = Train.TrainID
                WHERE Ticket.PassengerID = {passengerID};""")
    records = cursor.fetchall()

    # count = 0

    for record in records:
        iidValue = str(count)
        tree.insert(parent='', index='end', iid=iidValue, text='',
                    values=(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                            record[8]))
        count += 1

    tree.bind("<ButtonRelease-1>", select_record)


#   TICKET MANAGER
def ticketManager():
    destroy()
    global user, bg, Label1, Label2, Label3, Label4, Label5, Label6, Label7, bookButton, dashButton, logoutButton
    global win, titleMain, LabelTitle, l1, l1, window, cboFrom, cboDate, cboTo, cboClass
    global stationFromLabel, stationToLabel, classLabel, scheduleLabel, updateButton, cancelButton, saveButton
    destroy()
    bg = Label(win, width=40, height=50)
    titleMain = win.title("Rail E-Ticket Booking V1.01")
    LabelTitle = Label(win, text="TICKET MANAGER", font=('Agency FB', 25), fg='red')
    win.iconphoto(False, PhotoImage(file="train.png"))
    winDimension(1040, 580, win)
    win['bg'] = '#c4def6'

    LabelTitle.place(x=430, y=5)
    bookButton = Button(win, text="Back to Menu", height=2, width=15, bg='#FFFFB6', command=menu)
    bookButton.place(x=60, y=520)
    dashButton = Button(win, text="Refresh", height=2, width=15, bg='#FFFFB6', command=ticketManager)
    dashButton.place(x=455, y=520)
    updateButton = Button(win, text="Update Ticket", font=("Arial", 10), width=10, bg='#FFFFB6', command=enable_widgets)
    updateButton.place(x=415, y=70)
    cancelButton = Button(win, text="Cancel Ticket", font=("Arial", 10), width=10, bg='#FFFFB6', command=delete_records)
    cancelButton.place(x=525, y=70)

    setValues()
    format_treeview()
    get_records()

    stationFromLabel = Label(win, text="Station From", font=("Arial", 10), fg='#656c73', bg='#c4def6')
    stationFromLabel.place(x=265, y=120)
    cboFrom = ttk.Combobox(win, values=stationList, state=DISABLED)
    cboFrom.place(x=360, y=120)
    stationToLabel = Label(win, text="Station To", font=("Arial", 10), fg='#656c73', bg='#c4def6')
    stationToLabel.place(x=515, y=120)
    cboTo = ttk.Combobox(win, values=stationList, state=DISABLED)
    cboTo.place(x=585, y=120)
    scheduleLabel = Label(win, text="Schedule", font=("Arial", 10), fg='#656c73', bg='#c4def6')
    scheduleLabel.place(x=290, y=160)
    cboDate = ttk.Combobox(win, values=scheduleList, state=DISABLED)
    cboDate.place(x=360, y=160)
    classLabel = Label(win, text="Class", font=("Arial", 10), fg='#656c73', bg='#c4def6')
    classLabel.place(x=535, y=160)
    cboClass = ttk.Combobox(win, values=trainList, state=DISABLED)
    cboClass.place(x=585, y=160)
    saveButton = Button(win, text="Save", bg='#FFFFB6', width=5, state=DISABLED, command=update_record)
    saveButton.place(x=500, y=200)


# TICKET BOOKING FUNCTIONS

# Print Ticket Function
def printSelected():
    global strSelectedFrom, strSelectedTo, strSelectedDate, strSelectedClass, strPrice, strSelectedID, strSelectedTrain, purchaseButtonState
    strSelectedFrom = cboFrom.get()
    strSelectedTo = cboTo.get()
    strSelectedDate = cboDate.get()
    strSelectedClass = cboClass.get()
    strSelectedTrain = cboNull.get()
    strSelectedID = cboNull.get()
    strPrice = cboNull.get()
    #Setting Train Fare Price
    cursor = database.execute("""SELECT * FROM Train""")
    records = cursor.fetchall()
    for i in range(len(records)):
        if cboFrom.get() in (records[i][2], records[i][3]) and cboTo.get() in (records[i][2], records[i][3]):
            if cboClass.get() == 'AC':
                strPrice = str(price[i][0])
            if cboClass.get() == "ORDINARY":
                strPrice = str(price[i][1])

            strSelectedID = str(records[i][0])
            strSelectedTrain = records[i][1]
    purchaseButtonState = NORMAL
    book()


# Purchase Button Function
def purchase():
    global iD, purchaseButtonState
    # gets the passengerID of the user
    cursor = database.execute(f"""SELECT passengerID
            FROM Passenger
            WHERE userName = '{user}'""")
    records = cursor.fetchall()
    iD = records[0][0]

    database.execute(f"""INSERT INTO Ticket (PassengerID, Schedule, TrainID, Class, FarePrice) 
    VALUES ('{iD}', '{strSelectedDate}', {strSelectedID}, '{strSelectedClass}', {strPrice})""")
    database.execute("INSERT INTO History (HistoryInf, PassengerID)" "VALUES (?, ?)", ('Purchased Ticket', iD))
    database.commit()
    purchaseButtonState = DISABLED
    messagebox.showinfo("Purchased", "Purchased Successfully!")
    book()


#   TICKET BOOKING
def book():
    destroy()
    global Label1, Label2, Label3, Label4, Label5, Label6, Label7, Label8, Label9, Label10, Label11, Label12, Label13
    global win, titleMain, LabelTitle, l1, l1, l2, tree, bookButton, dashButton, logoutButton, user, bg, purchaseButton, purchaseButtonState
    global cboFrom, cboDate, cboTo, cboClass

    destroy()
    bg = Label(win, width=40, height=50)
    titleMain = win.title("Rail E-Ticket Booking V1.01")
    LabelTitle = Label(win, text="BOOK YOUR TICKET", font=('Agency FB', 25), fg='red')
    win.iconphoto(False, PhotoImage(file="train.png"))
    winDimension(1040, 580, win)
    win['bg'] = '#c4def6'

    LabelTitle.place(x=410, y=5)
    l1 = Label(win, width=55, height=24, bg='#D4D4D4')
    l1.place(x=540, y=80)
    l2 = Label(win, width=55, height=24, bg='#D4D4D4')
    l2.place(x=80, y=80)

    Label1 = Label(win, text="Customize your ticket:", font=('Agency FB', 22), bg='#D4D4D4')
    Label1.place(x=180, y=90)
    Label2 = Label(win, text="Ticket Details:", font=('Agency FB', 22), bg='#D4D4D4')
    Label2.place(x=680, y=90)
    Label3 = Label(win, text="Station from: ", font=(1, 12), bg='#D4D4D4')
    Label3.place(x=110, y=160)
    Label4 = Label(win, text="Schedule: ", font=(1, 12), bg='#D4D4D4')
    Label4.place(x=110, y=220)
    Label5 = Label(win, text="Station to: ", font=(1, 12), bg='#D4D4D4')
    Label5.place(x=110, y=280)
    Label6 = Label(win, text="Class: ", font=(1, 12), bg='#D4D4D4')
    Label6.place(x=110, y=340)

    Label7 = Label(win, text="Journey Date:         " + strSelectedDate, font=(1, 12), bg='#D4D4D4')
    Label7.place(x=570, y=150)
    Label8 = Label(win, text="From station:          " + strSelectedFrom, font=(1, 12), bg='#D4D4D4')
    Label8.place(x=570, y=190)
    Label9 = Label(win, text="To station:               " + strSelectedTo, font=(1, 12), bg='#D4D4D4')
    Label9.place(x=570, y=230)
    Label10 = Label(win, text="Train ID:                  " + strSelectedID, font=(1, 12), bg='#D4D4D4')
    Label10.place(x=570, y=270)
    Label11 = Label(win, text="Train Name:            " + strSelectedTrain, font=(1, 12), bg='#D4D4D4')
    Label11.place(x=570, y=310)
    Label12 = Label(win, text="Class:                      " + strSelectedClass, font=(1, 12), bg='#D4D4D4')
    Label12.place(x=570, y=350)
    Label13 = Label(win, text="Fare Price:              " + strPrice, font=(1, 12), bg='#D4D4D4')
    Label13.place(x=570, y=390)

    bookButton = Button(win, text="Back to Menu", height=2, width=15, bg='#FFFFB6', command=menu)
    bookButton.place(x=60, y=520)

    purchaseButton = Button(win, text="Purchase", command=purchase, state=purchaseButtonState, height=2, width=15, bg='#FFFFB6')
    purchaseButton.place(x=860, y=520)
    logoutButton = Button(win, text="Print ticket", command=printSelected, height=1, width=11, bg='#FFFFB6')
    logoutButton.place(x=230, y=410)

    From = tk.StringVar()
    Date = tk.StringVar()
    To = tk.StringVar()
    Train = tk.StringVar()

    setValues()

    cboFrom = ttk.Combobox(window, values=stationList, width=27, textvariable=From)
    cboFrom.place(x=230, y=160)
    cboFrom.current(0)

    cboDate = ttk.Combobox(window, values=scheduleList, width=27, textvariable=Date)
    cboDate.place(x=230, y=220)
    cboDate.current(0)

    cboTo = ttk.Combobox(window, values=stationList, width=27, textvariable=To)
    cboTo.place(x=230, y=280)
    cboTo.current(0)

    cboClass = ttk.Combobox(window, values=trainList, width=27, textvariable=Train)
    cboClass.place(x=230, y=340)
    cboClass.current(0)


def loginSuccess():
    destroy()
    window.deiconify()
    menu()
    messagebox.showinfo("Successful Login", "WELCOME " + user.capitalize() + "!!!")


def clearHistory():
    global iD
    cursor = database.execute(f"""SELECT passengerID
                                FROM Passenger
                                WHERE userName = '{user}'""")
    records = cursor.fetchall()
    iD = records[0][0]

    database.execute(f"""DELETE FROM History
                   WHERE PassengerID = {iD}""")
    database.commit()
    menu()


def menu():
    def logout():
        loggedIn()

    global user, bg, Label1, Label2, Label3, Label4, Label5, Label6, Label7, bookButton, dashButton, logoutButton
    global win, Label0, titleMain, LabelTitle, LabelUser, l1, l2, frame, tree_scrollbary, tree, clearHistoryButton
    destroy()
    # identification of user's info
    cursor = database.cursor()
    query = 'SELECT * FROM Passenger WHERE userName = ?'
    cursor.execute(query, [user])
    result = cursor.fetchall()
    FName = ''
    LName = ''
    contact = ''
    Gender = ''
    Birth = ''
    passID = ''

    for i in result:
        FName = str(i[1])
        LName = str(i[2])
        contact = str(i[3])
        Gender = str(i[5])
        Birth = str(i[4])
        passID = str(i[0])

    # display Menu
    win.iconphoto(False, PhotoImage(file="train.png"))
    titleMain = win.title("Rail E-Ticket Booking V1.01")
    winDimension(1040, 580, win)
    win['bg'] = '#c4def6'
    l1 = Label(win, width=200, height=100, bg='#c4def6')
    l1.grid(column=5, row=5)
    l2 = Label(win, width=100, height=8)
    l2.place(x=300, y=440)
    bg = Label(win, width=40, height=50)
    bg.grid(column=0, row=0)

    LabelUser = Label(win, text="User: " + user.capitalize(), font=(1, 15), fg='green')
    LabelTitle = Label(win, text="RAIL E-TICKET BOOKING SYSTEM", font=('Agency FB', 25), fg='red')
    Label1 = Label(win, text="Personal Information ", font=(0.5, 11), fg='blue')
    Label2 = Label(win, text="First Name:         " + FName)
    Label0 = Label(win, text="Last Name:         " + LName)
    Label3 = Label(win, text="Contact No:       " + contact)
    Label4 = Label(win, text="Birth Date:          " + Birth)
    Label5 = Label(win, text="Gender:               " + Gender)
    Label6 = Label(win, text="Passenger ID:     " + passID)
    Label7 = Label(win, text="History Log:", font=(1, 12), bg='#c4def6')

    bookButton = Button(win, text="BOOK A TICKET", height=4, width=15, bg='#F0F080', command=book)
    dashButton = Button(win, text="MANAGE TICKET/S", height=4, width=15, bg='#F0F080', command=ticketManager)
    logoutButton = Button(win, text="LOGOUT", height=2, width=10, bg='#FFFFB6', command=logout)
    clearHistoryButton = Button(win, text="Clear History", command=clearHistory, height=1, width=11, bg='#FFFFB6')
    clearHistoryButton.place(x=930, y=410)

    LabelUser.place(x=25, y=5)
    LabelTitle.place(x=500, y=5)
    Label1.place(x=25, y=100)
    Label2.place(x=25, y=130)
    Label0.place(x=25, y=160)
    Label4.place(x=25, y=190)
    Label5.place(x=25, y=220)
    Label6.place(x=25, y=250)
    Label7.place(x=300, y=410)
    Label3.place(x=25, y=280)
    bookButton.place(x=600, y=110)
    dashButton.place(x=600, y=250)
    logoutButton.place(x=100, y=510)

    frame = Frame(window)
    frame.place(x=300, y=440)

    tree_scrollbary = Scrollbar(frame)
    tree_scrollbary.pack(side=RIGHT, fill=Y)

    tree = ttk.Treeview(frame, height=5, yscrollcommand=tree_scrollbary.set)  # instantiate treeview
    tree.pack()

    tree_scrollbary.config(command=tree.yview)

    # gets the History Information of the user
    cursor = database.execute(f"""SELECT passengerID
                           FROM Passenger
                           WHERE userName = '{user}'""")
    records = cursor.fetchall()
    passengerID = records[0][0]

    cursor = database.execute(f"""SELECT History.HistoryId, History.HistoryInf
                        FROM History
                        WHERE History.PassengerID = {passengerID};""")

    columns = tuple([description[0] for description in cursor.description])
    tree['columns'] = columns  # define our columns

    # Formatting Column
    tree.column("#0", width=0, stretch=NO)
    tree.column("HistoryId", anchor=CENTER, width=80)
    tree.column("HistoryInf", anchor=CENTER, width=620)

    # Creating Headings
    columnNames = ["Log#", "History Information"]

    tree.heading("#0", text="", anchor=CENTER)
    for i in range(len(columns)):
        tree.heading(columns[i], text=columnNames[i], anchor=CENTER)

    global count
    for item in tree.get_children():
        tree.delete(item)

    cursor = database.execute(f"""SELECT History.HistoryId, History.HistoryInf
                    FROM History
                    WHERE History.PassengerID = {passengerID};""")
    records = cursor.fetchall()

    # count = 0

    for record in records:
        iidValue = str(count)
        tree.insert(parent='', index='end', iid=iidValue, text='',
                    values=(record[0], record[1]))
        count += 1


def loggedIn():
    global database, Username, Password, login, buttonCreate, buttonLogin
    destroy()
    window.deiconify()
    # login window
    window.title('Rail E-Ticket V1.01')
    window.iconphoto(False, PhotoImage(file="login.png"))
    winDimension(340, 200, window)
    window.resizable(False, False)
    win['bg'] = '#F7F7F7'

    # connect to database
    database = sqlite3.connect("E-Ticket.db")

    # Login label
    login = Label(window, text="L O G I N", font=(loginFont, 20))
    login.place(x=125, y=5)
    # username widget and function
    Username = Entry(window, width=30, fg="Gray")
    Username.insert(END, 'Username')
    Username.place(x=70, y=45, height=25)
    Username.bind("<Button-1>", lambda e: Username.delete(0, END))
    Username.bind("<ButtonRelease-1>", lambda e: Username.configure(fg="black"))

    # password widget and function
    Password = Entry(window, width=30, fg="Gray")
    Password.insert(END, 'Password')
    Password.place(x=70, y=80, height=25)
    Password.bind("<Button-1>", lambda e: Password.delete(0, END))
    Password.bind("<ButtonRelease-1>", lambda e: Password.configure(fg="black", show="*"))

    # buttons for login and create account with functions
    buttonLogin = Button(window, text="Login", command=clickLogin)
    buttonLogin.place(x=135, y=120)

    buttonCreate = Button(window, text="Create an account", bd=0, fg="#4a7cdc", command=createAccount)
    buttonCreate.place(x=105, y=160)
    window.mainloop()


loggedIn()
