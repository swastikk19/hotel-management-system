from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox



class cust_win:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")


        #variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_idproof = StringVar()
        self.var_idnumber = StringVar()
        self.var_address = StringVar()


        #title
        lbl_title = Label(self.root, text = "ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)


        #logo
        img2 = Image.open(r"D:\College Project\Python\Hotel Management System\images\logo.png")
        img2 = img2.resize((100,40), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        #lable frame
        lableFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="CUSTOMER DETAILS", padx=2, font=("times new roman", 12, "bold"))
        lableFrameLeft.place(x=5, y=50, width=425, height=490)

        #lables and entries
        #cust ref
        lbl_cust_ref = Label(lableFrameLeft, text="Customer Reference: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(lableFrameLeft, textvariable=self.var_ref, width=22, font=("arial", 13, "bold"), state="readonly")
        entry_ref.grid(row=0, column=1)
        
        #cust name
        cname = Label(lableFrameLeft, text="Customer Name: ", font=("arial", 12, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(lableFrameLeft, textvariable=self.var_cust_name, width=22, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        #mother name
        lblmname = Label(lableFrameLeft, text="Mother Name: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        txtmname = ttk.Entry(lableFrameLeft, textvariable=self.var_mother, width=22, font=("arial", 13, "bold"))
        txtmname.grid(row=2, column=1)

        #gender combobox
        label_gender = Label(lableFrameLeft, font=("arial", 12, "bold"), text="Gender: ", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(lableFrameLeft, font=("arial", 12, "bold"), textvariable=self.var_gender, width=22, state="readonly")
        combo_gender["value"]=("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        #postcode
        lblPostCode=Label(lableFrameLeft, font=("arial", 12, "bold"), text="PostCode: ", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode=ttk.Entry(lableFrameLeft, font=("arial", 13, "bold"), textvariable=self.var_post, width=22)
        txtPostCode.grid(row=4, column=1)

        #mobile number
        lblMobile=Label(lableFrameLeft, font=("arial", 12, "bold"), text="Mobile: ", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile=ttk.Entry(lableFrameLeft, font=("arial", 13, "bold"), textvariable=self.var_mobile, width=22)
        txtMobile.grid(row=5, column=1)

        #email
        lblEmail=Label(lableFrameLeft, font=("arial", 12, "bold"), text="Email: ", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail=ttk.Entry(lableFrameLeft, font=("arial", 13, "bold"), textvariable=self.var_email, width=22)
        txtEmail.grid(row=6, column=1)


        #nationality
        lblNationality=Label(lableFrameLeft, font=("arial", 12, "bold"), text="Nationality: ", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        combo_nationality = ttk.Combobox(lableFrameLeft, font=("arial", 12, "bold"), textvariable=self.var_nationality, width=22, state="readonly")
        combo_nationality["value"]=("Indian", "American", "Britisher", "Russian")
        combo_nationality.current(0)
        combo_nationality.grid(row=7, column=1)

        #Id Proof
        lblIdProof=Label(lableFrameLeft, font=("arial", 12, "bold"), text="Id Proof Type: ", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)
        combo_id = ttk.Combobox(lableFrameLeft, font=("arial", 12, "bold"), textvariable=self.var_idproof, width=22, state="readonly")
        combo_id["value"]=("Adhaar Card", "Driving Liscence", "Passport", "Pan Card")
        combo_id.current(0)
        combo_id.grid(row=8, column=1)

        #ID Number
        lblIdNumber=Label(lableFrameLeft, font=("arial", 12, "bold"), text="Id Number: ", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber=ttk.Entry(lableFrameLeft, font=("arial", 13, "bold"), textvariable=self.var_idnumber, width=22)
        txtIdNumber.grid(row=9, column=1)

        #Address
        lblAddress=Label(lableFrameLeft, font=("arial", 12, "bold"), text="Address: ", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress=ttk.Entry(lableFrameLeft, font=("arial", 13, "bold"), textvariable=self.var_address, width=22)
        txtAddress.grid(row=10, column=1)




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
        table_frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy=Label(table_frame, font=("arial", 12, "bold"), text="Search By: ", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_search = ttk.Combobox(table_frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=19, state="readonly")
        combo_search["value"]=("mobile", "ref")
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
        details_table.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)    

        self.cust_details_table = ttk.Treeview(details_table, columns=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cust_details_table.xview)
        scroll_y.config(command=self.cust_details_table.yview)

        self.cust_details_table.heading("ref", text="Reference")
        self.cust_details_table.heading("name", text="Name")
        self.cust_details_table.heading("mother", text="Mother's Name")
        self.cust_details_table.heading("gender", text="Gender")
        self.cust_details_table.heading("post", text="Post")
        self.cust_details_table.heading("mobile", text="Mobile Number")
        self.cust_details_table.heading("email", text="Email Id")
        self.cust_details_table.heading("nationality", text="Nationality")
        self.cust_details_table.heading("idproof", text="Id Proof")
        self.cust_details_table.heading("idnumber", text="Id Number")
        self.cust_details_table.heading("address", text="Address")

        self.cust_details_table["show"] = "headings"

        self.cust_details_table.column("ref", width=100)
        self.cust_details_table.column("name", width=100)
        self.cust_details_table.column("mother", width=100)
        self.cust_details_table.column("gender", width=100)
        self.cust_details_table.column("post", width=100)
        self.cust_details_table.column("mobile", width=100)
        self.cust_details_table.column("email", width=100)
        self.cust_details_table.column("nationality", width=100)
        self.cust_details_table.column("idproof", width=100)
        self.cust_details_table.column("idnumber", width=100)
        self.cust_details_table.column("address", width=100)

        self.cust_details_table.pack(fill=BOTH, expand=1)
        self.cust_details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "Please enter all fields", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_idproof.get(),
                    self.var_idnumber.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success", "User has been added successfully", parent = self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent = self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event = ""):
        cusrsor_row = self.cust_details_table.focus()
        content = self.cust_details_table.item(cusrsor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nationality.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    def update_data(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error!", "Please enter mobile number", parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set name = %s, mother = %s, gender = %s, post = %s, mobile = %s, email = %s, nationality = %s, idproof = %s, idnumber = %s, address = %s where ref = %s", (
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_idproof.get(),
                self.var_idnumber.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            conn.commit()  
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details has been updated successfully", parent = self.root)

    
    def delete_data(self):
        delete_data = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent = self.root)
        if delete_data > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from customer where ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_data:
                return
        conn.commit()
        self.fetch_data()
        conn.close()


    def reset_data(self):
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_idnumber.set("")
        self.var_address.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))


    def search_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where " + str(self.search_var.get()) + " LIKE '%" + str(self.text_search.get()) + "%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.cust_details_table.delete(*self.cust_details_table.get_children())
            for i in rows:
                self.cust_details_table.insert("", END, values=i)
            conn.commit()
        conn.close()
        


if __name__ == "__main__":
    root = Tk()
    obj = cust_win(root)
    root.mainloop()