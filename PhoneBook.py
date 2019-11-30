from Tkinter import *
from tkMessageBox import *
import sqlite3
import CoverPhoneBook
## Main Root Window Declaration
root=Tk()
root.title("PhoneBook")
root.geometry("1000x1000")
root.configure(background="#B3FFE3")
## SQLite3 Database Connection and Table Creation
con=sqlite3.Connection("PhoneBook")
cur=con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS CONTACTDETAILS(CONTACTID INTEGER PRIMARY KEY AUTOINCREMENT,FNAME VARCHAR(30),MNAME VARCHAR(30),LNAME VARCHAR(30),COMNAME VARCHAR(30),ADDR VARCHAR(50),CITY VARCHAR(20),ZIPCODE CHAR(6),WEB VARCHAR(30),DOB DATE)')
cur.execute('CREATE TABLE IF NOT EXISTS CONTACTNUMBERS(CONTACTID INTEGER,PHNO NUMBER(10),PH CHAR(6),PRIMARY KEY(CONTACTID,PHNO),FOREIGN KEY(CONTACTID) REFERENCES CONTACTDETAILS(CONTACTID))')
cur.execute('CREATE TABLE IF NOT EXISTS CONTACTEMAILS(CONTACTID INTEGER,EMID VARCHAR(30),EM CHAR(8),PRIMARY KEY(CONTACTID,EMID)FOREIGN KEY(CONTACTID) REFERENCES CONTACTDETAILS(CONTACTID))')
con.commit()
## Main Root Window
h=0
Label(root,text="Phone Book",font="Garamond 25",bg="#D0FFED").grid(row=h,column=1,sticky="N")
photo=PhotoImage(file="PhoneBook.gif")
Label(root,image=photo).grid(row=h+1,column=1)
Label(root,text="First Name: ",font="Garamond 14",bg="#D0FFED").grid(row=h+2,column=0,sticky="E")
fname=Entry(root,bg="#E3FFF3")
fname.grid(row=h+2,column=1)
Label(root,text="*Mandatory Field",font="Garamond 10",bg="#D0FFED").grid(row=h+2,column=2,sticky="W")
Label(root,text="Middle Name: ",font="Garamond 14",bg="#D0FFED").grid(row=h+3,column=0,sticky="E")
mname=Entry(root,bg="#E3FFF3")
mname.grid(row=h+3,column=1)
Label(root,text="Last Name: ",font="Garamond 14",bg="#D0FFED").grid(row=h+4,column=0,sticky="E")
lname=Entry(root,bg="#E3FFF3")
lname.grid(row=h+4,column=1)
Label(root,text="Company Name: ",font="Garamond 14",bg="#D0FFED").grid(row=h+5,column=0,sticky="E")
comname=Entry(root,bg="#E3FFF3")
comname.grid(row=h+5,column=1)
Label(root,text="Address: ",font="Garamond 14",bg="#D0FFED").grid(row=h+6,column=0,sticky="E")
add=Entry(root,bg="#E3FFF3")
add.grid(row=h+6,column=1)
Label(root,text="City: ",font="Garamond 14",bg="#D0FFED").grid(row=h+7,column=0,sticky="E")
city=Entry(root,bg="#E3FFF3")
city.grid(row=h+7,column=1)
Label(root,text="ZIP Code: ",font="Garamond 14",bg="#D0FFED").grid(row=h+8,column=0,sticky="E")
zipcode=Entry(root,bg="#E3FFF3")
zipcode.grid(row=h+8,column=1)
Label(root,text="Website: ",font="Garamond 14",bg="#D0FFED").grid(row=h+9,column=0,sticky="E")
web=Entry(root,bg="#E3FFF3")
web.grid(row=h+9,column=1)
Label(root,text="Date of Birth(YYYY-MM-DD): " ,font="Garamond 14",bg="#D0FFED").grid(row=h+10,column=0,sticky="E")
dob=Entry(root,bg="#E3FFF3")
dob.grid(row=h+10,column=1)
i=11
j=13
phno=IntVar()
ph=StringVar()
emid=StringVar()
em=StringVar()
offph=0
homph=0
mobph=0
offem=0
perem=0
tempd=0
tempn=0
tempe=0
t=0
conid=0
iphno=[]
def addph():
    global i,j,phno,ph,offph,homph,mobph,iphno
    i=i+2
    addem()
    Label(root,text="Select Phone Type: ",font="Garamond 14",bg="#D0FFED").grid(row=i,column=0,sticky="E")
    offph=Radiobutton(root,text="Office",variable=ph,value="Office",tristatevalue=0,font="Garamond 14",bg="#D0FFED")
    offph.grid(row=i,column=1)
    homph=Radiobutton(root,text="Home",variable=ph,value="Home",tristatevalue=0,font="Garamond 14",bg="#D0FFED")
    homph.grid(row=i,column=2,sticky="W")
    mobph=Radiobutton(root,text="Mobile",variable=ph,value="Mobile",tristatevalue=0,font="Garamond 14",bg="#D0FFED")
    mobph.grid(row=i,column=3,sticky="W")
    Label(root,text="Phone Number: ",font="Garamond 14",bg="#D0FFED").grid(row=i+1,column=0,sticky="E")
    phno=Entry(root,bg="#E3FFF3")
    phno.grid(row=i+1,column=1)
    Label(root,text="*Mandatory Field",font="Garamond 10",bg="#D0FFED").grid(row=i+1,column=2,sticky="W")
    def appph():
        global iphno
        iphno.append(str(phno.get()))
    appph()
    Button(root,text="+",command=addph,bg="#88FFD1").grid(row=i,column=4)
def addem():
    global i,j,emid,em,offem,perem,iphno
    j=j+2
    print iphno
    Label(root,text="Select E-mail Type: ",font="Garamond 14",bg="#D0FFED").grid(row=j,column=0,sticky="E")
    offem=Radiobutton(root,text="Office",variable=em,value="Office",tristatevalue=0,font="Garamond 14",bg="#D0FFED")
    offem.grid(row=j,column=1)
    perem=Radiobutton(root,text="Personal",variable=em,value="Personal",tristatevalue=0,font="Garamond 14",bg="#D0FFED")
    perem.grid(row=j,column=2)
    Label(root,text="E-mail ID: ",font="Garamond 14",bg="#D0FFED").grid(row=j+1,column=0,sticky="E")
    emid=Entry(root,bg="#E3FFF3")
    emid.grid(row=j+1,column=1)
    Label(root,text="*Mandatory Field",font="Garamond 10",bg="#D0FFED").grid(row=j+1,column=2,sticky="W")
    Button(root,text="+",command=addem,bg="#88FFD1").grid(row=j,column=4)
def save():
    global phno,emid,ph,em,offph,homph,mobph,offem,perem,iphno
    if fname.get()=="":
        showerror("Save","Please enter your First Name!")
        return
    if fname.get()==mname.get() and mname.get()==lname.get():
        showerror("Save","First Name, Middle Name and Last Name cannot be same!")
        return
    if ((len(phno.get()))!=10) or (phno.get()).isdigit()==False:
        showerror("Save","Phone Number must be of 10 digits!")
        return
    cur.execute('INSERT INTO CONTACTDETAILS (FNAME,MNAME,LNAME,COMNAME,ADDR,CITY,ZIPCODE,WEB,DOB) VALUES(?,?,?,?,?,?,?,?,?)',(fname.get(),mname.get(),lname.get(),comname.get(),add.get(),city.get(),zipcode.get(),web.get(),dob.get()))
    cur.execute('SELECT MAX(CONTACTID) FROM CONTACTDETAILS')
    idr=cur.fetchall()
    idr=int(idr[0][0])
    cur.execute('INSERT INTO CONTACTNUMBERS (CONTACTID,PHNO,PH) VALUES(?,?,?)',(idr,phno.get(),ph.get()))
    cur.execute('INSERT INTO CONTACTEMAILS (CONTACTID,EMID,EM) VALUES(?,?,?)',(idr,emid.get(),em.get()))
    con.commit()
    showinfo("Save","Contact saved successfully!")
    fname.delete(0,END)
    mname.delete(0,END)
    lname.delete(0,END)
    comname.delete(0,END)
    add.delete(0,END)
    city.delete(0,END)
    zipcode.delete(0,END)
    web.delete(0,END)
    dob.delete(0,END)
    phno.delete(0,END)
    emid.delete(0,END)
    offph.deselect()
    homph.deselect()
    mobph.deselect()
    offem.deselect()
    perem.deselect()
def search():
    global tempd,tempn,tempe,t,conid
    sroot=Tk()
    sroot.configure(background="#FFB588")
    sroot.title("Search PhoneBook")
    sroot.geometry("1000x1000")
    Label(sroot,text="Search PhoneBook",font="Garamond 25",bg="#FFD6B2").grid(row=0,columnspan=4)
    Label(sroot,text="Search Here: ",font="Garamond 14",bg="#FFD6B2").grid(row=1,column=0)
    s=Entry(sroot,bg="#FFF4DE",width=35)
    s.grid(row=1,column=1)
    def showrecord(e=1):
        try:
            global tempd,tempn,tempe,t,conid
            t=lb.curselection()
            lb.delete(0,END)
            t=t[0]
            lb.config(fg="BLACK",font="Garamond 11")
            conid=tempd[t][0]
            lb.insert(END,"Contact Details for: {}".format(tempd[t][1]+" "+tempd[t][2]+" "+tempd[t][3]))
            lb.insert(END,"First Name: {}".format(tempd[t][1]))
            lb.insert(END,"Middle Name: {}".format(tempd[t][2]))
            lb.insert(END,"Last Name: {}".format(tempd[t][3]))
            lb.insert(END,"Company Name: {}".format(tempd[t][4]))
            lb.insert(END,"Address: {}".format(tempd[t][5]))
            lb.insert(END,"City: {}".format(tempd[t][6]))
            lb.insert(END,"ZIP Code: {}".format(tempd[t][7]))
            lb.insert(END,"Website: {}".format(tempd[t][8]))
            lb.insert(END,"DOB: {}".format(tempd[t][9]))
            cur.execute("SELECT * FROM CONTACTNUMBERS WHERE CONTACTID=?",(tempd[t][0],))
            tempn=cur.fetchall()
            cur.execute("SELECT * FROM CONTACTEMAILS WHERE CONTACTID=?",(tempd[t][0],))
            tempe=cur.fetchall()
            lb.insert(END,"Phone Number: {}".format(tempn[0][1]))
            lb.insert(END,"E-mail Address: {}".format(tempe[0][1]))
            lb.configure(state=DISABLED)
            Button(sroot,text="EDIT",command=iedit,bg="#FEA365").grid(row=3,column=2)
            Button(sroot,text="DELETE",command=searchdelete,bg="#FEA365").grid(row=3,column=3)
        except IndexError:
            None
    def iedit():
        sroot.destroy()
        global tempd,tempn,tempe,conid
        eroot=Tk()
        eroot.title("Edit PhoneBook")
        eroot.geometry("600x600")
        eroot.configure(background="#00DDFF")
        cur.execute("SELECT * FROM CONTACTDETAILS WHERE CONTACTID=?",(conid,))
        tempd=cur.fetchall()
        cur.execute("SELECT * FROM CONTACTNUMBERS WHERE CONTACTID=?",(conid,))
        tempn=cur.fetchall()
        cur.execute("SELECT * FROM CONTACTEMAILS WHERE CONTACTID=?",(conid,))
        tempe=cur.fetchall()
        Label(eroot,text="Edit PhoneBook",font="Garamond 25",bg="#80EAFF").grid(row=0,column=1)
        Label(eroot,text="First Name: ",font="Garamond 14",bg="#80EAFF").grid(row=1,column=0,sticky="E")
        newfname=Entry(eroot,bg="#ACF1FF")
        newfname.grid(row=1,column=1)
        newfname.insert(0,tempd[0][1])
        Label(eroot,text="Middle Name: ",font="Garamond 14",bg="#80EAFF").grid(row=2,column=0,sticky="E")
        newmname=Entry(eroot,bg="#ACF1FF")
        newmname.grid(row=2,column=1)
        newmname.insert(0,tempd[0][2])
        Label(eroot,text="Last Name: ",font="Garamond 14",bg="#80EAFF").grid(row=3,column=0,sticky="E")
        newlname=Entry(eroot,bg="#ACF1FF")
        newlname.grid(row=3,column=1)
        newlname.insert(0,tempd[0][3])
        Label(eroot,text="Company Name: ",font="Garamond 14",bg="#80EAFF").grid(row=4,column=0,sticky="E")
        newcomname=Entry(eroot,bg="#ACF1FF")
        newcomname.grid(row=4,column=1)
        newcomname.insert(0,tempd[0][4])
        Label(eroot,text="Address: ",font="Garamond 14",bg="#80EAFF").grid(row=5,column=0,sticky="E")
        newadd=Entry(eroot,bg="#ACF1FF")
        newadd.grid(row=5,column=1)
        newadd.insert(0,tempd[0][5])
        Label(eroot,text="City: ",font="Garamond 14",bg="#80EAFF").grid(row=6,column=0,sticky="E")
        newcity=Entry(eroot,bg="#ACF1FF")
        newcity.grid(row=6,column=1)
        newcity.insert(0,tempd[0][6])
        Label(eroot,text="ZIP Code: ",font="Garamond 14",bg="#80EAFF").grid(row=7,column=0,sticky="E")
        newzipcode=Entry(eroot,bg="#ACF1FF")
        newzipcode.grid(row=7,column=1)
        newzipcode.insert(0,tempd[0][7])
        Label(eroot,text="Website: ",font="Garamond 14",bg="#80EAFF").grid(row=8,column=0,sticky="E")
        newweb=Entry(eroot,bg="#ACF1FF")
        newweb.grid(row=8,column=1)
        newweb.insert(0,tempd[0][8])
        Label(eroot,text="DOB: ",font="Garamond 14",bg="#80EAFF").grid(row=9,column=0,sticky="E")
        newdob=Entry(eroot,bg="#ACF1FF")
        newdob.grid(row=9,column=1)
        newdob.insert(0,tempd[0][9])
        Label(eroot,text="Phone Number: ",font="Garamond 14",bg="#80EAFF").grid(row=10,column=0,sticky="E")
        newphno=Entry(eroot,bg="#ACF1FF")
        newphno.grid(row=10,column=1)
        newphno.insert(0,tempn[0][1])
        Label(eroot,text="Email Address: ",font="Garamond 14",bg="#80EAFF").grid(row=11,column=0,sticky="E")
        newemid=Entry(eroot,bg="#ACF1FF")
        newemid.grid(row=11,column=1)
        newemid.insert(0,tempe[0][1])
        def ed():
            cur.execute("UPDATE CONTACTDETAILS SET FNAME=?,MNAME=?,LNAME=?,COMNAME=?,ADDR=?,CITY=?,ZIPCODE=?,WEB=?,DOB=? WHERE CONTACTID=?",(newfname.get(),newmname.get(),newlname.get(),newcomname.get(),newadd.get(),newcity.get(),newzipcode.get(),newweb.get(),newdob.get(),conid))
            cur.execute("UPDATE CONTACTNUMBERS SET PHNO=? WHERE CONTACTID=?",(newphno.get(),conid))
            cur.execute("UPDATE CONTACTEMAILS SET EMID=? WHERE CONTACTID=?",(newemid.get(),conid))
            con.commit()
            showinfo("Edit","Contact updated successfully!")
            eroot.destroy()
        def eclose():
            eroot.destroy()
        Button(eroot,text="SAVE",command=ed,bg="#00B3F5").grid(row=14,column=1)
        Button(eroot,text="CLOSE",command=eclose,bg="#00B3F5").grid(row=14,column=2)
        eroot.mainloop()
    def searchdata(e=1):
        global tempd
        lb.configure(state=NORMAL)
        lb.delete(0,END)
        lb.config(fg="DARK RED",font="Garamond 11")
        cur.execute("SELECT * FROM CONTACTDETAILS WHERE FNAME LIKE '%{}%' OR MNAME LIKE '%{}%' OR LNAME LIKE '%{}%' ORDER BY FNAME".format(s.get(),s.get(),s.get(),s.get()))
        tempd=cur.fetchall()
        for i in range(0,len(tempd)):
            name=tempd[i][1]+" "+tempd[i][2]+" "+tempd[i][3]
            lb.insert(END,name)
        lb.bind("<Double-Button-1>",showrecord)
    def searchclose():
        sroot.destroy()
    def searchdelete():
        x=askyesno("Delete","Are you sure you want to delete?")
        if x==True:
            cur.execute("DELETE FROM CONTACTDETAILS WHERE CONTACTID=?",(tempd[t][0],))
            cur.execute("DELETE FROM CONTACTNUMBERS WHERE CONTACTID=?",(tempd[t][0],))
            cur.execute("DELETE FROM CONTACTEMAILS WHERE CONTACTID=?",(tempd[t][0],))
            con.commit()
            lb.delete(0,END)
            showinfo("Delete","Contact deleted successfully!")
            sroot.destroy()
        else:
            sroot.destroy()
    Button(sroot,text="CLOSE",command=searchclose,bg="#FEA365").grid(row=3,column=1)
    lb=Listbox(sroot,width=100,height=30,bg="#FFF4DE")
    lb.grid(row=2,columnspan=4)
    lb.config(fg="DARK RED",font="Garamond 11")
    cur.execute("SELECT * FROM CONTACTDETAILS ORDER BY FNAME")
    tempd=cur.fetchall()
    for i in range(0,len(tempd)):
        name=tempd[i][1]+" "+tempd[i][2]+" "+tempd[i][3]
        lb.insert(END,name)
    lb.bind("<Double-Button-1>",showrecord)
    s.bind("<KeyPress>",searchdata)
    sroot.mainloop()
def oedit():
    showinfo("Edit","Perform Edit in Search!")
def close():
    showinfo("Bye PhoneBook","Thank You!")
    root.destroy()
addph()
Button(root,text="SAVE",command=save,bg="#88FFD1").grid(row=h+3,column=6)
Button(root,text="SEARCH",command=search,bg="#88FFD1").grid(row=h+5,column=6)
Button(root,text="EDIT",command=oedit,bg="#88FFD1").grid(row=h+7,column=6)
Button(root,text="CLOSE",command=close,bg="#88FFD1").grid(row=h+9,column=6)
root.mainloop()
