from tkinter import *
import Back_End

def get_selected_row(event):
    global selected_row
    #Get Index of Selected Row
    index = list_box.curselection()[0]
    #Get the data of Selected row
    selected_row = list_box.get(index)
    #Clear Entries and Selected Row Data to Entries
    e1.delete(0,END)
    e1.insert(END,selected_row[1])
    e2.delete(0,END)
    e2.insert(END,selected_row[2])
    e3.delete(0,END)
    e3.insert(END,selected_row[3])
    e4.delete(0,END)
    e4.insert(END,selected_row[4])
    e5.delete(0,END)
    e5.insert(END,selected_row[5])
    e6.delete(0,END)
    e6.insert(END,selected_row[6])

#Delete Data from table
def delete_data():
    global selected_row
    Back_End.delete(selected_row[0])

#Function to add data to table
def add_data():
    Back_End.insert(date_text.get(),earn_text.get(),exer_text.get(),study_text.get(),diet_text.get(),py_text.get())
    list_box.delete(0,END)
    list_box.insert(END,(date_text.get(),earn_text.get(),exer_text.get(),study_text.get(),diet_text.get(),py_text.get()))

#Add Retrived Data to ListBox
def view_all():
    #Make the Listbox Empty
    list_box.delete(0,END)
    #Get Data
    for row in Back_End.view():
        #Add Data to Listbox
        list_box.insert(END,row)

#Function to Get Data and add to ListBox
def search():
    #Make the Listbox Empty
    list_box.delete(0,END)
    #Get Data based on search criteria defined in Entry Boxes
    for row in Back_End.search(date_text.get(),earn_text.get(),exer_text.get(),study_text.get(),diet_text.get(),py_text.get()):
        #Add Data to Listbox
        list_box.insert(END,row)

#Create Window Object
win = Tk()
win.title("Data Base System")

#Labels & Their Arrangement
l1 = Label(win,text="Date")
l1.grid(row=0,column=0)

l2 = Label(win,text="Earnings")
l2.grid(row=0,column=2)

l3 = Label(win,text="Exercise")
l3.grid(row=1,column=0)

l4 = Label(win,text="Study")
l4.grid(row=1,column=2)

l5 = Label(win,text="Diet")
l5.grid(row=2,column=0)

l6 = Label(win,text="Python")
l6.grid(row=2,column=2)

#Adding Entries & Their Arrangement
date_text= StringVar()
e1 = Entry(win,textvariable=date_text)
e1.grid(row=0,column=1)

earn_text= StringVar()
e2 = Entry(win,textvariable=earn_text)
e2.grid(row=0,column=3)

exer_text= StringVar()
e3 = Entry(win,textvariable=exer_text)
e3.grid(row=1,column=1)

study_text= StringVar()
e4 = Entry(win,textvariable=study_text)
e4.grid(row=1,column=3)

diet_text= StringVar()
e5 = Entry(win,textvariable=diet_text)
e5.grid(row=2,column=1)

py_text= StringVar()
e6 = Entry(win,textvariable=py_text)
e6.grid(row=2,column=3)

#ListBox
list_box = Listbox(
    win,
    width=35,
    height=8
    )
list_box.grid(row=3,column=0,rowspan=9,columnspan=2)

#Scroll Bar
scroll_bar = Scrollbar(win)
scroll_bar.grid(row=3,column=2,rowspan=9)

#Buttons
b1 = Button(win,text="Add",width=12,pady=5,command=add_data)
b1.grid(row=3,column=3)

b2 = Button(win,text="Search",width=12,pady=5,command=search)
b2.grid(row=4,column=3)

b3 = Button(win,text="Delete Data",width=12,pady=5,command=delete_data)
b3.grid(row=5,column=3)

b4 = Button(win,text="View All",width=12,pady=5,command=view_all)
b4.grid(row=6,column=3)

b5 = Button(win,text="Close",width=12,pady=5,command=win.destroy)
b5.grid(row=7,column=3)


#Attach Scroll Bar to Listbox
list_box.bind('<<ListboxSelect>>',get_selected_row)

#Run GUI
win.mainloop()
