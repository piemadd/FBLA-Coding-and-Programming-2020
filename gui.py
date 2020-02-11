from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog, messagebox
from fileManagement import *

file = ""
data = ""

def userManage_start(): #opens the user management window
    global data
    global combo
    #main.destroy()
    root = Tk()
    root.title("User Management Console")
    root.geometry('600x400')
    lbl = Label(root, text="Enter User ID/Sudent ID: ")
    lbl.grid(column=0, row=0)
    combo = Combobox(root)
    userIDs = userIndex(data)
    combo['values'] = userIDs
    combo.grid(column=2, row=0)
    openUser = Button(root, text="View/Edit User", command=editUser_start)
    openUser.grid(column=3, row=0)
    root.mainloop()

def editUser_start():
    global data
    global main
    global combo
    global root
    global user_current_editing
    global txta, txtb, txtc, txtd
    root = Tk()
    root.title("User Editing Console")
    root.geometry('600x400')
    userID_current_editing = combo.get()
    try:
        user_current_editing = findUser(data, userID_current_editing)
        a = user_current_editing['nameFirst']
        b = user_current_editing['nameLast']
        c = user_current_editing['gradeLevel']
        d = user_current_editing['id']
    except:
        a = ''
        b = ''
        c = ''
        d = ''
        user_current_editing = {"nameFirst": "", "gradeLevel": "", "hourIds": [], "lastTotal": "", "nameLast": "", "id": ""}
    lbla = Label(root, text="First Name: ")
    lbla.grid(column=0, row=0)
    txta = Entry(root, width=20)
    txta.grid(column=1, row=0)
    txta.insert(END, a)
    user_current_editing['nameFirst'] = txta.get()
    lblb = Label(root, text="Last Name: ")
    lblb.grid(column=0, row=1)
    txtb = Entry(root, width=20)
    txtb.grid(column=1, row=1)
    txtb.insert(END, b)
    user_current_editing['nameLast'] = txtb.get()
    lblc = Label(root, text="Grade Level: ")
    lblc.grid(column=0, row=2)
    txtc = Entry(root, width=20)
    txtc.grid(column=1, row=2)
    txtc.insert(END, c)
    user_current_editing['gradeLevel'] = txtc.get()
    lbld = Label(root, text="Student ID: ")
    lbld.grid(column=0, row=3)
    txtd = Entry(root, width=20)
    txtd.grid(column=1, row=3)
    txtd.insert(END, d)
    user_current_editing['id'] = txtd.get()
    btn = Button(root, text="Save Current User", command=save_current_user)
    btn.grid(column=0, row=5)
    root.mainloop()

def save_current_user():
    global combo
    global data
    global user_current_editing
    global txta, txtb, txtc, txtd
    append = 0
    user_current_editing['nameFirst'] = txta.get()
    user_current_editing['nameLast'] = txtb.get()
    user_current_editing['gradeLevel'] = txtc.get()
    user_current_editing['id'] = txtd.get()
    userID_current_editing = combo.get()
    users_current = data['profiles']
    user_current_location = findUserLocation(data, userID_current_editing)
    if str(user_current_location) == "<type 'exceptions.Exception'>":
        user_current_location = len(users_current)
        users_current.append("")
    #global user_current_location, users_current
    #user_current_location = len(users_current)
    users_current[user_current_location] = user_current_editing
    data['profiles'] = users_current
    saveDatabase(data, file)

def hourManage_start():  # opens the user management window
    global data
    global combo
    root = Tk()
    root.title("Hour Management Console")
    root.geometry('600x400')
    lbl = Label(root, text="Enter Hour ID: ")
    lbl.grid(column=0, row=0)
    combo = Combobox(root)
    hourIDs = hoursIndex_ids(data)
    combo['values'] = hourIDs
    combo.grid(column=2, row=0)
    openHour = Button(root, text="View/Edit Hour", command=editHour_start)
    openHour.grid(column=3, row=0)
    root.mainloop()

def editHour_start():
    global data
    global main
    global combo
    global root
    global hour_current_editing
    global txta, txtb, txtc, txtd
    root = Tk()
    root.title("Hour Editing Console")
    root.geometry('600x400')
    hourID_current_editing = combo.get()
    if True:
        hour_current_editing = findHour(data, hourID_current_editing)
        print(hour_current_editing)
        print("got the hour current successfully")
        a = hour_current_editing['hourId']
        print("hourid")
        b = hour_current_editing['studentNumber']
        print("studentNumber")
        c = hour_current_editing['date']
        print("date")
        d = hour_current_editing['hours']
        print("hours")
    '''except:
        a = ''
        b = ''
        c = ''
        d = ''
        hour_current_editing = {"hourId": "", "studentNumber": "", "date": "", "hours": ""}
        print("oof")'''
    lbla = Label(root, text="Hour ID: ")
    lbla.grid(column=0, row=0)
    txta = Entry(root, width=20)
    txta.grid(column=1, row=0)
    txta.insert(END, a)
    hour_current_editing['hourId'] = txta.get()
    lblb = Label(root, text="Student Number: ")
    lblb.grid(column=0, row=1)
    txtb = Entry(root, width=20)
    txtb.grid(column=1, row=1)
    txtb.insert(END, b)
    hour_current_editing['studentNumber'] = txtb.get()
    lblc = Label(root, text="Date: ")
    lblc.grid(column=0, row=2)
    txtc = Entry(root, width=20)
    txtc.grid(column=1, row=2)
    txtc.insert(END, c)
    hour_current_editing['date'] = txtc.get()
    lbld = Label(root, text="Number of Hours: ")
    lbld.grid(column=0, row=3)
    txtd = Entry(root, width=20)
    txtd.grid(column=1, row=3)
    txtd.insert(END, d)
    hour_current_editing['hours'] = txtd.get()
    btn = Button(root, text="Save Current Hours", command=save_current_hour)
    btn.grid(column=0, row=5)
    root.mainloop()

def save_current_hour():
    global combo
    global data
    global hour_current_editing
    global txta, txtb, txtc, txtd
    append = 0
    hour_current_editing['hourId'] = txta.get()
    hour_current_editing['studentNumber'] = txtb.get()
    hour_current_editing['date'] = txtc.get()
    hour_current_editing['hours'] = txtd.get()
    hourID_current_editing = combo.get()
    hours_current = data['hours']
    hour_current_location = findHourLocation(data, hourID_current_editing)
    if str(hour_current_location) == "<type 'exceptions.Exception'>":
        hour_current_location = len(hours_current)
        hours_current.append("")
    hours_current[hour_current_location] = hour_current_editing
    data['hours'] = hours_current
    saveDatabase(data, file)

def rootScreen(): #window responsible for the main screen
    global file
    global root
    root = Tk()
    root.title("P.S.H.M.")
    root.geometry('250x250')
    lbla = Label(root, text="PieMadd Service", font=("Arial Bold", 16))
    lblb = Label(root, text="Hours Manager", font=("Arial Bold", 16))
    lbla.place(relx=0.5, rely=0.1, anchor=CENTER)
    lblb.place(relx=0.5, rely=0.25, anchor=CENTER)
    openFile = Button(root, text="Open Database", command=findFilePath)
    openFile.place(relx=0.5, rely=0.5, anchor=CENTER)
    root.mainloop()
    if file != "":
        mainScreen()
    else:
        messagebox.showerror('File Type Error', 'Invalid file type used. Please open a correctly formatted JSON File and try again.')

def findFilePath():
    global file
    global root
    global data
    file = filedialog.askopenfilename(filetypes=(("JSON Files", "*.json"), ("All Files", "*.*")))
    data = loadDatabase(file)
    root.destroy()

def mainScreen():
    global file
    global main
    global root
    main = Tk()
    main.title("P.S.H.M.")
    main.geometry('250x250')
    lbla = Label(main, text="PieMadd Service", font=("Arial Bold", 16))
    lblb = Label(main, text="Hours Manager", font=("Arial Bold", 16))
    lblc = Label(main, text="Please select whether you", font=("Arial", 12))
    lbld = Label(main, text="would like to manage the", font=("Arial", 12))
    lble = Label(main, text="users or service hours:", font=("Arial", 12))
    lbla.place(relx=0.5, rely=0.1, anchor=CENTER)
    lblb.place(relx=0.5, rely=0.25, anchor=CENTER)
    lblc.place(relx=0.5, rely=0.4, anchor=CENTER)
    lbld.place(relx=0.5, rely=0.5, anchor=CENTER)
    lble.place(relx=0.5, rely=0.6, anchor=CENTER)
    userManage = Button(main, text="Manage Users", command=userManage_start)
    userManage.place(relx=0.3, rely=0.8, anchor=CENTER)
    hoursManage = Button(main, text="Manage Hours", command=hourManage_start)
    hoursManage.place(relx=0.7, rely=0.8, anchor=CENTER)
    main.mainloop()