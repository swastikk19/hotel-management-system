from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import mysql.connector
from customer import cust_win
from room import room_booking
from details import room_details
from hotel import HotelManagementSystem


def main():
    win = Tk()
    app = login_win(win)
    win.mainloop() 


class login_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file = r"D:\College Project\Python\Hotel Management System\images\bg.jpg")

        lbl_bg = Label(self.root, image = self.bg)
        lbl_bg.place(x = 0, y = 0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg = "black")
        frame.place(x = 550, y = 200, width=400, height=450)

        img1 = Image.open(r"D:\College Project\Python\Hotel Management System\images\login.png")
        img1 = img1.resize((100, 100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(image= self.photoimg1, bg = "black", borderwidth=0)
        lblimg1.place(x = 710, y = 210, width=100, height=100)

        get_str = Label(frame, text = "Get Started", font = ("times new roman", 20, "bold"), fg = "white", bg = "black")
        get_str.place (x = 130, y = 110)

        #labels 
        lbl_username = Label(frame, text = "Username: ", font = ("times new roman", 15, "bold"), fg = "white", bg = "black")
        lbl_username.place(x = 50, y = 190)
        self.txt_username = ttk.Entry(frame, font = ("times new roman", 15, "bold"))
        self.txt_username.place(x = 170, y = 190, width= 200)

        lbl_password = Label(frame, text = "Password: ", font = ("times new roman", 15, "bold"), fg = "white", bg = "black")
        lbl_password.place(x = 50, y = 250)
        self.txt_password = ttk.Entry(frame, font = ("times new roman", 15, "bold"))
        self.txt_password.place(x = 170, y = 250, width= 200)

        #icon images
        img2 = Image.open(r"D:\College Project\Python\Hotel Management System\images\username.jpg")
        img2 = img2.resize((25, 25), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg2 = Label(image= self.photoimg2, bg = "black", borderwidth=0)
        lblimg2.place(x = 570, y = 392, width=25, height=25)

        img3 = Image.open(r"D:\College Project\Python\Hotel Management System\images\password.png")
        img3 = img3.resize((25, 25), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lblimg3 = Label(image= self.photoimg3, bg = "black", borderwidth=0)
        lblimg3.place(x = 570, y = 452, width=25, height=25)


        #buttons
        login_btn = Button(frame, text = "Login", command=self.login, font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "red", activeforeground="white", activebackground="red")
        login_btn.place(x = 135, y = 330, width = 120, height=35)

        register_btn = Button(frame, text = "SignUp", command = self.register_win, font = ("times new roman", 10, "bold"), borderwidth = 0, relief=RIDGE, fg = "white", bg = "black", activeforeground="white", activebackground="black")
        register_btn.place(x = 135, y = 375, width = 120)

        forgot_btn = Button(frame, text = "Forgot Password?", command = self.forgot_password, font = ("times new roman", 10, "bold"), borderwidth = 0, relief=RIDGE, fg = "white", bg = "black", activeforeground="white", activebackground="black")
        forgot_btn.place(x = 280, y = 422, width = 120)

    def register_win(self):
        self.new_window = Toplevel(self.root)
        self.app = register(self.new_window)

    def login(self):
        if self.txt_username.get() == "" or self.txt_password.get() == "":
            messagebox.showerror("Error!", "All fields required")

        elif self.txt_username.get() == "kapu" and self.txt_password.get() == "ashu":
            messagebox.showinfo("Success", "Welcome!")
        
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email = %s and password = %s", (
                self.txt_username.get(),
                self.txt_password.get()
            ))
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Invalid username and password")
            else:
                open_main = messagebox.askyesno("Yes/No", "Access only admin")
                if open_main > 0:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

    def reset_password(self):
        if self.cSecurityQ.get() == "Select":
            messagebox.showerror("Error", "Select security question", parent = self.root2)
        elif self.a_securityA.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent = self.root2)
        elif self.new_password.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent = self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s and securityQ = %s and securityA = %s")
            value = (self.txt_username.get(), self.cSecurityQ.get() ,self.a_securityA.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row == None:
                messagebox.showerror("Error", "Please enter the correct answer", parent = self.root2)
            else:
                query = ("update register set password = %s where email = %s")
                value = (self.new_password.get(), self.txt_username.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Password changed successfully", parent = self.root2)
                self.root2.destroy()

    #forgot password
    def forgot_password(self):
        if self.txt_username.get() == "":
            messagebox.showerror("Error", "Please enter email address")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="1234", database="hotel")
            my_cursor = conn.cursor()
            query = ("select * from register where email = %s")
            value = (self.txt_username.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            #print(row)
            if row == None:
                messagebox.showerror("Error", "Please entre valid username")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                lbl_forgotPas = Label(self.root2, text = "Forgot Password", font = ("times new roman", 20, "bold"), fg = "white", bg = "black")
                lbl_forgotPas.place(x = 0, y = 10, relwidth = 1)

                securityQ = Label(self.root2, text="Security Questions: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
                securityQ.place(x=50, y=80)
                self.cSecurityQ = ttk.Combobox(self.root2, font=("times new roman", 15), state="readonly")
                self.cSecurityQ["values"]=("Select", "Father's Name", "Pet Name", "Bestfriend's Name")
                self.cSecurityQ.current(0)
                self.cSecurityQ.place(x = 50, y = 110, width = 250)

                securityA = Label(self.root2, text="Security Answer: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
                securityA.place(x=50, y=150)
                self.a_securityA = ttk.Entry(self.root2, font=("times new roman", 15))
                self.a_securityA.place(x=50, y=180, width = 250)

                new_password = Label(self.root2, text="New Password: ", font=("times new roman", 15, "bold"), bg = "white", fg = "black")
                new_password.place(x=50, y=220)
                self.new_password = ttk.Entry(self.root2, font=("times new roman", 15))
                self.new_password.place(x=50, y=250, width = 250)

                btn = Button(self.root2, text = "Reset Password", command = self.reset_password, font = ("times new roman", 15, "bold"), bg = "white", fg = "green")
                btn.place(x = 100, y = 290)
        



class HotelManagementSystem:
    def __init__(self, root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

        #1st Image
        img1 = Image.open(r"D:\College Project\Python\Hotel Management System\images\hotel1.jpg")
        img1 = img1.resize((1550,140), Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg = Label(self.root, image=self.photoimg1, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=1550, height=140)

        #logo
        img2 = Image.open(r"D:\College Project\Python\Hotel Management System\images\logo.png")
        img2 = img2.resize((230,140), Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=4, relief=RIDGE)
        lblimg.place(x=0, y=0, width=230, height=140)

        #title
        lbl_title = Label(self.root, text = "HOTEL MANAGEMENT SYSTEM", font=("times new roman", 40, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=140, width=1550, height=50)

        #main frame
        main_frame=Frame(self.root, bd=4, relief=RIDGE)
        main_frame.place(x=0, y=190, width=1550, height=620)

        #menu
        lbl_menu = Label(main_frame, text = "MENU", font=("times new roman", 20, "bold"), bg="black", fg="gold", bd=4, relief=RIDGE)
        lbl_menu.place(x=0, y=0, width=230)

        #button frame
        btn_frame=Frame(main_frame, bd=4, relief=RIDGE)
        btn_frame.place(x=0, y=35, width=228, height=190)

        cust_btn = Button(btn_frame, text="CUSTOMER", command=self.cust_details ,width=22 ,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        cust_btn.grid(row=0, column=0, pady = 1)

        booking_btn = Button(btn_frame, text="BOOKING", command=self.room_booking, width=22, font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        booking_btn.grid(row=1, column=0, pady = 1)

        details_btn = Button(btn_frame, text="DETAILS", command=self.room_details, width=22 ,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        details_btn.grid(row=2, column=0, pady = 1)

        report_btn = Button(btn_frame, text="REPORT",width=22 ,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        report_btn.grid(row=3, column=0, pady = 1)

        logout_btn = Button(btn_frame, text="LOGOUT", command=self.logout,width=22 ,font=("times new roman", 14, "bold"), bg="black", fg="gold", bd=0, cursor="hand1")
        logout_btn.grid(row=4, column=0, pady = 1)

        #right side image
        img3 = Image.open(r"D:\College Project\Python\Hotel Management System\images\reception.png")
        img3 = img3.resize((1310,590), Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1 = Label(main_frame, image=self.photoimg3, bd=4, relief=RIDGE)
        lblimg1.place(x=225, y=0, width=1310, height=590)

        #down images
        img4 = Image.open(r"D:\College Project\Python\Hotel Management System\images\front.jpg")
        img4 = img4.resize((230,210), Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1 = Label(main_frame, image=self.photoimg4, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=225, width=230, height=210)


        img5 = Image.open(r"D:\College Project\Python\Hotel Management System\images\food.jpg")
        img5 = img5.resize((230,190), Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1 = Label(main_frame, image=self.photoimg5, bd=4, relief=RIDGE)
        lblimg1.place(x=0, y=420, width=230, height=190)
    
    def logout(self):
        self.root.destroy()


    def cust_details(self):
        self.new_window = Toplevel(self.root)
        self.app = cust_win(self.new_window)

    def room_booking(self):
        self.new_window = Toplevel(self.root)
        self.app = room_booking(self.new_window)

    def room_details(self):
        self.new_window = Toplevel(self.root)
        self.app = room_details(self.new_window)


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

        login_btn = Button(frame, text = "Login", command=self.return_login, font = ("times new roman", 15, "bold"), bd = 3, relief=RIDGE, fg = "white", bg = "red", activeforeground="white", activebackground="red")
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


    def return_login(self):
        self.root.destroy()















if __name__ == "__main__":
    main()