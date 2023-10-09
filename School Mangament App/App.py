import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess
import webbrowser

# Create the main window
window = tk.Tk()
window.title("Teacher & Student Dashboard")
window.geometry("800x600")
bright_bg_color = "#FFFF99"

# Background color for the main window
window.configure(bg="#FFFF33")

# Predefined login credentials
predefined_credentials = {
    "John": {"class": "11", "section": "A", "password": "123", "role": "teacher"},
    "Jane": {"class": "10", "section": "B", "password": "456", "role": "student"},
    "Meet": {"class": "11", "section": "A", "password": "122", "role": "student"},
    "Admin": {"password": "admin", "role": "admin"},
    "announcements": []
}

# Function to show teacher or student options
def show_teacher_student_options():
    def open_google():
        webbrowser.open("https://www.google.com")

    custom_dialog = tk.Toplevel(window)
    custom_dialog.title("Sign Up Options")
    custom_dialog.geometry("400x200")
    custom_dialog.grab_set()

    teacher_button = tk.Button(custom_dialog, text="Teacher", command=open_google,
                               bg="lime green", fg="white", font=("Arial", 16))
    teacher_button.pack(pady=10)

    student_button = tk.Button(custom_dialog, text="Student", command=open_google,
                               bg="deep sky blue", fg="white", font=("Arial", 16))
    student_button.pack(pady=10)

# Create the "Sign Up" button on the main window
button_signup = tk.Button(window, text="Sign Up", command=show_teacher_student_options,
                          bg="lime green", fg="white", font=("Arial", 24))
button_signup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

def login_page():
    login_window = tk.Toplevel(window)
    login_window.title("Login")
    login_window.geometry("400x400")
    login_window.grab_set()

    tk.Label(login_window, text="Login", font=("Arial", 18)).pack(pady=10)
    tk.Label(login_window, text="Name:").pack()
    name_entry = tk.Entry(login_window)
    name_entry.pack()
    tk.Label(login_window, text="Class:").pack()
    class_entry = tk.Entry(login_window)
    class_entry.pack()
    tk.Label(login_window, text="Section:").pack()
    sec_entry = tk.Entry(login_window)
    sec_entry.pack()
    tk.Label(login_window, text="Password:").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    def login_check():
        name = name_entry.get()
        class_ = class_entry.get()
        sec = sec_entry.get()
        password = password_entry.get()

        if name in predefined_credentials:
            predefined_data = predefined_credentials[name]
            if (class_ == predefined_data.get("class", "") and
                sec == predefined_data.get("section", "") and
                password == predefined_data.get("password", "")):
                messagebox.showinfo("Login", "Login successful! You are now on the main page.")
                open_main_page(predefined_data.get("role", ""))
            else:
                messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
        else:
            messagebox.showerror("Login Failed", "User not found. Please try again.")

    login_button = tk.Button(login_window, text="Login", command=login_check,
                             bg="#FF0000", fg="white", font=("Arial", 16))
    login_button.pack(pady=20)

# Function to open the main page based on user's role
def open_main_page(user_role):
    if user_role == "teacher":
        subprocess.run(['python', r'D:\School Mangament App\Teacher_main_page.py'], check=True)
    elif user_role == "student":
        subprocess.run(['python', r'D:\School Mangament App\Student_main.py'], check=True)
    elif user_role == "admin":
        subprocess.run(['python', r'D:\School Mangament App\Admin_main.py'], check=True)
    else:
        messagebox.showerror("Error", "Invalid user role.")

# Create the "Login" button on the main window
button_login = tk.Button(window, text="Login", command=login_page,
                          bg="#87CEEB", fg="white", font=("Arial", 24))
button_login.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Function to close a window
def close_window(window):
    window.destroy()

# Start the main event loop
window.mainloop()
