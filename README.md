# Hotel Management System

We all know, data management has became so important over the past few years. 

Nowadays, It is not only about managing the data. In order to maintain the privacy of any user, we have had to look for an optimal & handy software which can be used in one's daily life without any issue or problems.

Few days back, I visited a hotel.

There, the booking process was going on. I noticed that they were using old fashioned registers to make the entry of the new customer, which takes alot of time, wastes alot of paper, ink & not at all a good or healthy solution for enviroment.

I got an idea to develop something using my skills, knowledge and coding concepts.

## Here comes the concept of Hotel Management System.

* This software was developed in **Python** 
* Made an interactive GUI using **Tkinter**
* Added **various functions** to perform **several tasks**.
* Added **Login/SignUp** system for security.
* Used **MySQL Workbench** for database, and store the data in table.
* It can be operated in **Windows**.
* The whole program was coded on **VS Code**

## Screens of Hotel Management System.

### Login/SignUp System

**MySQL Workbench is being used to store the ID & Password.**
Since, This software is going to carry sensitive information of a user like Card Details, ID Details, etc. & it should only be accessed by the Admin. I've added a Login feature into the software for the security.

* This is the first page of the software.
* It requires Username & Password to login/enter into the software
* If the management wants to have more than one admin, SignUp feature allows them.
  > SignUp 
  * Here comes the Registration process of new admin.
  * It requires various information from the new admin, like:
    * First Name
    * Last Name
    * Contact Number
    * Email ID
    * Security Questions to be asked ((If forgotten password) (Combo Box))
    * Security Answer (Input Field )
    * Password
    * Confirm Password (It should be matched with the password field)
    * Terms & Conditions (Checkbox)
  * It has two buttons
    * Register Now : It registers the new admin successfully if all the required fields were answerd.
    * Login : If managemnet doesn't wants to continue with the new admin.
    
* If the admin forgots the account password.
  > Forgot Password
  * Here comes the process of creating new password.
  * It requires various details from the admin, like:
    * Security Questions (Which was added during SignUp process) (Combo Box)
    * Security Answer (Corrorponding to question) (Input Field)
    * New Password
  * If all the deatils have been added correctly, admin clicks the Reset Password Button.  
  
  
  
  
  
  
  
  
  
In order to book a room for customer, I've devided this process into 3 different screens.
## Adding Customer Deatils.

There's an Admin, who can perform various functions on this management system like **Add Data**, **Update Data**, **Delete Data**, **Read Data** & **Fetch Data** to ease the booking process.

> **Add Data**
* Admin can add the **basic/personal details** of the customer.
* **Unique Customer Reference** will be alloted to **every new customer**.
* **Unique Customer Reference** has been **kept unedited**, or in **readonly format**.
* The moment admin clicks **Add** button, **Add Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" data gets added in the table of **MySQL Workbench**.
    * Else data will not be added in the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Update Data**
* Admin can update the **basic/personal details** of the customer.
* **Unique Customer Reference** will be not be affected of **any updated customer**.
* **Unique Customer Reference** will remain **unedited**, or in **readonly format**.
* The moment admin clicks "**Update**" button, **Update Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" data gets updated in the table of **MySQL Workbench**.
    * Else data will not be updated in the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Delete Data**
* Admin can delete the **basic/personal details** of the student.
* **Unique Customer Reference** will also be deleted along with the whole record of the customer.
* The moment admin clicks "**Delete Data**" button, **Delete Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" the whole record will be deleted from the table of **MySQL Workbench**.
    * Else data will not be deleted from the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Fetch Data**
* Admin can fetch the **basic/personal details** of the customer using the unique "**Customer Reference**", or "**Mobile Number**".
* Admin will be required to add the "**Student ID**", or "**Mobile Number**" of the customer to fetch the corresponding data.
* The moment admin clicks "**Fetch Data**" button, **Fetch Data** function gets called.
* At the same time, respective data is shown on the screen.

> **Reset Data**
* Admin can reset the **basic/personal details** of the screen.
* **Unique Customer Reference** will also get reset.
* The moment admin clicks "**Reset**" button, **Reset Data** function gets called.
* Admin can now easily enter the data again.

> **Read Data**
* Admin can read the **basic/personal details** of the student in there **respective columns, or fields**.
* Admin will be required to **click on a particular record** of the student which is shown on the right side of the screen.
* The moment admin clicks a record, **Read Data** functions gets called.
* At the same time respective columns, or fields will be filled with the corresponding data.

**Customer has been added. Now, here comes the room booking system.**









After adding the new customer, here comes the process of booking a desired room for them.
## Booking the Room.

Here, Admin performs various functions on this screen to ease the booking process.

> **Fetch Data**
* Admin can fetch the **basic/personal details** of the customer using the "**Mobile Number**".
* Admin will be required to add the "**Mobile Number**" of the customer to fetch the corresponding data to verify that customer.
* The moment admin clicks "**Fetch Data**" button, **Fetch Data** function gets called.
* At the same time, respective data is shown on the screen.

> **Bill**
* This button helps to calculate the bill of the customer according to the following deatils:
  * Check-In Date.
  * Check-Out Date.
  * Room Type (Combo Box)
  * Available Rooms (Combo Box)
  * Meals (Combo Box)
* Once the admin clicks "**Bill**" button, bill gets generated & gets devided into respective fields.
  * Number of Days (Calculated on the basis of Check-In & Check-Out Date)
  * Sub Total (Calculated on the basis of Room Type, Number of Days & Meals)
  * Tax (Calculated on sub total)
  * Total Cost (Sum of Tax & Sub Total)

> **Add Data**
* Admin adds the **Booking Details** of the customer.
* The moment admin clicks **Add** button, **Add Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" data gets added in the table of **MySQL Workbench**.
    * Else data will not be added in the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Update Data**
* Admin can update the **Booking Details** of the customer.
* **Unique Customer Reference** will be not be affected of **any updated customer**.
* **Unique Customer Reference** will remain **unedited**, or in **readonly format**.
* The moment admin clicks "**Update**" button, **Update Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" data gets updated in the table of **MySQL Workbench**.
    * Else data will not be updated in the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Delete Data**
* Admin can delete the **Booking Details** of the student.
* **Unique Customer Reference** will also be deleted along with the whole record of the customer.
* The moment admin clicks "**Delete**" button, **Delete Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" the whole record will be deleted from the table of **MySQL Workbench**.
    * Else data will not be deleted from the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Reset Data**
* Admin can reset the **Booking Details** of the screen.
* **Unique Customer Reference** will also get reset.
* The moment admin clicks "**Reset**" button, **Reset Data** function gets called.
* Admin can now easily enter the data again.

> **Read Data**
* Admin can read the **Booking Details** of the customer in there **respective columns, or fields**.
* Admin will be required to **click on a particular record** of the customer which is shown on the right side of the screen.
* The moment admin clicks a record, **Read Data** functions gets called.
* At the same time respective columns, or fields will be filled with the corresponding data.

**Room has been booked, alloted to the customer. Now customer can enjoy the stay.**









After booking a room, here comes the process of adding rooms in hotel.
## Adding Room.

Here, Admin performs various functions on this screen to add more rooms in the software.

To add the rooms in the software, admin is required to fill the following details of the room.
* Room ID (Automatically gets generated for each room)
* Floor Number
* Room Type (Combo Box)
* Room Number

> **Add Data**
* Admin adds the **Room Details** of the hotel.
* "**Unique Room ID**" will be generated for each customer.
* "**Unique Room ID**" will be **unedited**, or in **readonly format**.
* The moment admin clicks **Add** button, **Add Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" data gets added in the table of **MySQL Workbench**.
    * Else data will not be added in the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Update Data**
* Admin can update the **Room Details** of the hotel.
* **Unique Room ID** will be not be affected of **any updated customer**.
* **Unique Room ID** will remain **unedited**, or in **readonly format**.
* The moment admin clicks "**Update**" button, **Update Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" data gets updated in the table of **MySQL Workbench**.
    * Else data will not be updated in the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Delete Data**
* Admin can delete the **Room Details** from the hotel.
* **Unique Room ID** will also be deleted along with the whole record of the customer.
* The moment admin clicks "**Delete**" button, **Delete Data** function gets called.
  * Confirmation box occurs **asking yes/no**.
    * If user clicks "**YES**" the whole record will be deleted from the table of **MySQL Workbench**.
    * Else data will not be deleted from the tabel.
* At the same time, "**Fetch Data**" function gets called on the same button, and data is shown on the screen.

> **Reset Data**
* Admin can reset the **Room Details Form** of the screen.
* **Unique Room ID** will also get reset.
* The moment admin clicks "**Reset**" button, **Reset Data** function gets called.
* Admin can now easily enter the data again.
  
> **Read Data**
* Admin can read the **Booking Details** of the customer in there **respective columns, or fields**.
* Admin will be required to **click on a particular record** of the customer which is shown on the right side of the screen.
* The moment admin clicks a record, **Read Data** functions gets called.
* At the same time respective columns, or fields will be filled with the corresponding data.









Whenever, Admin wants to logout from the software. There's an Logout Button.
## Logout.

Here, Admin will be required to click on the Logout button.
Once, Admin cicks Logout.
System will be automatically closed, and will require login username & password again.





## Challenges faced in the development phase

There were **many different challenges** which I faced during the development of **Hotel Management System**.

With **R&D**, I managed to overcome all of them, and came up with the desired output.

But, following are some challenges I faced.

* The first challenge was to make an interactive & simple GUI, which can be understood easily by any non-tech profile.
* The second challenge was to setup the database, and integrate the table to play with the records.
* The third challenge was to add proper exceptions, if the user fails to provide required details of the student.
* The fourth challenge was to set up a working connection string with MySQL workbench.
* The last challenge was to test, and bug hunting in the management system.

## New Features that can be seen in future
Some of the updates that can be seen in the project in future.

> Design Updates
* More interesting GUI will be seen in the future.
* More eye catchy color gradings, and photos.
* Some good animations, to make it look more interactive.

> Development Updates
* More diversifications like pool parties, games, drinks, etc will be seen.
* Click send mail will be seen the future.
* Will be generating Invoice for customers.
* Check-Out and Rating System will be seen.
