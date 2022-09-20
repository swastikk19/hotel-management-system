from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from datetime import datetime
from tkinter import messagebox





class room_details:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

        self.var_id = StringVar()
        x = random.randint(1001, 50000)
        self.var_id.set(str(x))

        #title
        lbl_title = Label(self.root, text = "ADD ROOMS", font=("times new roman", 18, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1295, height=50)

        #logo
        img2 = Image.open(r"D:\College Project\Python\Hotel Management System\images\logo.png")
        img2 = img2.resize((100,40), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=5, y=2, width=100, height=45)

        #lable frame
        lableFrameLeft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room Details", padx=2, font=("times new roman", 12, "bold"))
        lableFrameLeft.place(x=5, y=50, width=540, height=350)


        #lables and entries
        #room id
        lbl_room_id = Label(lableFrameLeft, text="Room ID: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_room_id.grid(row=0, column=0, sticky=W)
        entry_room_id = ttk.Entry(lableFrameLeft, textvariable=self.var_id, width=22, font=("arial", 13, "bold"), state="readonly")
        entry_room_id.grid(row=0, column=1)

        #floor
        self.var_floor = StringVar()
        lbl_floor = Label(lableFrameLeft,text="Floor: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=1, column=0, sticky=W)
        entry_floor = ttk.Entry(lableFrameLeft, textvariable=self.var_floor, width=20, font=("arial", 13, "bold"))
        entry_floor.grid(row=1, column=1, sticky=W)

        #room type
        self.var_roomtype = StringVar()
        lbl_roomtype = Label(lableFrameLeft,text="Room Type: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_roomtype.grid(row=2, column=0, sticky=W)
        combo_room_type = ttk.Combobox(lableFrameLeft, textvariable=self.var_roomtype, font=("arial", 12, "bold"), width=22, state="readonly")
        combo_room_type["value"]=("Single", "Double", "Luxury")
        combo_room_type.current(0)
        combo_room_type.grid(row=2, column=1, sticky=W)

        #room num
        self.var_roomno = StringVar()
        lbl_roomno = Label(lableFrameLeft,text="Room Number: ", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_roomno.grid(row=3, column=0, sticky=W)
        entry_roomno = ttk.Entry(lableFrameLeft, textvariable=self.var_roomno, width=20, font=("arial", 13, "bold"))
        entry_roomno.grid(row=3, column=1, sticky=W)


        #buttons
        btn_frame = Frame(lableFrameLeft, bd = 2, relief=RIDGE)
        btn_frame.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 13, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)


        #table frame search system
        table_frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Showroom Details", padx=2, font=("times new roman", 12, "bold"))
        table_frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)    
        self.room_table = ttk.Treeview(table_frame, columns=("roomid", "floor", "roomtype", "roomno"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("roomid", text = "Room ID")
        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomno", text="Room Number")

        self.room_table["show"] = "headings"

        self.room_table.column("roomid", width=100)
        self.room_table.column("floor", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    #add data
    def add_data(self):
        if self.var_floor.get() == "" or self.var_roomtype.get() == "":
            messagebox.showerror("Error", "Please enter all fields", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into details values(%s, %s, %s, %s)", (
                    self.var_id.get(),
                    self.var_floor.get(),
                    self.var_roomtype.get(),
                    self.var_roomno.get()
                ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()
                messagebox.showinfo("Success", "New room has been added successfully", parent = self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent = self.root)


    #fetch data
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from details")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    #update
    def update_data(self):
        if self.var_floor.get() == "":
            messagebox.showerror("Error!", "Please enter room number", parent = self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("update details set floor = %s, roomtype = %s, roomno = %s where roomid = %s", (
                self.var_floor.get(),
                self.var_roomtype.get(),
                self.var_roomno.get(),
                self.var_id.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details has been updated successfully", parent = self.root)


    #get cursor
    def get_cursor(self, event = ""):
        cusrsor_row = self.room_table.focus()
        content = self.room_table.item(cusrsor_row)
        row = content["values"]

        self.var_id.set(row[0])
        self.var_floor.set(row[1])
        self.var_roomtype.set(row[2])
        self.var_roomno.set(row[3])


    #delete data
    def delete_data(self):
        delete_data = messagebox.askyesno("Hotel Management System", "Do you want to delete this?", parent = self.root)
        if delete_data > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            query = "delete from details where roomid=%s"
            value = (self.var_id.get(),)
            my_cursor.execute(query, value)
        else:
            if not delete_data:
                return
        conn.commit()
        self.fetch_data()
        self.reset_data()
        conn.close()


    #reset data
    def reset_data(self):
        x = random.randint(1001, 50000)
        self.var_id.set(str(x))

        self.var_floor.set(" "),
        self.var_roomtype.set(" "),
        self.var_roomno.set(" ")





if __name__ == "__main__":
    root = Tk()
    obj = room_details(root)
    root.mainloop()