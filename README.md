🏦 Banking Simulator (Python + Tkinter + SQLite)

##  Project Overview

The Banking Simulator is a desktop application built using Python and Tkinter GUI that performs basic banking operations.
The system allows both Admin and Customer users to log in and manage banking activities.

This project is designed for educational purposes and demonstrates GUI design, database connectivity, authentication, and transaction management.


# Features

## Admin Panel

Admin login credentials:

* Account No: 0
* Password: admin

Admin can perform the following operations:

✔ Open New Account
✔ View Account Details
✔ Close Account (with OTP verification)
✔ Email notification on account creation
✔ Secure account closing system

## Customer Panel

After logging in, customers can:

✔ View Account Details
✔ Edit Profile (Name, Email, Mobile, Password)
✔ Deposit Money
✔ Withdraw Money
✔ Transfer Money
✔ Real-time Balance Updates


## Security Features

✔ Login authentication
✔ CAPTCHA verification
✔ OTP-based password recovery
✔ OTP verification before account closure
✔ Email alerts for important actions


## Forgot Password System

Customers can recover their password by:

1. Entering account number and registered email
2. Receiving an OTP via email
3. Verifiying OTP to view the password


# Database

Database: SQLite

Table Name: 'accounts'

# Fields:

| Field    | Description                  |
| -------- | ---------------------------- |
| acn      | Account Number (Primary Key) |
| name     | Customer Name                |
| pass     | Account Password             |
| bal      | Account Balance              |
| mob      | Mobile Number                |
| adhar    | Aadhaar Number               |
| email    | Email Address                |
| opendate | Account Opening Date         |



# Technologies Used

* Python
* Tkinter (GUI Development)
* SQLite3 (Database)
* PIL (Image handling)
* SMTP Mailing (OTP & notifications)


# Project Modules

| File         | Purpose                  |
| ------------ | ------------------------ |
| main.py      | Main application GUI     |
| table.py     | Database table creation  |
| generator.py | CAPTCHA & OTP generation |
| mailing.py   | Email sending functions  |
| bank.sqlite  | Database file            |
| logo.png     | Application logo         |



# How to Run the Project

## install Required Library

```bash
pip install pillow
```


##  Run the Application

```bash
python main.py
```



# Usage Flow

# Admin:

1. Login as Admin
2. Open a new account
3. Customer receives credentials via email

# Customer:

1. Login using account number & password
2. Perform banking operations


# Email Functionality

The system automatically sends emails for:

✔ Account creation credentials
✔ OTP for password recovery
✔ OTP for account closure

 Ensure an internet connection and correct email configuration.



# Educational Concepts Covered

✔ GUI Programming
✔ Database Connectivity
✔ Authentication Systems
✔ OTP & Security Workflow
✔ Transaction Handling
✔ Event-driven Programming


# Important Notes

* Ensure the database file path is correct.
* Configure the mailing module with valid sender credentials.
* Do not share admin credentials publicly.
* This project is for educational use.



# Author

Harshit
7906117754


# Future Improvements

✔ Dark mode UI
✔ Transaction history
✔ Mini statement
✔ ATM PIN security
✔ Mobile app version
✔ Charts & analytics



# Conclusion

This Banking Simulator project demonstrates practical implementation of Python GUI development with database integration.
It provides a strong foundation for understanding real-world application development concepts.


