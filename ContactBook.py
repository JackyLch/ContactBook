import sys
import os.path
import time
import pickle
from tkinter import *
from tkinter import messagebox

# Setup the window with fixed size and non-adjustable size
app = Tk()
app.geometry('500x300')
app.title('Contact List')
app.config(bg='#beedc0')
app.resizable(False, False)

# load the existing data from file
if os.path.isfile('./contacts.txt') == True and os.stat('./contacts.txt').st_size != 0:
    with open('./contacts.txt', 'rb') as f:
        contactlist = pickle.load(f)

if os.path.isfile('./contacts.txt') == False or os.stat('./contacts.txt').st_size == 0:
    # set the default values for the program to startup if contacts.txr file doesn't exist
    contactlist = [
        ['Bill Gate',  '12345678'],
        ['Tim Apple',  '23456789'],
        ['The Rock',   '11111111'],
        ['Barack Obama', '99999999'],
    ]

with open('./contacts.txt', 'wb') as f:
    pickle.dump(contactlist, f)

NAME = StringVar()
PHONENUMBER = StringVar()

frame = Frame(app)
frame.pack(side=RIGHT)
scrollbar = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scrollbar.set, height=12)
scrollbar.config(command=select.xview)
scrollbar.pack(side=LEFT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)


def selected_contact():
    # get the currently selected ListBox from the frame
    return int(select.curselection()[0])


def add():
    if NAME.get() == '' or PHONENUMBER.get() == '':
        return
    contactlist.append([NAME.get(), PHONENUMBER.get()])
    with open('./contacts.txt', 'wb') as f:
        pickle.dump(contactlist, f)
    Select_set()


def delete():
    del contactlist[selected_contact()]
    contactlist.sort()
    with open('./contacts.txt', 'wb') as f:
        pickle.dump(contactlist, f)
    Select_set()


def show():
    NAME, PHONENUMBER = contactlist[selected_contact()]
    choice = messagebox.askquestion(
        "Contact Info", NAME + "\n" + PHONENUMBER + "\nCorrect?\n" + "Pressing No Will Delete Set Entry")
    if choice == "no":
        delete()


def exit():
    with open('./contacts.txt', 'wb') as f:
        pickle.dump(contactlist, f)
    app.destroy()


def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for NAME, PHONENUMBER in contactlist:
        select.insert(END, NAME)
    with open('./contacts.txt', 'wb') as f:
        pickle.dump(contactlist, f)


time_string = time.strftime('%H:%M:%S')


def LabelsSetup():
    Label(app, text='Name', font='arial 12 bold',
          bg='#beedc0').place(x=30, y=20)
    Entry(app, textvariable=NAME).place(x=150, y=20)
    Label(app, text='Phone Number', font='arial 12 bold',
          bg='#beedc0').place(x=30, y=70)
    Entry(app, textvariable=PHONENUMBER).place(x=150, y=70)


def ButtonsSetup():
    Button(app, text="ADD", font='arial 12 bold',
           bg='#a2fce4', command=add).place(x=30, y=110)
    Button(app, text="DELETE", font='arial 12 bold',
           bg='#a2fce4', command=delete).place(x=100, y=110)
    Button(app, text="SHOW", font='arial 12 bold',
           bg='#a2fce4', command=show).place(x=200, y=110)
    Button(app, text="EXIT", font='arial 12 bold',
           bg='orange', command=exit).place(x=200, y=200)


Select_set()
ButtonsSetup()
LabelsSetup()
app.mainloop()
