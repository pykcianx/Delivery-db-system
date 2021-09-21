from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import tkinter.messagebox
import tkinter as tk
import sqlite3
import pyodbc
import smtplib

class App:
    def __init__(self,root):
        self.root = root
        self.root.state('zoomed')
        self.root.title("Delivery info")
        self.root.geometry("1920x1080")
        self.root.iconbitmap('icon2.ico')
        self.root.config(bg="#f5f5f7")
        
        def ring():
            root.bell()

        def clickszukaj(event):
            self.szukajentry.config(state=NORMAL)
            self.szukajentry.delete(0, END)
               
        def onclick1():
            my_tree.place_forget()
            my_tree2.place_forget()
            my_tree2.delete(*my_tree2.get_children())
            DodajFrame.place_forget()
            self.btnwydaj1.place_forget()
            self.btnhome.configure(bg="#00bbaa")
            self.btnszukaj.configure(bg="#252643")
            self.btnwydaj.configure(bg="#252643")
            self.btnustawienia.configure(bg="#252643")
            self.szukajentry.place_forget()
            self.btndodaj.place_forget()
            self.napiswydaj.place_forget()
            self.btnwydaj2.place_forget()
            self.wydajentry.place_forget()
            self.napisustmail.place_forget()
            addressentry.place_forget()
            self.btnustmail.place_forget()
            
        def onclick2():
            selection()
            my_tree.place(x = 210,y = 75)
            my_tree2.place_forget()
            my_tree2.delete(*my_tree2.get_children())
            DodajFrame.place(x = 900,y = 75)
            self.btnwydaj1.place(x = 1160,y = 205)
            self.szukajentry.delete(first=0,last=100)
            self.szukajentry.focus_set()
            self.btnhome.configure(bg="#252643")
            self.btnszukaj.configure(bg="#00bbaa")
            self.btnwydaj.configure(bg="#252643")
            self.btnustawienia.configure(bg="#252643")
            self.btndodaj.place(x = 1170,y = 163)
            self.szukajentry.place(x= 930,y= 160)
            self.napiswydaj.place_forget()
            self.btnwydaj2.place_forget()
            self.wydajentry.place_forget()
            self.szukajentry.insert(0, ' Wyszukaj...')
            self.szukajentry.config(state=DISABLED)
            self.szukajentry.bind("<ButtonRelease-1>", clickszukaj)
            self.napisustmail.place_forget()
            addressentry.place_forget()
            self.btnustmail.place_forget()
                   
        def onclick3():
            my_tree2.delete(*my_tree2.get_children())
            selection2()
            my_tree.place_forget()
            my_tree2.place(x = 210,y = 75)
            DodajFrame.place(x = 900,y = 75)
            self.btnwydaj1.place_forget()
            self.wydajentry.delete(first=0,last=100)
            self.wydajentry.focus_set()
            self.btnwydaj.configure(bg="#00bbaa")
            self.btnszukaj.configure(bg="#252643")
            self.btnhome.configure(bg="#252643")
            self.btnustawienia.configure(bg="#252643")
            self.szukajentry.place_forget()
            self.btndodaj.place_forget()
            self.wydajentry.place(x= 930,y= 210)
            self.napiswydaj.place(x = 980,y = 140)
            self.btnwydaj2.place(x = 1190,y = 210)
            self.napisustmail.place_forget()
            addressentry.place_forget()
            self.btnustmail.place_forget()
            
            sqconn = sqlite3.connect("DB1.db")
            sqcur = sqconn.cursor()
            sqcur.execute("SELECT DISTINCT numer, kol1, kol2 FROM sqtable")
            sqrows = sqcur.fetchall()

            for sqrow in sqrows:
                my_tree2.insert('', 'end', values=(sqrow[0],sqrow[1],sqrow[2]))
                
            
        def onclick4():
            self.odpdodaj = messagebox.askquestion("Dodaj nową paczkę", "Czy dodać nową paczkę?")
        
            if self.odpdodaj == 'yes':
                ring()
                self.odpdodaj.destroy()
                   
            else:
                self.odpdodaj.destroy()
            
    
        def onclick5():
            sqconn = sqlite3.connect("DB1.db")
            sqcur = sqconn.cursor()
            selected_item2 = my_tree2.selection()
            values = my_tree2.item(selected_item2, 'values')
                
            if len(my_tree2.selection()) > 0:
                self.odpwydaj = messagebox.askquestion("Wydaj przesyłkę", "Czy chcesz wydać zaznaczoną przesyłkę?")
                if self.odpwydaj == 'yes':
                    sqcur.execute("DELETE FROM sqtable WHERE numer=?", (my_tree2.set(selected_item2, '#1'),))
                    sqconn.commit()
                    my_tree2.delete(selected_item2)
                    self.wydajentry.delete(0, END)
                    sendmsg()
                    self.odpwydano = messagebox.showwarning("Wydałeś przesyłkę", "Potwierdzenie wydania przesłano na adres e-mail")
                    ring()
                else:
                    self.odpwydaj.destroy()
                         
            else:
                messagebox.showwarning("Zaznacz przesyłkę","Zaznacz przesyłkę do wydania!")
                
            sqconn.commit() 
            sqconn.close()
            
        def sendmsg():
            sender_email = "example@gmail.com"
            sender_password = pass

            server = smtplib.SMTP('smtp.gmail.com',587)
            server.starttls()
            server.login(sender_email,sender_password)

            print("Login successful")

            address_info = address.get()
            email_body_info = ("Wydano przesylke")
            server.sendmail(sender_email,address_info,email_body_info)
            print("Message sent")

        def zapiszmail():
            mails = open("maillist.txt", 'w')
            mlist = mails.write(addressentry.get())
            addressentry.insert(mlist, '')
            messagebox.showwarning("Adres e-mail", "Zmieniono adres do potwierdzeń e-mail")

        def onclicksettings():
            self.btnustawienia.configure(bg="#f0525f")
            self.btnwydaj.configure(bg="#252643")
            self.btnszukaj.configure(bg="#252643")
            self.btnhome.configure(bg="#252643")
            my_tree.place_forget()
            my_tree2.place_forget()
            DodajFrame.place_forget()
            self.btnwydaj1.place_forget()
            self.szukajentry.place_forget()
            self.btndodaj.place_forget()
            self.napiswydaj.place_forget()
            self.btnwydaj2.place_forget()
            self.wydajentry.place_forget()
            self.napisustmail.place(x = 297,y = 100)
            addressentry.place(x=300,y=140)
            self.btnustmail.place(x = 440,y = 210)
   
                  
        def searchnow():
    
            msconn = pyodbc.connect("DRIVER={ODBC Driver 13 for SQL Server};" "SERVER=DESKTOP\SQLEXPRESS;" "DATABASE=pyapp;" "UID=sa;" "PWD="sqlpass";")
            mscur = msconn.cursor()

            searched = self.szukajentry.get()
            query = "SELECT DISTINCT numer, kol1, kol2 FROM dbo.Table1 WHERE numer = '"+searched+"'"
            mscur.execute(query)
            rows = mscur.fetchall()

            for row in rows:
                my_tree.insert('', 'end', values=(row[0],row[1],row[2]))

            self.szukajentry.delete(0, 'end')


        def wydajpaczke():
            
            selected = my_tree.selection()
            values = my_tree.item(selected, 'values')
            
            if len(my_tree.selection()) > 0:
                #grab record number
                #grab record values
                self.odpdowydania = messagebox.askquestion("Przyjmij przesyłkę", "Czy chcesz przyjąć zaznaczoną paczkę?")
                if self.odpdowydania == 'yes':
                    sqconn = sqlite3.connect("DB1.db")
                    sqcur = sqconn.cursor()
                    sqcur.execute("INSERT INTO sqtable VALUES (?,?,?)", (values[0],values[1],values[2]))
                    sqconn.commit()
                    my_tree.delete(selected)
                    ring()
                else:
                    self.odpdowydania.destroy()             
            else:
                messagebox.showwarning("Zaznacz przesyłkę","Zaznacz przesyłkę do przyjęcia!")
               
        
        def selection():
            if len(my_tree.selection()) > 0:
                my_tree.selection_remove(my_tree.selection())
         
                
        def selection2():
            if len(my_tree2.selection()) > 0:
                my_tree2.selection_remove(my_tree2.selection())
                
        def bindtoentry():
            self.wydajentry.delete(0, END)
            bind = my_tree2.focus()
            values = my_tree2.item(bind, 'values')
            self.wydajentry.insert(0, values[0])
        
        def clicker(e):
            bindtoentry()  


        address = StringVar()
      
        MainFrame = Frame(self.root, bg="#f5f5f7")
        MainFrame.grid()
        
        ButtonFrame = Frame(MainFrame, bd=0, width=152, height=1350, padx=1, pady=10, bg="#252643", relief=FLAT)
        ButtonFrame.pack(side=LEFT)
        
        DodajFrame = Frame(self.root, bd=0, width=355, height=547, padx=18, pady=0, bg="#949494", relief=FLAT)
        
        self.napiswydaj = Label(self.root, text="Wydaj przesyłkę", bg='#949494', font=("Iosevka", 20), fg='#f5f5f7')

        self.napisustmail = Label(self.root, text="Potwierdzenie e-mail", bg='#f5f5f7', font=("Iosevka", 16), fg='#252643')
 
        self.szukajentry = Entry(self.root, width=16, bg="#fafafa", fg="#313131", insertborderwidth=0, relief="flat", selectbackground="#fc6200", font=('Helvetica', 24), insertbackground="#fc6200")
        self.wydajentry = Entry(self.root, width=14, bg="#fafafa", fg="#313131", insertborderwidth=0, relief="flat", selectbackground="#fc6200", font=('Helvetica', 24), insertbackground="#fc6200")

        addressentry = Entry(textvariable=address, width=23, bg="#fafafa", fg="#696969", insertborderwidth=0, relief="groove", selectbackground="#fc6200", font=('Iosevka', 14), insertbackground="#fc6200")
        
        #photos
        self.photo1 = PhotoImage(file = "homek.png") 
        self.photo2 = PhotoImage(file = "box.png") 
        self.photo3 = PhotoImage(file = "box2.png")
        self.photo4 = PhotoImage(file = "btnhistory.png")
        self.photo5 = PhotoImage(file = "btnsettings.png")
        self.photo6 = PhotoImage(file = "searchbutton.png")
          
        #menu buttons
        self.btnhome = Button(ButtonFrame, command=onclick1, text="     Home", fg="white", font = ('Iosevka','11'), relief='flat', width=146, height=70, image=self.photo1, bg="#252643", activebackground="#1a7d74", borderwidth=0, compound=LEFT)
        self.btnhome.place(x = 1,y = 50)
        self.btnhome.configure(bg="#00bbaa")
        self.btnszukaj = Button(ButtonFrame, command=onclick2, text="    Przyjmij", fg="white", font = ('Iosevka','11'), relief='flat', width=146, height=70, image=self.photo2, bg="#252643", activebackground="#1a7d74", borderwidth=0, compound=LEFT)
        self.btnszukaj.place(x = 1,y = 125)
        self.btnwydaj = Button(ButtonFrame, command=onclick3, text="     Wydaj", fg="white", font = ('Iosevka','11'), relief='flat', width=146, height=70, image=self.photo3, padx=2, bg="#252643", activebackground="#1a7d74", borderwidth=0, compound=LEFT)
        self.btnwydaj.place(x = 1,y = 200)
        self.btnhistoria = Button(ButtonFrame, text="Historia\n  przesyłek", fg="white", font = ('Iosevka','11'), relief='flat', width=146, height=70, image=self.photo4, padx=5, bg="#252643", activebackground="#1a7d74", borderwidth=0, compound=LEFT)
        self.btnhistoria.place(x = 1,y = 275)
        self.btnustawienia = Button(ButtonFrame, command=onclicksettings,text=" ", fg="white", font = ('Iosevka','11'), relief='flat', width=146, height=35, image=self.photo5, padx=5, bg="#252643", activebackground="#ba2d44", borderwidth=0, compound=LEFT)
        self.btnustawienia.place(x = 1,y = 580)
        #funcbuttons
        self.btndodaj = Button(self.root, command=searchnow, relief='flat', image=self.photo6, borderwidth=0, highlightbackground="#000000", highlightthickness=0)
        self.btnwydaj1 = Button(self.root, command=wydajpaczke, text="Przyjmij", fg="white", font = ('Iosevka','10'), relief='flat', width=7, height=2, bg="#f4a52e", activebackground="#e35c07", borderwidth=0, compound=LEFT)
        self.btnwydaj2 = Button(self.root, command=onclick5, text="-", fg="white", font = ('Iosevka','10','bold'), relief='flat', width=5, height=2, bg="#f4a52e", activebackground="#e35c07", borderwidth=0, compound=LEFT)
        self.btnustmail = Button(self.root, command=zapiszmail, text="Zapisz", fg="white", font = ('Iosevka','10'), relief='flat', width=7, height=2, bg="#f4a52e", activebackground="#e35c07", borderwidth=0, compound=LEFT)

        mails = open("maillist.txt", 'r')
        mlist = mails.read()
        mails.close()
        addressentry.insert(END, mlist)
        
        #TREEVIEW
        #tree1     
        my_tree = ttk.Treeview(self.root)
        my_tree['columns'] = ("Klient", "Zlecenie", "Status")
        style = ttk.Style()
        style.configure("Treeview.Heading", foreground='#949494', fieldbackground="#FAFAFA", font=('Iosevka', 14))
        style.configure("Treeview", rowheight=52, font=('Iosevka', 13))
        style.map('Treeview', background=[('selected', '#949494')])

        my_tree.column("#0", width=0, stretch=FALSE)
        my_tree.column("Klient", minwidth=230, anchor=CENTER, width=230)
        my_tree.column("Zlecenie", minwidth=230, anchor=CENTER, width=230)
        my_tree.column("Status", minwidth=230, anchor=CENTER, width=230)

        my_tree.heading("#0", text="", anchor=W)
        my_tree.heading("Klient", text="Klient", anchor=CENTER)
        my_tree.heading("Zlecenie", text="Zlecenie", anchor=CENTER)
        my_tree.heading("Status", text="Status", anchor=CENTER)

        #tree2
        my_tree2 = ttk.Treeview(self.root)
        my_tree2['columns'] = ("Klient", "Zlecenie", "Status")
        style = ttk.Style()
        style.configure("Treeview.Heading", foreground='#949494', fieldbackground="#FAFAFA", font=('Iosevka', 14))
        style.configure("Treeview", rowheight=52, font=('Iosevka', 13))
        style.map('Treeview', background=[('selected', '#949494')])

        my_tree2.column("#0", width=0, stretch=FALSE)
        my_tree2.column("Klient", minwidth=230, anchor=CENTER, width=230)
        my_tree2.column("Zlecenie", minwidth=230, anchor=CENTER, width=230)
        my_tree2.column("Status", minwidth=230, anchor=CENTER, width=230)

        my_tree2.heading("#0", text="", anchor=W)
        my_tree2.heading("Klient", text="Klient", anchor=CENTER)
        my_tree2.heading("Zlecenie", text="Zlecenie", anchor=CENTER)
        my_tree2.heading("Status", text="Status", anchor=CENTER)
        #bindings
        my_tree2.bind("<ButtonRelease-1>", clicker)
        
                
                             
     
if __name__=='__main__':
    root = Tk()
    application = App(root)
    root.mainloop()
    