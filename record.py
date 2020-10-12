import backendy
from tkinter import *
def csss():
    backendy.csv()


def get_selected_row(event):
     global selected_tuple
     index=l1.curselection()[0]
     selected_tuple=l1.get(index)
     e1.delete(0,END)
     e1.insert(END,selected_tuple[1])
     e2.delete(0, END)
     e2.insert(END, selected_tuple[2])
     e3.delete(0, END)
     e3.insert(END, selected_tuple[0])
     e4.delete(0, END)
     e4.insert(END, selected_tuple[3])
     em1.delete(0, END)
     em1.insert(END, selected_tuple[4])
     em2.delete(0, END)
     em2.insert(END, selected_tuple[5])
     em3.delete(0, END)
     em3.insert(END, selected_tuple[6])
     em4.delete(0, END)
     em4.insert(END, selected_tuple[7])
     em5.delete(0, END)
     em5.insert(END, selected_tuple[8])


def insert_command():
    backendy.insert(e3.get(),e1.get(),e2.get(),e4.get(),em1.get(),em2.get(),em3.get(),em4.get(),em5.get())
    l1.delete(0,END)
    l1.insert(END,(e3.get(),e1.get(),e2.get(),e4.get(),em1.get(),em2.get(),em3.get(),em4.get(),em5.get()))

def view_command():
           l1.delete(0,END)
           for row in backendy.view():
               l1.insert(END,row)

def search_command():
    l1.delete(0,END)
    for row in backendy.search(e1.get(),e3.get()):
        l1.insert(END,row)
        print(row)

def update_command():
    backendy.update(e3.get(),e1.get(),e2.get(),e4.get(),em1.get(),em2.get(),em3.get(),em4.get(),em5.get())
    for row in backendy.search(e1.get(),e3.get()):
        l1.delete(0,END)
        l1.insert(END,row)

def delete_command():
    backendy.delete(e3.get())

window=Tk()

#Entries: Name,Attendence,USN,Subject
details=Label(window,text="Details of the Student:")
details.grid(row=0,column=1,)
t1=Label(window,text="Name:")
t1.grid(row=2,column=0)
e1=Entry(window)
e1.grid(row=2,column=1)

t4=Label(window,text="Subject:")
t4.grid(row=3,column=0)
e2=Entry(window)
e2.grid(row=3,column=1)

t2=Label(window,text="USN:")
t2.grid(row=2,column=4)
e3=Entry(window)
e3.grid(row=2,column=5)

t3=Label(window,text="Attendence:")
t3.grid(row=3,column=4)
e4=Entry(window)
e4.grid(row=3,column=5)


#Subject marks label from Event 1 to Event 5
event1=Label(window,text="Event1:")
event1.grid(row=5,column=0,rowspan=3)
event2=Label(window,text="Event2:")
event2.grid(row=8,column=0,rowspan=3)
event3=Label(window,text="Event3:")
event3.grid(row=11,column=0,rowspan=3)
event4=Label(window,text="Event4:")
event4.grid(row=14,column=0,rowspan=3)
event5=Label(window,text="Event5:")
event5.grid(row=17,column=0,rowspan=3)


#Subjects marks entry from event 1 to 5

em1=Entry(window)
em1.grid(row=5,column=1,rowspan=2)
em2=Entry(window)
em2.grid(row=8,column=1,rowspan=2)
em3=Entry(window)
em3.grid(row=11,column=1,rowspan=2)
em4=Entry(window)
em4.grid(row=14,column=1,rowspan=2)
em5=Entry(window)
em5.grid(row=17,column=1,rowspan=2)

#Buttons for adding,deleting,updating,searching,View all,close
b1=Button(window,text="Add Entry",width=20,command=insert_command)
b1.grid(row=5,column=5)
b2=Button(window,text="Update Entry",width=20,command=update_command)
b2.grid(row=8,column=5)
b3=Button(window,text="Search Entry",width=20,command=search_command)
b3.grid(row=11,column=5)
b4=Button(window,text="View All",width=20,command=view_command)
b4.grid(row=14,column=5)
b5=Button(window,text="Delete",width=20,command=delete_command)
b5.grid(row=17,column=5)
b6=Button(window,text="Export",width=20,command=csss)
b6.grid(row=18,column=5)
#ListView
l1=Listbox(window,height=50,width=100)
l1.grid(row=21,column=0,columnspan=6)

sb1=Scrollbar(window)
sb1.grid(row=21,column=10)
l1.configure(yscrollcommand=sb1.set)
sb1.configure(command=l1.yview())

# Binding the event(Current selection)
l1.bind('<<ListboxSelect>>',get_selected_row)


window.mainloop()
print(selected_tuple)
