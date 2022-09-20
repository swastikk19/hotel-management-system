from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector


class register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register User")
        self.root.geometry("1550x800+0+0")

        #variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_password = StringVar()
        self.var_confirm_password = StringVar()
        self.var_check = IntVar()


        #bg image
        self.bg = ImageTk.PhotoImage(file = r"D:\College Project\Python\Hotel Management System\images\bg.jpg")
        lbl_bg = Label(self.root, image = self.bg)
        lbl_bg.place(x = 0, y = 0, relwidth=1, relheight=1)

        #left image
        self.bg1 = ImageTk.PhotoImage(file = r"D:\College Project\Python\Hotel Management System\images\bgleft.jpg")
        lbl_left = Label(self.root, image = self.bg1)
        lbl_left.place(x = 50, y = 100, width=470, height=550)

        #main frame
        frame = Frame (self.root, bg = "white")
        frame.place(x = 520, y = 100, width=800, height=550)

        register_lbl = Label(frame, text = "REGISTER HERE", font = ("times new roman", 20, "bold"), fg = "dark green", bg = "white")
        register_lbl.place(x = 20, y = 20)

        #labels and entries
        #----------------------row 1
        fname = Label(frame, text="First Name: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        fname.place(x=50, y=100)
        self.fname = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15))
        self.fname.place(x=50, y=130, width = 250)

        lname = Label(frame, text="Last Name: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        lname.place(x=370, y=100)
        self.lname = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15))
        self.lname.place(x=370, y=130, width = 250)


        #----------------------row 2
        contact = Label(frame, text="Contact Number: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        contact.place(x=50, y=170)
        self.contact = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15))
        self.contact.place(x=50, y=200, width = 250)

        email = Label(frame, text="Email: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        email.place(x=370, y=170)
        self.email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.email.place(x=370, y=200, width = 250)


        #----------------------row 3
        securityQ = Label(frame, text="Security Questions: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        securityQ.place(x=50, y=240)
        combo_securityQ = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15), state="readonly")
        combo_securityQ["values"]=("Select", "Father's Name", "Pet Name", "Bestfriend's Name")
        combo_securityQ.current(0)
        combo_securityQ.place(x = 50, y = 270, width = 250)

        securityA = Label(frame, text="Security Answer: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        securityA.place(x=370, y=240)
        self.securityA = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.securityA.place(x=370, y=270, width = 250)


        #----------------------row 4
        password = Label(frame, text="Password: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        password.place(x=50, y=310)
        self.password = ttk.Entry(frame, textvariable=self.var_password, font=("times new roman", 15))
        self.password.place(x=50, y=340, width = 250)

        confirm_password = Label(frame, text="Confirm Password: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
        confirm_password.place(x=370, y=310)
        self.confirm_password = ttk.Entry(frame, textvariable=self.var_confirm_password, font=("times new roman", 15))
        self.confirm_password.place(x=370, y=340, width = 250)


        #check button
        checkbtn = Checkbutton(frame, variable=self.var_check, text = "I agree the terms & conditions", font=("times new roman", 12, "bold"), bg="white", onvalue=1, offvalue=0, activeforeground="white", activebackground="white")
        checkbtn.place(x = 50, y = 380)

        #buttons
        register_btn = Button(frame, text = "Resgister Now", command=self.register_user, font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "red", activeforeground="white", activebackground="red")
        register_btn.place(x = 45, y = 420, width = 250)

        login_btn = Button(frame, text = "Login", font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "red", activeforeground="white", activebackground="red")
        login_btn.place(x = 370, y = 420, width = 250)


    def register_user(self):
        if (self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select"):
            messagebox.showerror("Error", "All fields are required")
        elif (self.var_password.get() != self.confirm_password.get()):
            messagebox.showerror("Error", "Password & Confrim Password must be same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Check to terms & conditions")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.var_email.get(), )
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row != None:
                messagebox.showerror("Error", "User already exist, please try another email")
            else:
                my_cursor.execute("insert into register values (%s, %s, %s, %s, %s, %s, %s)", (
                    self.var_fname.get(),
                    self.var_lname.get(),
                    self.var_contact.get(),
                    self.var_email.get(),
                    self.var_securityQ.get(),
                    self.var_securityA.get(),
                    self.var_password.get()
                ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Registered Successfully")





















if __name__ == "__main__":
    root = Tk()
    obj = register(root)
    root.mainloop()