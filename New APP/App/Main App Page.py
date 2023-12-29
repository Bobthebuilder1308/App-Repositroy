import customtkinter as ctk
from customtkinter import CTkEntry, CTkLabel, CTkToplevel
import tkinter as tk
import subprocess
import csv
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
# Create a custom CTkButton class supporting bg and fg arguments
class CTkButton(ctk.CTkButton):
    def __init__(self, master=None, bg_color=None, fg_color=None, **kwargs):
        super().__init__(master=master, bg_color=bg_color, fg_color=fg_color, **kwargs)
# Create the main window
root = CTkToplevel()
root.title("Teacher & Student Dashboard")
root.geometry("800x600")
root.configure(background='#000000')
# Create a CSV file for user data
csv_file_path = "user_data.csv"
csv_header = ["Name", "Class", "Section", "Role", "E-Mail", "Password"]
# Predefined login credentials
predefined_credentials = {
    "John": {"class": "11", "section": "A", "password": "123", "role": "teacher"},
    "Jane": {"class": "10", "section": "B", "password": "456", "role": "student"},
    "Meet": {"class": "11", "section": "A", "password": "122", "role": "student"},
    "Admin": {"password": "admin", "role": "admin"},
    "announcements": []
}
def handle_signup(name, email, phone, role, password):
    # Check if the name is unique
    if name in predefined_credentials:
        show_custom_message("Sign Up Failed: Username already exists. Please choose another.")
    else:
        # Add the new user to predefined_credentials
        predefined_credentials[name] = {"email": email, "phone": phone, "role": role, "password": password}
        show_custom_message("Sign Up successful! Welcome, {}!".format(name))
        # Add the new user to the CSV file
        with open(csv_file_path, mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([name, predefined_credentials[name].get("class", ""),
                                predefined_credentials[name].get("section", ""),
                                predefined_credentials[name].get("role", ""), email])
        # Add the new user to the CSV file
        with open(csv_file_path, mode='a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([name, predefined_credentials[name].get("class", ""),
                                predefined_credentials[name].get("section", ""),
                                predefined_credentials[name].get("role", ""), email, password])
# Define variables outside the signup_page function
signup_window = None
email_var = None
phone_var = None
role_var = None
# Function to create sign-up page
def signup_page():
    global signup_window, email_var, phone_var, role_var
    # Create the signup_window
    signup_window = CTkToplevel(root)
    signup_window.title("Sign Up")
    signup_window.geometry("500x400")
    signup_window.grab_set()
    CTkLabel(signup_window, text="Sign Up", font=("Arial", 18), bg_color="#000000", fg_color="#d3d3d3").pack(pady=10)
    CTkLabel(signup_window, text="Name:").pack()
    name_var = CTkEntry(signup_window)
    name_var.pack()
    CTkLabel(signup_window, text="Email:").pack()
    email_var = CTkEntry(signup_window)
    email_var.pack()
    CTkLabel(signup_window, text="Phone No.:").pack()
    phone_var = CTkEntry(signup_window)
    phone_var.pack()
    CTkLabel(signup_window, text="Password:").pack()
    password_var = CTkEntry(signup_window, show="*")
    password_var.pack()
    role_var = ctk.StringVar()
    CTkLabel(signup_window, text="Select Role:").pack()
    teacher_checkbox = CTkButton(signup_window, text="Teacher", command=lambda: handle_signup(name_var.get(), email_var.get(), phone_var.get(), role_var.get(), password_var.get(), signup_window, email_var, phone_var, role_var),
                            font=("Arial", 12), bg_color="#000000", fg_color="#3f51b5")
    teacher_checkbox.pack()
    student_checkbox = CTkButton(signup_window, text="Student", command=lambda: handle_signup(name_var.get(), email_var.get(), phone_var.get(), role_var.get(), password_var.get(), signup_window, email_var, phone_var, role_var),
                            font=("Arial", 12), bg_color="#000000", fg_color="#2ecc71")
    student_checkbox.pack()
    admin_checkbox = CTkButton(signup_window, text="Admin", command=lambda: handle_signup(name_var.get(), email_var.get(), phone_var.get(), role_var.get(), password_var.get(), signup_window, email_var, phone_var, role_var),
                            font=("Arial", 12), bg_color="#000000", fg_color="#e74c3c")
    admin_checkbox.pack()
    signup_button = CTkButton(signup_window, text="Sign Up", command=lambda: handle_signup(name_var.get(), email_var.get(), phone_var.get(), role_var.get(), password_var.get(), signup_window, email_var, phone_var, role_var), font=("Arial", 16),
                            bg_color="#000000", fg_color="#39FF14")
    # Place the signup_button 
    signup_button.pack(side=tk.TOP, pady=0.5)
# Define The inputs as global variable 
global name_var, class_var, sec_var, password_var
import customtkinter
# Function to set up the login page
def login_page():
    # create custom tkinter window
    app = customtkinter.CTk()  
    app.geometry("600x440")
    app.title('Login')

    # create a black background
    background = customtkinter.CTkFrame(master=app, width=600, height=440, corner_radius=0)
    background.place(relx=0, rely=0)

    # create custom frame
    frame = customtkinter.CTkFrame(master=background, width=320, height=360, corner_radius=15)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
    l2.place(x=50, y=45)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
    entry1.place(x=50, y=110)

    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
    entry2.place(x=50, y=165)

    forget_password_button = customtkinter.CTkButton(master=frame, text="Forget password?", command=forget_password_page)
    forget_password_button.place(x=155, y=195)

    # Create custom button
    button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
    button1.place(x=50, y=240)
    app.mainloop()
# Function to handle the "Login" button press
def button_function():
    # Function to check login credentials
    def login_check():
        name = name_var.get()
        class_ = class_var.get()
        sec = sec_var.get()
        password = password_var.get()
        if name in predefined_credentials:
            predefined_data = predefined_credentials[name]
            if (
                class_ == predefined_data.get("class", "")
                and sec == predefined_data.get("section", "")
                and password == predefined_data.get("password", "")
                ):
                show_custom_message("Login successful! You are now on the main page.", "#39FF14")
                open_main_page(predefined_data.get("role", ""))
            else:
                show_custom_message("Login Failed: Invalid credentials. Please try again.", "#FF0000")
        else:
                show_custom_message("Login Failed: User not found. Please try again.", "#FF0000")
# Function to create forget password page
def forget_password_page():
    global name_var
    forget_password_window = CTkToplevel(root)
    forget_password_window.title("Forget Password")
    forget_password_window.geometry("500x300")
    forget_password_window.grab_set()
    CTkLabel(forget_password_window, text="Forget Password", font=("Arial", 18), bg_color="#000000", fg_color="#00FFFF").pack(pady=10)
    CTkLabel(forget_password_window, text="Enter your Username:").pack()
    name_var = CTkEntry(forget_password_window)
    name_var.pack()
    # Create the "Generate OTP" button
    generate_otp_button = CTkButton(forget_password_window, text="Generate OTP", command=generate_otp, font=("Arial", 16),
                                    bg_color="#000000", fg_color="#1F51FF")
    generate_otp_button.pack(pady=20)
# Function to create forget password page
def forget_password_page():
    global name_var
    forget_password_window = CTkToplevel(root)
    forget_password_window.title("Forget Password")
    forget_password_window.geometry("500x300")
    forget_password_window.grab_set()
    CTkLabel(forget_password_window, text="Forget Password", font=("Arial", 18), bg_color="#000000", fg_color="#00FFFF").pack(pady=10)
    CTkLabel(forget_password_window, text="Enter your Username:").pack()
    name_var = CTkEntry(forget_password_window)
    name_var.pack()
    # Create the "Generate OTP" button
    generate_otp_button = CTkButton(forget_password_window, text="Generate OTP", command=generate_otp, font=("Arial", 16),
                                    bg_color="#000000", fg_color="#1F51FF")
    generate_otp_button.pack(pady=20)

# Function to generate OTP and send it to the user's email
def generate_otp():
    username = name_var.get()
    if username in predefined_credentials:
        user_data = predefined_credentials[username]
        email = user_data.get("email", "")
        if email:
            otp = generate_random_otp()
            send_otp_email(email, otp)
            show_custom_message("OTP sent to your email. Check your inbox.")
            verify_otp_page(otp, username)
        else:
            show_custom_message("Email not found for the given username.")
    else:
        show_custom_message("Username not found.")

# Function to generate a random 5-digit OTP
def generate_random_otp():
    return str(random.randint(10000, 99999))

# Function to send OTP to the user's email
def send_otp_email(email, otp):
    # Add your email configuration
    sender_email = "meetpythontest@gmail.com"
    sender_password = "Python@123!test"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    # Create the message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = email
    message["Subject"] = "OTP Verification"
    # Body of the email
    body = f"Your OTP is: {otp}"
    message.attach(MIMEText(body, "plain"))
    # Establish a connection with the SMTP server
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls(context=context)
        # Log in to your email account
        server.login(sender_email, sender_password) 
        # Send the email
        server.sendmail(sender_email, email, message.as_string())

# Function to create a GUI for email input
def get_receiver_email():
    receiver_email_window = ctk.CTkToplevel()
    receiver_email_window.title("Enter Receiver Email")
    receiver_email_window.geometry("300x150")
    receiver_email_window.grab_set()
    ctk.CTkLabel(receiver_email_window, text="Enter Receiver Email:").pack(pady=10)
    receiver_email_var = ctk.CTkEntry(receiver_email_window)
    receiver_email_var.pack(pady=10)
    # Create the "Send OTP" button
    send_otp_button = ctk.CTkButton(receiver_email_window, text="Send OTP", command=lambda: send_otp(receiver_email_var.get()),
                                    font=("Arial", 16), bg_color="#000000", fg_color="#1F51FF")
    send_otp_button.pack(pady=20)

# Function to generate a random 5-digit OTP
def generate_random_otp():
    return str(random.randint(10000, 99999))

# Function to send OTP using the entered email
def send_otp(receiver_email):
    # Add your email configuration
    sender_email = "meetpythontest@gmail.com"
    sender_password = "Python@123!test"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    # Generate OTP
    otp = generate_random_otp()
    # Send OTP email
    send_otp_email(sender_email, sender_password, smtp_server, smtp_port, receiver_email, otp)


# Function to create OTP verification page
def verify_otp_page(otp, username):
    verify_otp_window = CTkToplevel(root)
    verify_otp_window.title("Verify OTP")
    verify_otp_window.geometry("500x300")
    verify_otp_window.grab_set()
    CTkLabel(verify_otp_window, text="Verify OTP", font=("Arial", 18), bg_color="#000000", fg_color="#00FFFF").pack(pady=10)
    CTkLabel(verify_otp_window, text="Enter OTP sent to your email:").pack()
    otp_var = CTkEntry(verify_otp_window)
    otp_var.pack()
    verify_otp_button = CTkButton(verify_otp_window, text="Verify OTP", command=lambda: verify_otp(otp, otp_var.get(), username),
                            font=("Arial", 16), bg_color="#000000", fg_color="#1F51FF")
    verify_otp_button.pack(pady=20)

# Function to verify the entered OTP
def verify_otp(expected_otp, entered_otp, username):
    if expected_otp == entered_otp:
        show_custom_message("OTP Verified. Enter your new password.")
        reset_password_page(username)
    else:
        show_custom_message("Invalid OTP. Please try again.")

# Function to create password reset page
def reset_password_page(username):
    reset_password_window = CTkToplevel(root)
    reset_password_window.title("Reset Password")
    reset_password_window.geometry("500x300")
    reset_password_window.grab_set()

    CTkLabel(reset_password_window, text="Reset Password", font=("Arial", 18), bg_color="#000000", fg_color="#00FFFF").pack(pady=10)

    CTkLabel(reset_password_window, text="Enter your new password:").pack()
    new_password_var = CTkEntry(reset_password_window, show="*")
    new_password_var.pack()

    # Create the "Reset Password" button
    reset_password_button = CTkButton(reset_password_window, text="Reset Password",
                                    command=lambda: update_password(username, new_password_var.get()),
                                    font=("Arial", 16), bg_color="#000000", fg_color="#1F51FF")
    reset_password_button.pack(pady=20)

# Function to update the password in the user data
def update_password(username, new_password):
    if username in predefined_credentials:
        predefined_credentials[username]["password"] = new_password
        show_custom_message("Password updated successfully. You can now login with your new password.")
        # You may want to update the CSV file with the new password as well.
    else:
        show_custom_message("Error updating password. User not found.")

# Function to open the main page based on user's role
def open_main_page(user_role):
    if user_role == "admin":
        subprocess.run(['python', r'New APP\App\Admin_Main_Page.py'], check=True)
    elif user_role == "student":
        subprocess.run(['python', r'New APP\App\Student_Main_Page.py'], check=True)
    elif user_role == "teacher":
        subprocess.run(['python', r'New APP\App\Teacher_Main_Page.py'], check=True)
    else:
        show_custom_message("Error", "Invalid user role.", "#FF0000")

# Function to show a custom message
def show_custom_message(message, bg_color="#000000", fg_color="#87CEEB"):
    custom_message_window = tk.Toplevel()
    custom_message_window.title("Custom Message")
    custom_message_window.geometry("300x100")
    custom_message_window.grab_set()

    custom_label = CTkLabel(custom_message_window, text=message, font=("Arial", 14), bg_color=bg_color, fg_color=fg_color)
    custom_label.pack(pady=20)

    ok_button = CTkButton(custom_message_window, text="OK", command=custom_message_window.destroy,
                        font=("Arial", 12), bg_color=bg_color, fg_color=fg_color)
    ok_button.pack(pady=10)

# Create the "Sign Up" button on the main window
button_signup = CTkButton(root, text="Sign Up", command=signup_page, font=("Arial", 24),
                        bg_color="#000000", fg_color="#39FF14")
button_signup.place(relx=0.5, rely=0.4, anchor=ctk.CENTER)

# Create the "Login" button on the main window
button_login = CTkButton(root, text="Login", command=login_page, font=("Arial", 24),
                        bg_color="#000000", fg_color="#00FFFF")
button_login.place(relx=0.5, rely=0.6, anchor=ctk.CENTER)

# Start the main event loop
root.mainloop()
get_receiver_email()
login_page()