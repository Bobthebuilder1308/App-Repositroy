import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# Create the main window
window = tk.Tk()
window.title("Teacher & Student Dashboard")
window.geometry("800x600")

# Bright background color Hopefully
bright_bg_color = "#FFFF99"

#background color for the main window
window.configure(bg="#FFFF33")

# Initialize the create_class_button
create_class_button = None

# Predefined login credentials
predefined_credentials = {
    "John": {"class": "11", "section": "A", "password": "123"},
    "Jane": {"class": "10", "section": "B", "password": "456"}
}

# Function to show teacher or student options
def show_teacher_student_options():
    def on_teacher():
        teacher_account_creation()

    def on_student():
        # Implement student sign-up here
        pass

    custom_dialog = tk.Toplevel(window)
    custom_dialog.title("Sign Up Options")
    custom_dialog.geometry("400x200")
    custom_dialog.grab_set()

    teacher_button = tk.Button(custom_dialog, text="Teacher", command=on_teacher,
                               bg="lime green", fg="white", font=("Arial", 16))
    teacher_button.pack(pady=20)

    student_button = tk.Button(custom_dialog, text="Student", command=on_student,
                               bg="deep sky blue", fg="white", font=("Arial", 16))
    student_button.pack()

# Create the Sign Up button
button_signup = tk.Button(window, text="Sign Up", command=show_teacher_student_options,
                          bg="lime green", fg="white", font=("Arial", 24))
button_signup.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

# Create the Login button
button_login = tk.Button(window, text="Login", command=lambda: login_page(),
                         bg="deep sky blue", fg="white", font=("Arial", 24))
button_login.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

# Function for the login page
def login_page():
    def login_check():
        # Implement login check based on name, class, sec, and password
        name = name_entry.get()
        class_ = class_entry.get()
        sec = sec_entry.get()
        password = password_entry.get()

        # Check if the name exists in predefined_credentials
        if name in predefined_credentials:
            # Get the predefined credentials for the name
            predefined_data = predefined_credentials[name]
            
            # Check if the provided class, section, and password match
            if (class_ == predefined_data["class"] and
                sec == predefined_data["section"] and
                password == predefined_data["password"]):

                # Login successful, navigate to the main page
                messagebox.showinfo("Login", "Login successful! You are now on the main page.")
                main_page()
            else:
                # Login failed, show an error message
                messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
        else:
            # Name not found, show an error message
            messagebox.showerror("Login Failed", "User not found. Please try again.")

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

    login_button = tk.Button(login_window, text="Login", command=login_check,
                             bg="#FF0000", fg="white", font=("Arial", 16))
    login_button.pack(pady=20)

# Function for Main Page (after login)
def main_page():
    main_window = tk.Toplevel(window)
    main_window.title("Main Page")
    main_window.geometry("800x600")
    main_window.configure(bg=bright_bg_color)
    main_window.grab_set()

    tk.Label(main_window, text="Main Page", font=("Arial", 18), bg=bright_bg_color).pack(pady=10)

    my_class_button = tk.Button(main_window, text="My Class", command=add_students_page,
                                bg="lime green", fg="white", font=("Arial", 24))
    my_class_button.place(relx=0.2, rely=0.3, anchor=tk.CENTER)

    class_timetable_button = tk.Button(main_window, text="Class Timetable", command=class_timetable_page,
                                      bg="lime green", fg="white", font=("Arial", 24))
    class_timetable_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    my_timetable_button = tk.Button(main_window, text="My Timetable", command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                    bg="deep sky blue", fg="white", font=("Arial", 24))
    my_timetable_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)

    create_test_button = tk.Button(main_window, text="Create Test", command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                   bg="deep sky blue", fg="white", font=("Arial", 24))
    create_test_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    check_grade_button = tk.Button(main_window, text="Check Student Grade", command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                   bg="deep sky blue", fg="white", font=("Arial", 24))
    check_grade_button.place(relx=0.2, rely=0.7, anchor=tk.CENTER)

# Function for Add Students Page
def add_students_page():
    def save_student_data():
        student_data = {
            "student_name": student_name_entry.get(),
            "father_name": father_name_entry.get(),
            "mother_name": mother_name_entry.get(),
            "dob": dob_entry.get(),
            "blood_group": blood_group_entry.get(),
            "gender": gender_entry.get(),
            "roll_no": roll_no_entry.get(),
            "class": class_entry.get(),
            "section": section_entry.get(),
        }
        # Save student data to a file or database
        with open("student_data.json", "a") as file:
            json.dump(student_data, file)
            file.write("\n")
        messagebox.showinfo("Student Added", "Student data saved successfully!")

    add_students_window = tk.Toplevel(window)
    add_students_window.title("Add Students")
    add_students_window.geometry("400x600")
    add_students_window.configure(bg=bright_bg_color)
    add_students_window.grab_set()

    tk.Label(add_students_window, text="Add Students", font=("Arial", 18), bg=bright_bg_color).pack(pady=10)

    tk.Label(add_students_window, text="Student Name:").pack()
    student_name_entry = tk.Entry(add_students_window)
    student_name_entry.pack()

    tk.Label(add_students_window, text="Father Name:").pack()
    father_name_entry = tk.Entry(add_students_window)
    father_name_entry.pack()

    tk.Label(add_students_window, text="Mother Name:").pack()
    mother_name_entry = tk.Entry(add_students_window)
    mother_name_entry.pack()

    tk.Label(add_students_window, text="D.O.B:").pack()
    dob_entry = tk.Entry(add_students_window)
    dob_entry.pack()

    tk.Label(add_students_window, text="Blood Group:").pack()
    blood_group_entry = tk.Entry(add_students_window)
    blood_group_entry.pack()

    tk.Label(add_students_window, text="Gender:").pack()
    gender_entry = tk.Entry(add_students_window)
    gender_entry.pack()

    tk.Label(add_students_window, text="Roll No:").pack()
    roll_no_entry = tk.Entry(add_students_window)
    roll_no_entry.pack()

    tk.Label(add_students_window, text="Class:").pack()
    class_entry = tk.Entry(add_students_window)
    class_entry.pack()

    tk.Label(add_students_window, text="Section:").pack()
    section_entry = tk.Entry(add_students_window)
    section_entry.pack()

    save_button = tk.Button(add_students_window, text="Save", command=save_student_data,
                            bg="#008000", fg="white", font=("Arial", 16))
    save_button.pack(pady=20)

# Function for Class Timetable Page
def class_timetable_page():
    def save_class_timetable():
        # Implement saving class timetable
        pass

    class_timetable_window = tk.Toplevel(window)
    class_timetable_window.title("Class Timetable")
    class_timetable_window.geometry("800x600")
    class_timetable_window.configure(bg=bright_bg_color)
    class_timetable_window.grab_set()

    tk.Label(class_timetable_window, text="Class Timetable", font=("Arial", 18), bg=bright_bg_color).pack(pady=10)

    # ... (add widgets for class timetable, and a button to save)

    save_button = tk.Button(class_timetable_window, text="Save Timetable", command=save_class_timetable,
                            bg="#008000", fg="white", font=("Arial", 16))
    save_button.pack(pady=20)

# Start the main event loop
window.mainloop()
