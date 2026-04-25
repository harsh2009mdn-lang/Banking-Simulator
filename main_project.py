from tkinter import Tk,Label,Frame,Entry,Button,simpledialog,messagebox
from tkinter.ttk import Combobox        #combox is genrally used for dropdown list
import time
import generator                        #we import this module to create the captcha code
import table                            #we make table for db and import it
import sqlite3
table.create_table()
import mailing
from PIL import Image,ImageTk

#it is used to update date & time in every 1000 ms(1s)
def update_time():
    datetime=time.strftime("%d-%b-%Y⏰%r")
    dt_lbl.configure(text=datetime)
    dt_lbl.after(1000,update_time)

#it is used to create the new frame to forgot the pass.
def forgot_screen():
    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="#eecfe1")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.75)
    
    def back():
        frm.destroy()                 #destroy() method is used to destroy the running screen
        main_screen()
    
    def send_forgot_otp():
        acn=acn_entry.get()
        email=email_entry.get()

        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query='select name,pass from accounts where acn=? and email=?'
        curobj.execute(query,(acn,email))
        tup=curobj.fetchone()
        conobj.close()

        if tup!=None:
         otp=generator.forgot_otp()
         text=f'''Hello {tup[0]},
OTP to recover password is = {otp}
'''
         mailing.forgototp_mail(email,text)
         messagebox.showinfo('forgot','OTP sent to registered email')
         attempts=1
         while attempts<=3:
            attempts+=1
            uotp=simpledialog.askinteger('forgot','otp')
            if otp==uotp:
                messagebox.showinfo('Password',tup[1])
                break
            else:
                messagebox.showerror('forgot','Invalid OTP, try again')

        else:
            messagebox.showerror('forgot','Invalid Details')


    back_btn=Button(frm,text='Back',font=('arial',15,'bold'),bg='#e5e7eb',bd=5,command=back)
    back_btn.pack(side='bottom')

    acn_label=Label(frm,text="Account no.",font=('arial',20,'bold'),bg='#e5e7eb')
    acn_label.place(relx=.25,rely=.2)

    acn_entry=Entry(frm,font=('arial',16,'bold'),bd=5)
    acn_entry.place(relx=.4,rely=.2)

    email_label=Label(frm,text="Email",font=('arial',20,'bold'),bg='#e5e7eb')
    email_label.place(relx=.3,rely=.3)

    email_entry=Entry(frm,font=('arial',16,'bold'),bd=5)
    email_entry.place(relx=.4,rely=.3)

    otp_btn=Button(frm,text='OTP',font=('arial',15,'bold'),bg='#e5e7eb',bd=5,command=send_forgot_otp)
    otp_btn.place(relx=.46,rely=.4)

#we create screen for customer
def customer_screen(uacn):
    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="#eecfe1")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.75)

    def logout():
        frm.destroy()
        main_screen()
    
    def show():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.18,rely=.1,relwidth=.6,relheight=.8)

        title_lbl=Label(ifrm,text="Show Detail Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title_lbl.pack(pady=15)

        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query='select * from accounts where acn=?'
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        Label(ifrm, text=f"Account No : {tup[0]}", font=('italic',18), bg='white').pack(anchor='w',pady=(20,5))

        Label(ifrm, text=f"Open Date  : {tup[7]}", font=('italic',18), bg='white').pack(anchor='w',pady=(20,5))

        Label(ifrm, text=f"Adhar No   : {tup[5]}", font=('italic',18), bg='white').pack(anchor='w',pady=(20,5))

        Label(ifrm, text=f"Mobile No  : {tup[4]}", font=('italic',18), bg='white').pack(anchor='w',pady=(20,5))

        Label(ifrm, text=f"Balance    : {tup[3]}", font=('italic',18), bg='white').pack(anchor='w',pady=(20,5))

    def edit():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.18,rely=.1,relwidth=.6,relheight=.8)

        def update():
            name=name_entry.get()
            pwd=pass_entry.get()
            if pwd == "":
                conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
                curobj=conobj.cursor()
                curobj.execute("select pass from accounts where acn=?", (uacn,))
                pwd = curobj.fetchone()[0]
                conobj.close()
            mob=mob_entry.get()
            email=email_entry.get()
            conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
            curobj=conobj.cursor()
            query="update accounts set name=?,pass=?,mob=?,email=? where acn=?"
            curobj.execute(query,(name,pwd,mob,email,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Update','Details Updated')



        title_lbl=Label(ifrm,text="Edit Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title_lbl.pack()

        #adding label and entry in edit frame
        name_label=Label(ifrm,text="Name",font=('arial',15,'bold')
                    ,bg="white")
        name_label.place(relx=.1,rely=.1)

        name_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        name_entry.place(relx=.1,rely=.17)
        name_entry.focus()

        email_label=Label(ifrm,text="Email",font=('arial',15,'bold')
                    ,bg="white")
        email_label.place(relx=.6,rely=.1)

        email_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        email_entry.place(relx=.6,rely=.17)

        mob_label=Label(ifrm,text="Mobile Number",font=('arial',15,'bold')
                    ,bg="white")
        mob_label.place(relx=.1,rely=.3)

        mob_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        mob_entry.place(relx=.1,rely=.37)

        pass_label=Label(ifrm,text="Password",font=('arial',15,'bold')
                    ,bg="white")
        pass_label.place(relx=.6,rely=.3)
        pass_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        pass_entry.place(relx=.6,rely=.37)
        
        update_btn=Button(ifrm,text="Update Details",font=("Arial",18,"bold"),
                      bg='green',bd=5,fg='white',width=12,command=update)
        update_btn.place(relx=.39,rely=.6)

        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query='select name,mob,email,"pass" from accounts where acn=?'
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        if tup:
            name_entry.insert(0,tup[0])
            mob_entry.insert(0,tup[1])
            email_entry.insert(0,tup[2])
            pass_entry.insert(0,tup[3])
        else:
            messagebox.showerror("Error","Account data not found")

    #creating functions for customer screen buttons
    def deposit():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.18,rely=.1,relwidth=.6,relheight=.8)

        title_lbl=Label(ifrm,text="Deposit Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title_lbl.pack()

        uamt=simpledialog.askfloat('Deposit','Amount')
        if uamt is None:
            return
        if uamt<=0:
            messagebox.showerror('Error','Invalid Amount')

        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query='update accounts set bal=bal+? where acn=?'
        curobj.execute(query,(uamt,uacn))
        conobj.commit()
        conobj.close()
        messagebox.showinfo('Deposit',f"{uamt} deposited")


    def withdraw():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.18,rely=.1,relwidth=.6,relheight=.8)

        title_lbl=Label(ifrm,text="Withdraw Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title_lbl.pack()

        uamt=simpledialog.askfloat('Withdraw','Amount')
        
        #we connect it to db to withdraw amt from back 
        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query='select bal from accounts where acn=?'
        curobj.execute(query,(uacn,))
        bal=curobj.fetchone()[0]
        conobj.close()

        if bal>=uamt:
            conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
            curobj=conobj.cursor()
            query='update accounts set bal=bal-? where acn=?'
            curobj.execute(query,(uamt,uacn))
            conobj.commit()
            conobj.close()
            messagebox.showinfo('Withdraw',f"{uamt} withdrawn")

        else:
            messagebox.showerror('Withdraw',"Insufficent Balance")
        
    def transfer():
        ifrm=Frame(frm,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.18,rely=.1,relwidth=.6,relheight=.8)

        title_lbl=Label(ifrm,text="Transfer Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title_lbl.pack()

        toacn=simpledialog.askinteger('Transfer','To Acc')
        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query='select * from accounts where acn=?'
        curobj.execute(query,(toacn,))
        tup=curobj.fetchone()
        conobj.close()

        if tup!=None:
            uamt=simpledialog.askinteger('Transfer','Amount')

            conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
            curobj=conobj.cursor()
            query='select bal from accounts where acn=?'
            curobj.execute(query,(uacn,))
            bal=curobj.fetchone()[0]
            conobj.close()

            if bal>=uamt:
                conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
                curobj=conobj.cursor()
                query1='update accounts set bal=bal-? where acn=?'
                query2='update accounts set bal=bal+? where acn=?'

                curobj.execute(query1,(uamt,uacn))
                curobj.execute(query2,(uamt,toacn))

                conobj.commit()
                conobj.close()
                messagebox.showinfo('Transfer',f"{uamt} transferred to {toacn}")
            else:
                messagebox.showerror('Withdraw',"Insufficent Balance")

        else:
            messagebox.showerror('Transfer','Invalid to ACN')

    #we create both welcome label and logout button
    conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
    curobj=conobj.cursor()
    query='select name from accounts where acn=?'
    curobj.execute(query,(uacn,))
    name=curobj.fetchone()[0]
    conobj.close()

    wel_lbl=Label(frm,text=f"Welcome {name}🙏",font=("italic",15,"bold"),
                        bg='#eecfe1',fg="#000000")
    wel_lbl.place(relx=0,rely=0)

    logout_btn=Button(frm,text='↩️',font=('arial',18,'bold'),command=logout,bd=4)
    logout_btn.place(relx=.02,rely=.9)

    show_btn=Button(frm,text='Show Details',font=('arial',18,'bold'),
                    bd=4,width=12,command=show)
    show_btn.place(relx=.001,rely=.1)

    edit_btn=Button(frm,text='Edit Details',font=('arial',18,'bold'),
                    bd=4,width=12,command=edit)
    edit_btn.place(relx=.001,rely=.25)

    deposit_btn=Button(frm,text='Deposit',font=('arial',18,'bold'),
                       bg='green',fg='white',bd=4,width=12,command=deposit)
    deposit_btn.place(relx=.001,rely=.4)

    withdraw_btn=Button(frm,text='Withdraw',font=('arial',18,'bold'),
                       bg='red',fg='white',bd=4,width=12,command=withdraw)
    withdraw_btn.place(relx=.001,rely=.55)

    transfer_btn=Button(frm,text='Transfer',font=('arial',18,'bold'),
                       bg="#e3f63b",fg='white',bd=4,width=12,command=transfer)
    transfer_btn.place(relx=.001,rely=.7)


#we create the screen for admin
def admin_screen():
    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="#eecfe1")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.75)

    def logout():
        frm.destroy()
        main_screen()

    #we create both welcome label and logout button
    wel_lbl=Label(frm,text="Welcome Admin 🙏",font=("italic",15,"bold"),
                        bg='#eecfe1',fg="#000000")
    wel_lbl.place(relx=0,rely=0)

    logout_btn=Button(frm,text='↩️',font=('arial',18,'bold'),command=logout,bd=4)
    logout_btn.place(relx=.02,rely=.9)

    #it used to create a new frame inside the main frame
    def new():
        ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.1,rely=.3,relwidth=.8,relheight=.5)

        def open_ac():
            print('open')
            name=name_entry.get()
            email=email_entry.get()
            mob=mob_entry.get()
            adhar=adhar_entry.get()
            bal=0
            opendate=time.strftime('%d-%b-%Y %r')
            pwd=generator.password()

            #use to connect it to sqlite db
            conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
            curobj=conobj.cursor()
            query="insert into accounts values(null,?,?,?,?,?,?,?)"
            curobj.execute(query,(name,pwd,bal,mob,adhar,email,opendate))
            conobj.commit()
            conobj.close()

            #now we connect sqllite to fetch bank acc
            conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
            curobj=conobj.cursor()
            query='select max(acn) from accounts'
            curobj.execute(query)
            acn=curobj.fetchone()[0]
            conobj.close()

            text=f'''Welcome {name},
We have successfully opened your account in ABC Bank
This is your Credentials
ACN={acn}
Pass={pwd}
'''

            mailing.openacn_mail(email,text)

            messagebox.showinfo('Account Opened','We have opened your account at mailed credential')

        #we create label and entry of title,name,email,monile no.,adhar no. and open btn on frm insde new button
        title1_lbl=Label(ifrm,text="New Account Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title1_lbl.pack()

        name_label=Label(ifrm,text="Name",font=('arial',15,'bold')
                    ,bg="white")
        name_label.place(relx=.1,rely=.1)

        name_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        name_entry.place(relx=.1,rely=.17)
        name_entry.focus()

        email_label=Label(ifrm,text="Email",font=('arial',15,'bold')
                    ,bg="white")
        email_label.place(relx=.6,rely=.1)

        email_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        email_entry.place(relx=.6,rely=.17)

        mob_label=Label(ifrm,text="Mobile Number",font=('arial',15,'bold')
                    ,bg="white")
        mob_label.place(relx=.1,rely=.3)

        mob_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        mob_entry.place(relx=.1,rely=.37)

        adhar_label=Label(ifrm,text="Adhar no.",font=('arial',15,'bold')
                    ,bg="white")
        adhar_label.place(relx=.6,rely=.3)

        adhar_entry=Entry(ifrm,font=('arial',20,'bold'),bd=5)
        adhar_entry.place(relx=.6,rely=.37)
        
        open_btn=Button(ifrm,text="Open Account",font=("Arial",18,"bold"),
                      bg='green',bd=5,fg='white',width=12,command=open_ac)
        open_btn.place(relx=.39,rely=.6)

       
    def view():
        ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.1,rely=.3,relwidth=.8,relheight=.5)

        title1_lbl=Label(ifrm,text="View Account Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title1_lbl.pack()

        #simpledialog is used to created dialog box inside the frame which already contain both title,lalbel & button.
        
        uacn=simpledialog.askinteger('View Account',"Enter Account no.")   
        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query='select * from accounts where acn=?'
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()
        if tup!=None:
                messagebox.showinfo('Details',tup)
        else:
                messagebox.showerror("Details","Account doesn't exists")
    
    def close():
        ifrm=Frame(root,highlightbackground="black",highlightthickness=2)
        ifrm.configure(bg="#fcfcfc")
        ifrm.place(relx=.1,rely=.3,relwidth=.8,relheight=.5)

        title1_lbl=Label(ifrm,text="Close Account Screen",font=("italic",20,"bold"),
                        bg='white',fg="#837bd7")
        title1_lbl.pack()
        uacn=simpledialog.askinteger('Close Account',"Enter Account no.")   
        conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
        curobj=conobj.cursor()
        query="select name,email from accounts where acn=?"
        curobj.execute(query,(uacn,))
        tup=curobj.fetchone()
        conobj.close()

        #we make a code to sent otp to acc holder to close the acc

        if tup!=None:
            otp=generator.close_otp()
            text=f"Hello {tup[0]}\nOTP to close your account : {otp}"
            mailing.closeotp_mail(tup[1],text)
            messagebox.showinfo('Close','We have sent otp to close account')
            uotp=simpledialog.askinteger('Close OTP','OTP')
            if otp==uotp:
                conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
                curobj=conobj.cursor()
                query='delete from accounts where acn=?'
                curobj.execute(query,(uacn,))
                conobj.commit()
                conobj.close()
                messagebox.showinfo('Close','Account Closed')

            else:
                messagebox.showerror("Close Account","Invalid OTP")

        else:
            messagebox.showerror('Close',"Account doesn't exists")

    #here button is created for new acc,view acc and close acc.
    newacn_btn=Button(frm,text="New Account",font=("Arial",18,"bold"),
                      bg='green',bd=5,fg='white',width=12,command=new)
    newacn_btn.place(relx=.13,rely=.05)

    viewacn_btn=Button(frm,text="View Account",font=("Arial",18,"bold"),
                       bg='powder blue',bd=5,fg='black',width=12,command=view)
    viewacn_btn.place(relx=.44,rely=.05)

    closeacn_btn=Button(frm,text="Close Account",font=("Arial",18,"bold"),
                        bg='red',bd=5,fg='white',width=12,command=close)
    closeacn_btn.place(relx=.75,rely=.05)

#here we make a function for main screen 
def main_screen():
    def refresh():
        global gen_cap
        gen_cap=generator.captcha()
        cap_label.configure(text=gen_cap)

    def forgot():
        frm.destroy()
        forgot_screen()
    
    def login():
        utype=user_combo.get()
        ucap=cap_entry.get()

        global gen_cap
        gen_cap=gen_cap.replace(" ","")
        if ucap!=gen_cap:
            messagebox.showerror('login','Invalid Captcha')
            return
        
        if utype=='Admin':
            uacn=int(acn_entry.get())
            upass=pass_entry.get()
            if uacn==0 and upass=="admin":
               frm.destroy()
               admin_screen()
            else:
                messagebox.showerror("Login",'Invalid Credentials')

        elif utype=='Customer':
            uacn=int(acn_entry.get())
            upass=pass_entry.get()
            conobj=sqlite3.connect(r'D:\ducat_python_programms\bank.sqlite')
            curobj=conobj.cursor()
            query="select * from accounts where acn=? and pass=?"
            curobj.execute(query,(uacn,upass))
            tup=curobj.fetchone()
            if tup!=None:
                    frm.destroy()
                    customer_screen(uacn)
            else:
                messagebox.showerror("Login",'Invalid Credentials')
        else:
           messagebox.showerror("Login",'Please select user type')
    
       

    def reset():
        user_combo.current(0)
        acn_entry.delete(0,'end')
        pass_entry.delete(0,'end')
        cap_entry.delete(0,'end')

        user_combo.focus()

        
#here we create frame,which contain label,entry and combobox
    frm=Frame(root,highlightbackground="black",highlightthickness=2)
    frm.configure(bg="#eecfe1")
    frm.place(relx=0,rely=.15,relwidth=1,relheight=.75)

    user_label=Label(frm,text="User",font=('arial',20,'bold'),bg='#eecfe1')
    user_label.place(relx=.3,rely=.095)
    
    user_combo=Combobox(frm,values=['---Select---','Admin','Customer'],
                        font=('arial',15,'bold'))
    user_combo.place(relx=.4,rely=.1)
    user_combo.current(0)
    
    acn_label=Label(frm,text="Account no.",font=('arial',20,'bold')
                    ,bg='#eecfe1')
    acn_label.place(relx=.28,rely=.2)

    acn_entry=Entry(frm,font=('arial',16,'bold'),bd=5)
    acn_entry.place(relx=.4,rely=.2)
    acn_entry.focus()

    pass_label=Label(frm,text="Password",font=('arial',20,'bold'),
                     bg='#eecfe1')
    pass_label.place(relx=.29,rely=.3)

    pass_entry=Entry(frm,font=('arial',16,'bold'),bd=5,show='*')
    pass_entry.place(relx=.4,rely=.3)
    
    global gen_cap
    gen_cap=generator.captcha()
    cap_label=Label(frm,text=gen_cap,font=('Special Elite',20,'bold'),
                    width=8)
    cap_label.place(relx=.43,rely=.4)

    cap_entry=Entry(frm,font=('arial',16,'bold'),bd=5)
    cap_entry.place(relx=.4,rely=.5)

    ref_btn=Button(frm,text='🔄',font=('arial',15,'bold'),command=refresh,bd=5)
    ref_btn.place(relx=.55,rely=.4)

    login_btn=Button(frm,text='login',font=('arial',15,'bold'),
                     bg='#e5e7eb',bd=5,command=login)
    login_btn.place(relx=.42,rely=.6)

    reset_btn=Button(frm,text='Reset',font=('arial',15,'bold'),bg='#e5e7eb',
                     bd=5,command=reset)
    reset_btn.place(relx=.5,rely=.6)

    forget_btn=Button(frm,text='forgot Password',font=('arial',15,'bold'),
                      bg='#e5e7eb',bd=5,command=forgot)
    forget_btn.place(relx=.43,rely=.75)

#from here project is start
root=Tk()
root.state("zoomed")
root.configure(bg="#e5e7eb")

title_lbl=Label(root,text="ABC BANK",font=("arial",42,"bold",'underline'),
                bg="#e5e7eb")
title_lbl.pack()

datetime=time.strftime("%d-%b-%Y %r")

dt_lbl=Label(root,text=datetime,font=("arial",18,"bold",),bg="#e5e7eb",fg="blue")
dt_lbl.pack()
update_time()

img=Image.open("logo.png").resize((200,150))
tkimg=ImageTk.PhotoImage(img,master=root)

logo_lbl=Label(root,image=tkimg)
logo_lbl.place(relx=0,rely=0)

footer_lbl=Label(root,text="Harshit\n📞: 7906117754",
                 font=("arial",18,"bold"),bg="#e5e7eb")
footer_lbl.pack(side='bottom',pady=10)

main_screen()
root.mainloop()