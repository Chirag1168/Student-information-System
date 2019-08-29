from Tkinter import *
import tkMessageBox
import MySQLdb
def clear():
    vv1.set('')
    vv2.set('')
    v1.set('')
    v2.set('')
    v3.set('')
    
def search():
    db = MySQLdb.connect("localhost","root", "123456","student" )
    cursor = db.cursor()
    rn=int(vv1.get())
    sql = "SELECT * FROM stu where rollno = '%d'" % (rn)
    try:
        c=cursor.execute(sql)
        if(c==0):
            tkMessageBox.showinfo( "Result", 'Rollno not found')
        results = cursor.fetchall()
        for row in results:
            rn = row[0]
            nm = row[1]
            fnm = row[2]
            ad = row[3]
            br = row[4]
            vv2.set(nm)
            v1.set(fnm)
            v2.set(ad)
            v3.set(br)
    except:
        print "Error: unable to fecth data"
    db.close()
def delete():
    db = MySQLdb.connect("localhost", "root","123456","student")
    cursor = db.cursor()
    rn=int(vv1.get())
           # Prepare SQL query to DELETE a record 
    sql = "delete from stu where rollno = '%d'" % (rn)
    try:
        c=cursor.execute(sql)
# Commit your changes in the database
        db.commit()
        tkMessageBox.showinfo( "Result", 'record Deleted')
    except:
# Rollback in case there is any error
        db.rollback()
        tkMessageBox.showinfo( "Result", 'record not Deleted')
    db.close()

def update():
    db = MySQLdb.connect("localhost", "root","123456","student")
    cursor = db.cursor()
    rn=int(vv1.get())
    nm=vv2.get()
    fnm=v1.get()
    ad=v2.get()
    br=v3.get()
    sql = "update stu set name = '%s', Fname= '%s', address = '%s', branch = '%s' where rollno = '%d'" % (nm,fnm,ad,br,rn)
    try:
        c=cursor.execute(sql)
# Commit your changes in the database
        db.commit()
        tkMessageBox.showinfo( "Result", 'record updated')
    except:
# Rollback in case there is any error
        db.rollback()
        tkMessageBox.showinfo( "Result", 'record not updated')
    db.close()


def save1():
    db = MySQLdb.connect("localhost", "root","123456","student")
    cursor = db.cursor()
    rn=int(vv1.get())
    nm=vv2.get()
    fnm=v1.get()
    ad=v2.get()
    br=v3.get()
    
    sql = "INSERT INTO STU VALUES ('%d', '%s', '%s', '%s', '%s' )" % (rn,nm,fnm,ad,br)
    try:
# Execute the SQL command
        cursor.execute(sql)
# Commit your changes in the database
        db.commit()
        tkMessageBox.showinfo( "Result", 'record Added')
    except:
# Rollback in case there is any error
        db.rollback()
        tkMessageBox.showinfo( "Result", 'record not Added')
# disconnect from server
    db.close()
 

def check():
    if(var.get()==1):
        newwin2 = Toplevel(top)
        clear()
        
        display = Label(newwin2, text="Add New Student")
        display.grid(row=0, column=1)
        l1=Label(newwin2, text="Rollno ")
        l2=Label(newwin2, text="Name ")
        l3=Label(newwin2, text="Father Name ")
        l4=Label(newwin2, text="Address ")
        l5=Label(newwin2, text="Branch ")
        l1.grid(row=1)
        l2.grid(row=2)
        l3.grid(row=3)
        l4.grid(row=4)
        l5.grid(row=5)

        e1 = Entry(newwin2, textvariable=vv1)
        e2 = Entry(newwin2, textvariable=vv2)
        e3 = Entry(newwin2, textvariable=v1)
        e4 = Entry(newwin2, textvariable=v2)
        e5 = Entry(newwin2, textvariable=v3)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        e4.grid(row=4, column=1)
        e5.grid(row=5, column=1)

        b1 = Button(newwin2, text ="SAVE", command = save1)
        b1.grid(row=6, column=0)


    elif(var.get()==2):
        newwin2 = Toplevel(top)
        clear()
        display = Label(newwin2, text="Student Details")
        display.pack()
        T = Text(newwin2, height=5, width=60)
        T.pack()
        db = MySQLdb.connect("localhost","root","123456","student" )
        cursor = db.cursor()
        sql = "select * from stu"
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            res="Rollno   Name   Fname   Address   Branch"
            T.insert(END,res)
            for row in results:
                rn = row[0]
                nm = row[1]
                fnm = row[2]
                ad = row[3]
                br = row[4]
                res="\n%d      %s   %s   %s   %s" % (rn, nm, fnm, ad,br)
                T.insert(END, res)
        except:
            print "Error: unable to fetch data"
        # disconnect from server
        db.close()
    elif(var.get()==3):
        newwin2 = Toplevel(top)
        clear()
        display = Label(newwin2, text="Delete Student")
        display.grid(row=0, column=1)
        l1=Label(newwin2, text="Rollno ")
        l2=Label(newwin2, text="Name ")
        l3=Label(newwin2, text="Father Name ")
        l4=Label(newwin2, text="Address ")
        l5=Label(newwin2, text="Branch ")
        l1.grid(row=1)
        l2.grid(row=2)
        l3.grid(row=3)
        l4.grid(row=4)
        l5.grid(row=5)

        e1 = Entry(newwin2, textvariable=vv1)
        e2 = Entry(newwin2, textvariable=vv2)
        e3 = Entry(newwin2, textvariable=v1)
        e4 = Entry(newwin2, textvariable=v2)
        e5 = Entry(newwin2, textvariable=v3)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        e4.grid(row=4, column=1)
        e5.grid(row=5, column=1)

        b1 = Button(newwin2, text ="SEARCH", command = search)
        b1.grid(row=6, column=0)
        b2 = Button(newwin2, text ="DELETE", command = delete)
        b2.grid(row=6, column=1)
    elif(var.get()==4):
        newwin2 = Toplevel(top)
        clear()
        display = Label(newwin2, text="Update Student")
        display.grid(row=0, column=1)
        l1=Label(newwin2, text="Rollno ")
        l2=Label(newwin2, text="Name ")
        l3=Label(newwin2, text="Father Name ")
        l4=Label(newwin2, text="Address ")
        l5=Label(newwin2, text="Branch ")
        l1.grid(row=1)
        l2.grid(row=2)
        l3.grid(row=3)
        l4.grid(row=4)
        l5.grid(row=5)

        e1 = Entry(newwin2, textvariable=vv1)
        e2 = Entry(newwin2, textvariable=vv2)
        e3 = Entry(newwin2, textvariable=v1)
        e4 = Entry(newwin2, textvariable=v2)
        e5 = Entry(newwin2, textvariable=v3)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        e4.grid(row=4, column=1)
        e5.grid(row=5, column=1)

        b1 = Button(newwin2, text ="SEARCH", command = search)
        b1.grid(row=6, column=0)
        b2 = Button(newwin2, text ="UPDATE", command = update)
        b2.grid(row=6, column=1)
    elif(var.get()==5):
        newwin2 = Toplevel(top)
        clear()
        display = Label(newwin2, text="Search Student")
        display.grid(row=0, column=1)
        l1=Label(newwin2, text="Rollno ")
        l2=Label(newwin2, text="Name ")
        l3=Label(newwin2, text="Father Name ")
        l4=Label(newwin2, text="Address ")
        l5=Label(newwin2, text="Branch ")
        l1.grid(row=1)
        l2.grid(row=2)
        l3.grid(row=3)
        l4.grid(row=4)
        l5.grid(row=5)

        e1 = Entry(newwin2, textvariable=vv1)
        e2 = Entry(newwin2, textvariable=vv2)
        e3 = Entry(newwin2, textvariable=v1)
        e4 = Entry(newwin2, textvariable=v2)
        e5 = Entry(newwin2, textvariable=v3)

        e1.grid(row=1, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=3, column=1)
        e4.grid(row=4, column=1)
        e5.grid(row=5, column=1)

        b1 = Button(newwin2, text ="SEARCH", command = search)
        b1.grid(row=6, column=0)
        

    else:
        top.destroy()
def disp():
    nm=e1.get()
    pa=e2.get()
    if(nm == 'System' and pa == 'Manager'):
        tkMessageBox.showinfo( "Result","Valid User name and password")
        newwin = Toplevel(top)
        top.withdraw()
        display = Label(newwin, text="Student Information System")
        display.pack()
    
        r1 = Radiobutton(newwin, text="Add New Student", variable=var, value=1)
        r1.pack( anchor = W )
        r2 = Radiobutton(newwin, text="Display Student", variable=var, value=2)
        r2.pack( anchor = W )
        r3 = Radiobutton(newwin, text="Delete Student", variable=var, value=3)
        r3.pack( anchor = W)
        r4 = Radiobutton(newwin, text="Update Student", variable=var, value=4)
        r4.pack( anchor = W)
        r5 = Radiobutton(newwin, text="Search Student", variable=var, value=5)
        r5.pack( anchor = W)
        r6 = Radiobutton(newwin, text="Exit Application", variable=var, value=6)
        r6.pack( anchor = W)
        
        b1 = Button(newwin, text ="GO", command = check)
        b1.pack()

    else:
        tkMessageBox.showinfo( "Result","Invalid User name and password")
top = Tk()
l1=Label(top, text="User Name ")
l2=Label(top, text="Password ")
l1.grid(row=0)
l2.grid(row=1)

var = IntVar()
vv1 = StringVar()
vv2 = StringVar()
v1 = StringVar()
v2 = StringVar()
v3 = StringVar()
       
e1 = Entry(top)
e2 = Entry(top, show='*')

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button(top, text ="CHECK", command = disp)
b1.grid(row=2, column=1)
top.mainloop()
