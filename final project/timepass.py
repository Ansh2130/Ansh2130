from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import Login_PAGE

def login():
    win = Tk()
    win.title('Pharmacy Management System')
    win.state('zoomed')
    win.config(bg='black')

    #=================================Button function=================================
    #=================================Sales Button function=================================
    def sales():
        if e16.get() == "" or e17.get() == "" or e18.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            con = mysql.connector.connect(host="localhost", username="root", password="itsok1234", database="mydata")
            my_cursor = con.cursor()
            int_cmd = (
                "INSERT INTO saless (`Product Name`, `Quantity`, `Total Price`, `Sale Date`)"
                "values(%s,%s,%s,%s)"
            )

            salesdata = (
                product_name.get(),
                quantity.get(),
                total_price.get(),
                sale_date.get(),
            )

            my_cursor.execute(int_cmd, salesdata)
            con.commit()
            fetch_salesdata()
            con.close()

            messagebox.showinfo("Success", "Record has been inserted")

    def fetch_salesdata():
        con = mysql.connector.connect(host="localhost", username="root", password="itsok1234", database="mydata")
        my_cursor = con.cursor()
        my_cursor.execute('select * from saless')
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            sales_table.delete(*sales_table.get_children())
            for items in rows:
                sales_table.insert('', END, values=items)
            con.commit()
        con.close()

    def get_salesdata(event=''):
        cursor_row = sales_table.focus()
        data = sales_table.item(cursor_row)
        row = data['values']
        product_name.set(row[0])
        quantity.set(row[1])
        total_price.set(row[2])
        sale_date.set(row[3])
#=========================================perscription data button fxn==============================
    def pd():
        if e1.get()=="" or e2.get()=="":
            messagebox.showerror("Error","All fields are requireds")
        else:
            con=mysql.connector.connect(host="localhost",username="root",password="itsok1234",database="mydata")
            my_cursor=con.cursor()
            int_cmd = (
                "INSERT INTO hospital (`Name of Tablets`, `Reference`, `Dose`, `No. of tablets`, `Issue date`, `Exp. Date`, `Daily Dose`, `Side Effect`, `Patient Name`, `DOB`, `Patient Address`)"
                "values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            )
            
            data = (
                nameoftablets.get(),
                ref.get(),
                dose.get(),
                nooftablets.get(),
                issuedate.get(),
                expdate.get(),
                dailydose.get(),
                sideeffect.get(),
                nameofpatient.get(),
                dob.get(),
                patientaddress.get()
            )


            my_cursor.execute(int_cmd, data)
            con.commit()
            fetch_data()
            con.close()
            
            messagebox.showinfo("Success","Record has been inserted") 
    def fetch_data():
        con=mysql.connector.connect(host="localhost",username="root",password="itsok1234",database="mydata")
        my_cursor=con.cursor()
        my_cursor.execute('select * from hospital')
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            table.delete(* table.get_children())
            for items in rows:
                table.insert('',END,values=items)
            con.commit()
        con.close()
    def get_data(event=''):
        cursor_row=table.focus()
        data=table.item(cursor_row)
        row=data['values']
        nameoftablets.set(row[0])
        ref.set(row[1])
        dose.set(row[2])
        nooftablets.set(row[3])
        issuedate.set(row[4])
        expdate.set(row[5]) 
        dailydose.set(row[6])
        sideeffect.set(row[7])
        nameofpatient.set(row[8])
        dob.set(row[9])
        patientaddress.set(row[10])   
    #==========================================Prescription Data=================
    def pre():
        txt_frme.insert(END,'Name of Tablets:\t\t\t'+nameoftablets.get()+'\n')
        txt_frme.insert(END,'Reference No:\t\t\t'+ref.get()+'\n')
        txt_frme.insert(END,'Dose:\t\t\t'+dose.get()+'\n')
        txt_frme.insert(END,'No of Tablets:\t\t\t'+nooftablets.get()+'\n') 
        txt_frme.insert(END,'Issue date:\t\t\t'+issuedate.get()+'\n')
        txt_frme.insert(END,'Exp. date:\t\t\t'+expdate.get()+'\n') 
        txt_frme.insert(END,'Daily Dose:\t\t\t'+dailydose.get()+'\n')
        txt_frme.insert(END,'Side effect:\t\t\t'+sideeffect.get()+'\n')
        txt_frme.insert(END,'Blood Pressure:\t\t\t'+nameoftablets.get()+'\n')
        txt_frme.insert(END,'Storage Device:\t\t\t'+nameoftablets.get()+'\n')
        txt_frme.insert(END,'Medication:\t\t\t'+medication.get()+'\n')
        txt_frme.insert(END,'Patient Id:\t\t\t'+patientid.get()+'\n')
        txt_frme.insert(END,'Name of Patient:\t\t\t'+nameofpatient.get()+'\n')
        txt_frme.insert(END,'DOB:\t\t\t'+dob.get()+'\n')
        txt_frme.insert(END,'Patient Address:\t\t\t'+patientaddress.get()+'\n')
    #===========================DELETE BUTTON===================================
    def delete():
        con= con=mysql.connector.connect(host="localhost",username="root",password="itsok1234",database="mydata")
        my_cursor=con.cursor() 
        querry=('delete from hospital where Reference=%s')
        value=(ref.get(),)
        my_cursor.execute(querry,value)
        con.commit()
        con.close()
        fetch_data()  
        messagebox.showinfo('Deleted','Patient data has been deleted')
    #============================Clear Button==============================
    def clear():
        nooftablets.set('')
        ref.set('')
        dose.set('')
        issuedate.set('')
        expdate.set('')
        dailydose.set('')
        sideeffect.set('')
        bloodpressure.set('')
        storage.set('')
        medication.set('')
        patientid.set('')
        nameofpatient.set('')
        dob.set('')
        patientaddress.set('')
        txt_frme.delete(1.0,END)   
        product_name.set('')
            
    #=============================================Exit button========================
    def exit():
        confirm=messagebox.askyesno('conformation','Are you sure you want to Exit')
        if confirm>0:
            win.destroy()
            return               
    #Heading
    Label(win,text='PHARMACY MANAGEMENT SYSTEM',font='impack 31 bold',bg='red',fg='white').pack(fill=X)
    #Frame1
    frame1=Frame(win,bd=15,relief=RIDGE)
    frame1.place(x=0,y=54,width=1750,height=310)
    #frame 3
    frame3=Frame(win,bd=15,relief=RIDGE)
    frame3.place(x=0,y=530,width=1553,height=175) 
    #Label frame for patient info
    lf1=LabelFrame(frame1,text='Patient Data',font='ariel 10 bold',bd=10,bg='cyan2')
    lf1.place(x=10,y=0,width=1400,height=280)
    #Labels for patient info
    Label(lf1,text='Name of tablets',bg='cyan2').place(x=5,y=10)
    Label(lf1,text='Reference No.',bg='cyan2').place(x=5,y=40)
    Label(lf1,text='Dose',bg='cyan2').place(x=5,y=70)
    Label(lf1,text='No of tablets',bg='cyan2').place(x=5,y=100)
    Label(lf1,text='Issue Date',bg='cyan2').place(x=5,y=130)
    Label(lf1,text='Exp. Date',bg='cyan2').place(x=5,y=160)
    Label(lf1,text='Daily dose',bg='cyan2').place(x=5,y=190)
    Label(lf1,text='Side Effect',bg='cyan2').place(x=5,y=220)
    Label(lf1,text='Blood pressure',bg='cyan2').place(x=370,y=10)
    Label(lf1,text='Storage Device',bg='cyan2').place(x=370,y=40)
    Label(lf1,text='Medication',bg='cyan2').place(x=370,y=70)
    Label(lf1,text='Patient Id',bg='cyan2').place(x=370,y=100)
    Label(lf1,text='Name of Patient',bg='cyan2').place(x=370,y=130)
    Label(lf1,text='DOB',bg='cyan2').place(x=370,y=160)
    Label(lf1,text='Patient Address',bg='cyan2').place(x=370,y=190)
    Label(lf1, text='Product Name', bg='cyan2').place(x=370, y=210)
    Label(lf1, text='Quantity', bg='cyan2').place(x=735, y=10)
    Label(lf1, text='Total Price', bg='cyan2').place(x=735, y=40)
    Label(lf1, text='Sale Date', bg='cyan2').place(x=735, y=70)
    #TextVariable for every field
    nameoftablets=StringVar()
    ref=StringVar()
    dose=StringVar()
    nooftablets=StringVar()
    issuedate=StringVar()
    expdate=StringVar()
    dailydose=StringVar()
    sideeffect=StringVar()
    bloodpressure=StringVar()
    storage=StringVar()
    medication=StringVar()
    patientid=StringVar()
    nameofpatient=StringVar()
    dob=StringVar()
    patientaddress=StringVar()
    product_name = StringVar()
    quantity = StringVar()
    total_price = StringVar()
    sale_date = StringVar()
    #Entry Field for all labels
    e1=Entry(lf1,bd=4,textvariable=nameoftablets)
    e1.place(x=130,y=10,width=200)
    e2=Entry(lf1,bd=4,textvariable=ref)
    e2.place(x=130,y=40,width=200)
    e3=Entry(lf1,bd=4,textvariable=dose)
    e3.place(x=130,y=70,width=200)
    e4=Entry(lf1,bd=4,textvariable=nooftablets)
    e4.place(x=130,y=100,width=200)
    e5=Entry(lf1,bd=4,textvariable=issuedate)
    e5.place(x=130,y=130,width=200)
    e6=Entry(lf1,bd=4,textvariable=expdate)
    e6.place(x=130,y=160,width=200)
    e7=Entry(lf1,bd=4,textvariable=dailydose)
    e7.place(x=130,y=190,width=200)
    e8=Entry(lf1,bd=4,textvariable=sideeffect)
    e8.place(x=130,y=220,width=200)
    e9=Entry(lf1,bd=4,textvariable=bloodpressure)
    e9.place(x=500,y=10,width=200)
    e10=Entry(lf1,bd=4,textvariable=storage)
    e10.place(x=500,y=40,width=200)
    e11=Entry(lf1,bd=4,textvariable=medication)
    e11.place(x=500,y=70,width=200)
    e12=Entry(lf1,bd=4,textvariable=patientid)
    e12.place(x=500,y=100,width=200)
    e13=Entry(lf1,bd=4,textvariable=nameofpatient)
    e13.place(x=500,y=130,width=200)
    e14=Entry(lf1,bd=4,textvariable=dob)
    e14.place(x=500,y=160,width=200)
    e15=Entry(lf1,bd=4,textvariable=patientaddress)
    e15.place(x=500,y=190,width=200)
    e16 = Entry(lf1, bd=4, textvariable=product_name)
    e16.place(x=500, y=210, width=200)
    e17 = Entry(lf1, bd=4, textvariable=quantity)
    e17.place(x=870, y=10, width=200)
    e18 = Entry(lf1, bd=4, textvariable=total_price)
    e18.place(x=870, y=40, width=200)
    e19 = Entry(lf1, bd=4, textvariable=sale_date)
    e19.place(x=870, y=70, width=200)

    #Label frame for Prescription
    lf2=LabelFrame(frame1,text='Prescription Receipt',font='ariel 12 bold',bd=10)
    lf2.place(x=1100,y=0,width=400,height=280)
    #Textbox for prescription
    txt_frme=Text(lf2,font='impack 10 bold',width=40,height=30,bg='medium spring green')
    txt_frme.pack(fill=BOTH)
    #frame2
    frame2=Frame(win,bd=15,relief=RIDGE)
    frame2.place(x=0,y=360,width=1553,height=180)
    #Button
    #Delete Button
    d_btn=Button(win,text='Eliminate',font='ariel 15 bold',bg='DarkOrchid1',fg='black',bd=6,cursor='hand2',command=delete)
    d_btn.place(x=0,y=700,width=280)
    #Perscription button
    p_btn=Button(win,text='Prescription',font='ariel 15 bold',bg='SeaGreen1',fg='black',bd=6,cursor='hand2',command=pre)
    p_btn.place(x=270,y=700,width=350)
    #Save Prescription Data
    pd_btn=Button(win,text='Record Prescription Data',font='ariel 15 bold',bg='SlateGray1',fg='black',bd=6,cursor='hand2',command=pd)
    pd_btn.place(x=600,y=700,width=350)
    #Clear button
    c_btn=Button(win,text='Remove',font='ariel 15 bold',bg='deep pink',fg='black',bd=6,cursor='hand2',command=clear)
    c_btn.place(x=940,y=700,width=200)
    #Exit button
    e_btn=Button(win,text='Exit',font='ariel 15 bold',bg='orange red',fg='black',bd=6,cursor='hand2',command=exit)
    e_btn.place(x=1140,y=700,width=200)
     #Button for Sales
    sales_btn = Button(win, text='Sales Data', font='ariel 15 bold', bg='misty rose', fg='black', bd=6, cursor='hand2', command=sales)
    sales_btn.place(x=1340, y=700, width=200)
    #Scrool bar for Prescription Data
    scroll_x=ttk.Scrollbar(frame2,orient=HORIZONTAL)
    scroll_x.pack(side='bottom',fill='x')
    scroll_y=ttk.Scrollbar(frame2,orient=VERTICAL)
    scroll_y.pack(side='right',fill='y')

    table=ttk.Treeview(frame2,columns=('not','ref','dose','nots','issd','expd','dd','sd','pn','dob','pa'),xscrollcommand=scroll_y.set,yscrollcommand=scroll_x.set)
    scroll_x=ttk.Scrollbar(command=table.xview)
    scroll_y=ttk.Scrollbar(command=table.yview)
     # Scrool bar for Sales Data
    sales_scroll_x = ttk.Scrollbar(frame3, orient=HORIZONTAL)
    sales_scroll_x.pack(side='bottom', fill='x')
    sales_scroll_y = ttk.Scrollbar(frame3, orient=VERTICAL)
    sales_scroll_y.pack(side='right', fill='y')

    sales_table = ttk.Treeview(frame3, columns=('prod', 'quant', 'price', 'date'), xscrollcommand=sales_scroll_y.set,
                               yscrollcommand=sales_scroll_x.set)
    sales_scroll_x = ttk.Scrollbar(command=sales_table.xview)
    sales_scroll_y = ttk.Scrollbar(command=sales_table.yview)
     # Heading for Sales data
    sales_table.heading('prod', text='Product Name')
    sales_table.heading('quant', text='Quantity')
    sales_table.heading('price', text='Total Price')
    sales_table.heading('date', text='Sale Date')
    sales_table['show'] = 'headings'
    sales_table.pack(fill=BOTH, expand=1)
    fetch_data()

    #Heading for prescription data
    table.heading('not',text='Name of Tablets')
    table.heading('ref',text='Reference No.')
    table.heading('dose',text='Dose')
    table.heading('nots',text='No of Tablets')
    table.heading('issd',text='Issue Date')
    table.heading('expd',text='Exp. Date')
    table.heading('dd',text='Daily Dose')
    table.heading('sd',text='Side Effect')
    table.heading('pn',text='Patient Name')
    table.heading('dob',text='DOB')
    table.heading('pa',text='Patient Address')
    table['show']='headings'
    table.pack(fill=BOTH,expand=1)
    #========================================
    table.column('not',width=100)
    table.column('ref',width=100)
    table.column('dose',width=100)
    table.column('nots',width=100)
    table.column('issd',width=100)
    table.column('expd',width=100)
    table.column('dd',width=100)
    table.column('sd',width=100)
    table.column('pn',width=100)
    table.column('dob',width=100)
    table.column('pa',width=100)
    table.bind('<ButtonRelease-1>',get_data)
    fetch_salesdata()
    fetch_data()
    

    mainloop()    