from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from datetime import datetime
from tkinter import messagebox



class room_booking:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        #variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_subtotal = StringVar()
        self.var_total = StringVar()

        #title
        lbl_title = Label(self.root, text = "BOOK YOUR ROOM", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        #logo
        img2 = Image.open(r"D:\College Project\Python\Hotel Management System\images\logo.png")
        img2 = img2.resize((100,40), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        #lable frame
        lableFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="ROOM DETAILS", padx=2, font=("times new roman", 12, "bold"))
        lableFrameLeft.place(x=5, y=50, width=425, height=490)

        #lables and entries
        #cust contact
        lbl_cust_contact = Label(lableFrameLeft,text="Customer Contact: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(lableFrameLeft, textvariable=self.var_contact, width=20, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        #fetch data
        btn_fetch_data = Button(lableFrameLeft, command=self.fetch_contact, text="Fetch Data", font=("arial", 10, "bold"), bg="black", fg="gold", width=8)
        btn_fetch_data.place(x=347, y=5)


        #check in date
        check_in_date = Label(lableFrameLeft, text="Check-in (dd/mm/yy): ", font=("arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        txtcheck_in_date = ttk.Entry(lableFrameLeft, textvariable=self.var_checkin, width=22, font=("arial", 13, "bold"))
        txtcheck_in_date.grid(row=1, column=1)
        
        #check out date
        check_out_date = Label(lableFrameLeft, text="Check-out (dd/mm/yy): ", font=("arial", 12, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)
        txtcheck_out_date = ttk.Entry(lableFrameLeft, textvariable=self.var_checkout, width=22, font=("arial", 13, "bold"))
        txtcheck_out_date.grid(row=2, column=1)

        #room type
        lbl_room_type = Label(lableFrameLeft, text="Room Type: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_type.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomtype from details")
        data = my_cursor.fetchall()

        combo_room_type = ttk.Combobox(lableFrameLeft, textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=22, state="readonly")
        combo_room_type["value"]=data
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)

        #Availabe room
        lbl_room_available = Label(lableFrameLeft, text="Available Room: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_available.grid(row=4, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select roomno from details")
        rows = my_cursor.fetchall()

        combo_room_available = ttk.Combobox(lableFrameLeft, textvariable=self.var_roomavailable, font=("arial", 12, "bold"), width=22, state="readonly")
        combo_room_available["value"]=rows
        combo_room_available.current(0)
        combo_room_available.grid(row=4, column=1)

        #Meal
        lbl_meal = Label(lableFrameLeft, text="Meal: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_meal.grid(row=5, column=0, sticky=W)
        combo_meal = ttk.Combobox(lableFrameLeft, textvariable=self.var_meal, font=("arial", 12, "bold"), width=22, state="readonly")
        combo_meal["value"]=("Breakfast", "Lunch", "Dinner", "All Meals")
        combo_meal.current(0)
        combo_meal.grid(row=5, column=1)

        #no of days
        lbl_no_of_days = Label(lableFrameLeft, text="Number of days: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_no_of_days.grid(row=6, column=0, sticky=W)
        txt_no_of_days = ttk.Entry(lableFrameLeft, textvariable=self.var_noofdays, width=22, font=("arial", 13, "bold"))
        txt_no_of_days.grid(row=6, column=1)

        #paid tax
        lbl_paid_tax = Label(lableFrameLeft, text="Paid Tax: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_paid_tax.grid(row=7, column=0, sticky=W)
        txt_paid_tax = ttk.Entry(lableFrameLeft, textvariable=self.var_paidtax, width=22, font=("arial", 13, "bold"))
        txt_paid_tax.grid(row=7, column=1)
        
        #subtotal
        lbl_sub_total = Label(lableFrameLeft, text="Sub Total: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_sub_total.grid(row=8, column=0, sticky=W)
        txt_sub_total = ttk.Entry(lableFrameLeft, textvariable=self.var_subtotal, width=22, font=("arial", 13, "bold"))
        txt_sub_total.grid(row=8, column=1)

        #total cost
        lbl_total_cost = Label(lableFrameLeft, text="Total Cost: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_total_cost.grid(row=9, column=0, sticky=W)
        txt_total_cost = ttk.Entry(lableFrameLeft, textvariable=self.var_total, width=22, font=("arial", 13, "bold"))
        txt_total_cost.grid(row=9, column=1)

        #bill button
        btnBill = Button(lableFrameLeft, text="Bill", command=self.total, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        #right side image
        img3 = Image.open(r"D:\College Project\Python\Hotel Management System\images\room.jpg")
        img3 = img3.resize((520,300), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=520, height=200)

        #buttons
        btn_frame = Frame(lableFrameLeft, bd = 2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        #table frame search system
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details & Search Engine", padx=2, font=("times new roman", 12, "bold"))
        table_frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy=Label(table_frame, font=("arial", 12, "bold"), text="Search By: ", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=19, state="readonly")
        combo_search["value"]=("contact", "roomavailable")
        combo_search.current(0)
        combo_search.grid(row=0, column=1, padx=2)

        self.text_search = StringVar()
        txtSearch=ttk.Entry(table_frame, textvariable=self.text_search, font=("arial", 13, "bold"), width=19)
        txtSearch.grid(row=0, column=2, padx=2)
        
        btnSearch = Button(table_frame, text="Search", command=self.search_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(table_frame, text="Show All", command=self.fetch_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)


        #show data table
        details_table = Frame(table_frame, bd = 2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)    

        self.room_table = ttk.Treeview(details_table, columns=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-In")
        self.room_table.heading("checkout", text="Check-Out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room Available")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="Number of days    ")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    #add data
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "Please enter all data", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into room values(%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_contact.get(),
                    self.var_checkin.get(),
                    self.var_checkout.get(),
                    self.var_roomtype.get(),
                    self.var_roomavailable.get(),
                    self.var_meal.get(),
                    self.var_noofdays.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked Successfully", parent = self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent = self.root)


    #update
    def update_data(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error!", "Please enter mobile number", parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set checkin = %s, checkout = %s, roomtype = %s, roomavailable = %s, meal = %s, noofdays = %s where contact = %s", (
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noofdays.get(),
                self.var_contact.get()
            ))
            conn.commit()  
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room booking has been updated successfully", parent = self.root)


    #delete data
    def delete_data(self):
        delete_data = messagebox.askyesno("Hotel Management System", "Do you want to delete this?", parent = self.root)
        if delete_data > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from room where contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    #reset data
    def reset_data(self):
        self.var_checkin.set(" "),
        self.var_checkout.set(" "),
        self.var_roomtype.set(" "),
        self.var_roomavailable.set(" "),
        self.var_meal.set(" "),
        self.var_noofdays.set(" "),
        self.var_paidtax.set(" "),
        self.var_subtotal.set(" "),
        self.var_total.set(" ")


    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()
 
    #get cursor
    def get_cursor(self, event = ""):
        cusrsor_row = self.room_table.focus()
        content = self.room_table.item(cusrsor_row)
        row = content["values"]

        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])



    #fetch all data
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error!", "Please enter contact number", parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            query = "select name from customer where mobile = %s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror("Error", "This number not found", parent = self.root)
            else:
                conn.commit()
                conn.close()

                #name
                showDataFrame = Frame(self.root, bd = 4, relief = RIDGE, padx = 2)
                showDataFrame.place(x = 450, y = 55, width=300, height=180)

                lblName = Label(showDataFrame, text = "Name: ", font = ("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl = Label(showDataFrame, text = row, font = ("arial", 12, "bold"))
                lbl.place(x=65, y=0)

                #gender
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
                my_cursor = conn.cursor()
                query = "select gender from customer where mobile = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataFrame, text = "Gender: ", font = ("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataFrame, text = row, font = ("arial", 12, "bold"))
                lbl2.place(x=65, y=30)

                #email
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
                my_cursor = conn.cursor()
                query = "select email from customer where mobile = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataFrame, text = "Email: ", font = ("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataFrame, text = row, font = ("arial", 12, "bold"))
                lbl3.place(x=65, y=60)

                #nationality
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
                my_cursor = conn.cursor()
                query = "select nationality from customer where mobile = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblNationality = Label(showDataFrame, text = "Nationality: ", font = ("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl4 = Label(showDataFrame, text = row, font = ("arial", 12, "bold"))
                lbl4.place(x=90, y=90)

                #address
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
                my_cursor = conn.cursor()
                query = "select address from customer where mobile = %s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()

                lblAddress = Label(showDataFrame, text = "Address: ", font = ("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl5 = Label(showDataFrame, text = row, font = ("arial", 12, "bold"))
                lbl5.place(x=75, y=120)


    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate - inDate).days)

        #=====================Luxury==========================
        if (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Luxury"):
            food_exp = float(200)
            room_type_exp = float(1000)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            food_exp = float(500)
            room_type_exp = float(1000)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            food_exp = float(800)
            room_type_exp = float(1000)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "All Meals" and self.var_roomtype.get() == "Luxury"):
            food_exp = float(1300)
            room_type_exp = float(1000)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)


        #=====================Single==========================
        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            food_exp = float(200)
            room_type_exp = float(500)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            food_exp = float(500)
            room_type_exp = float(500)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            food_exp = float(800)
            room_type_exp = float(500)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "All Meals" and self.var_roomtype.get() == "Single"):
            food_exp = float(1300)
            room_type_exp = float(500)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        #=====================Double==========================
        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Double"):
            food_exp = float(200)
            room_type_exp = float(800)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            food_exp = float(500)
            room_type_exp = float(800)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            food_exp = float(800)
            room_type_exp = float(800)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

        elif (self.var_meal.get() == "All Meals" and self.var_roomtype.get() == "Double"):
            food_exp = float(1300)
            room_type_exp = float(800)
            total_days = float(self.var_noofdays.get())
            room_exp = float(food_exp + room_type_exp)
            total_exp = float(total_days * room_exp)
            tax = "Rs. " + str("%.2f" %((total_exp) * 0.09))
            st = "Rs. " + str("%.2f" %((total_exp)))
            tt = "Rs. " + str("%.2f" %(total_exp + ((total_exp)*0.09)))
            self.var_paidtax.set(tax)
            self.var_subtotal.set(st)
            self.var_total.set(tt)

    #search system
    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where " + str(self.search_var.get()) + " LIKE '%" + str(self.text_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

        

    
    










if __name__ == "__main__":
    root = Tk()  
    obj = room_booking(root)
    root.mainloop()