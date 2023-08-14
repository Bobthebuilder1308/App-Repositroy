import tkinter as tk
from tkinter import simpledialog, messagebox
import json

# main window
window = tk.Tk()
window.title("Teacher & Student Dashboard")
window.geometry("800x600")

neon_bg_color = "#33A1C9"

window.configure(bg=neon_bg_color)

# Initialize the student and teacher data lists
student_data_list = []
teacher_data_list = []

# Function to handle the sign-up process
def sign_up_page():
    def save_teacher_data():
        # Save teacher data to the list
        teacher_data = {
            "name": name_entry.get(),
            "email": email_entry.get(),
            "password": password_entry.get(),
            "class": class_entry.get(),
            "section": section_entry.get()
        }
        teacher_data_list.append(teacher_data)
        messagebox.showinfo("Successful Sign Up", "You will soon be able to use this feature!")

    sign_up_window = tk.Toplevel(window)
    sign_up_window.title("Sign Up")
    sign_up_window.geometry("400x400")
    sign_up_window.grab_set()

    tk.Label(sign_up_window, text="Sign Up", font=("Arial", 18)).pack(pady=10)

    tk.Label(sign_up_window, text="Name:").pack()
    name_entry = tk.Entry(sign_up_window)
    name_entry.pack()

    tk.Label(sign_up_window, text="Email:").pack()
    email_entry = tk.Entry(sign_up_window)
    email_entry.pack()

    tk.Label(sign_up_window, text="Password:").pack()
    password_entry = tk.Entry(sign_up_window, show="*")
    password_entry.pack()

    tk.Label(sign_up_window, text="Class:").pack()
    class_entry = tk.Entry(sign_up_window)
    class_entry.pack()

    tk.Label(sign_up_window, text="Section:").pack()
    section_entry = tk.Entry(sign_up_window)
    section_entry.pack()

    # Teacher sign up button
    teacher_sign_up_button = tk.Button(sign_up_window, text="Sign Up as Teacher", command=save_teacher_data,
                                       bg="deep sky blue", fg="white", font=("Arial", 16))
    teacher_sign_up_button.pack(pady=20)

# Function to handle the login process
def login_page():
    def perform_login():
        username = username_entry.get()
        password = password_entry.get()
        class_ = class_entry.get()
        section = section_entry.get()

        # P Check if the username, password, class, and section match for teachers
        for teacher in teacher_data_list:
            if (username == teacher["name"] and password == teacher["password"] and
                    class_ == teacher["class"] and section == teacher["section"]):
                login_window.destroy()
                show_teacher_dashboard()
                return

        # Placeholder: Check if the username, password, class, and section match for students
        for student in student_data_list:
            if (username == student["student_name"] and password == "123" and
                    class_ == student["class"] and section == student["section"]):
                login_window.destroy()
                show_student_dashboard()
                return

        # Invalid login
        messagebox.showerror("Login Failed", "Invalid credentials or class/section")

    global login_window
    login_window = tk.Toplevel(window)
    login_window.title("Login")
    login_window.geometry("400x400")
    login_window.grab_set()

    tk.Label(login_window, text="Login", font=("Arial", 18)).pack(pady=10)

    tk.Label(login_window, text="Username:").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password:").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    tk.Label(login_window, text="Class:").pack()
    class_entry = tk.Entry(login_window)
    class_entry.pack()

    tk.Label(login_window, text="Section:").pack()
    section_entry = tk.Entry(login_window)
    section_entry.pack()

    login_button = tk.Button(login_window, text="Login", command=perform_login,
                             bg="green", fg="white", font=("Arial", 16))
    login_button.pack(pady=20)

# Show the teacher dashboard
def show_teacher_dashboard():
    # Enable teacher-specific features
    add_students_button.config(state=tk.NORMAL)
    attendance_button.config(state=tk.NORMAL)

# Show the student dashboard
def show_student_dashboard():
    # Enable student-specific features
    my_timetable_button.config(state=tk.NORMAL)
    class_timetable_button.config(state=tk.NORMAL)
    check_grades_button.config(state=tk.NORMAL)
    announcements_button.config(state=tk.NORMAL)

# Sign Up and Login Buttons
sign_up_button = tk.Button(window, text="Sign Up", command=sign_up_page,
                           bg="purple", fg="white", font=("Arial", 16))
sign_up_button.pack(pady=20)

login_button = tk.Button(window, text="Login", command=login_page,
                         bg="green", fg="white", font=("Arial", 16))
login_button.pack(pady=20)

# Function to show the main dashboard for teachers
def show_teacher_dashboard():
    main_window = tk.Toplevel(window)
    main_window.title("Teacher Dashboard")
    main_window.geometry("800x600")
    main_window.configure(bg=neon_bg_color)

    tk.Label(main_window, text="Welcome, Teacher!", font=("Arial", 18), bg=neon_bg_color).pack(pady=10)

    # Buttons for teacher-specific features
    add_students_button = tk.Button(main_window, text="Add Students", command=add_students_page,
                                    bg="purple", fg="white", font=("Arial", 16))
    add_students_button.pack(pady=20)

    attendance_button = tk.Button(main_window, text="Attendance", command=attendance_page,
                                  bg="green", fg="white", font=("Arial", 16))
    attendance_button.pack(pady=20)

# Function to show the main dashboard for students
def show_student_dashboard():
    main_window = tk.Toplevel(window)
    main_window.title("Student Dashboard")
    main_window.geometry("800x600")
    main_window.configure(bg=neon_bg_color)

    tk.Label(main_window, text="Welcome, Student!", font=("Arial", 18), bg=neon_bg_color).pack(pady=10)

    # Buttons for student-specific features
    my_timetable_button = tk.Button(main_window, text="My Timetable", command=lambda: messagebox.showinfo("My Timetable", "Your timetable will be available soon."),
                                    bg="purple", fg="white", font=("Arial", 16))
    my_timetable_button.pack(pady=20)

    class_timetable_button = tk.Button(main_window, text="Class Timetable", command=lambda: messagebox.showinfo("Class Timetable", "Class timetable will be available soon."),
                                       bg="green", fg="white", font=("Arial", 16))
    class_timetable_button.pack(pady=20)

    check_grades_button = tk.Button(main_window, text="Check Student Grades", command=lambda: messagebox.showinfo("Check Student Grades", "Check grades here."),
                                    bg="purple", fg="white", font=("Arial", 16))
    check_grades_button.pack(pady=20)

    announcements_button = tk.Button(main_window, text="Announcements", command=lambda: messagebox.showinfo("Announcements", "No announcements at the moment."),
                                     bg="green", fg="white", font=("Arial", 16))
    announcements_button.pack(pady=20)
student_data_list.append({
    "student_name": "Joey", "father_name": "Joey Sr.", "mother_name": "Gloria",
    "dob": "1971-05-11", "blood_group": "B+", "gender": "Male", "roll_no": "202", "class": "11", "section": "A",
    "attendance": "Present"
})

student_data_list.append({
    "student_name": "Harry", "father_name": "James", "mother_name": "Lily",
    "dob": "1980-07-31", "blood_group": "A+", "gender": "Male", "roll_no": "203", "class": "11", "section": "A",
    "attendance": "Present"
})

student_data_list.append({
    "student_name": "Chotta Bheem", "father_name": "Raju", "mother_name": "Kunti",
    "dob": "2004-01-01", "blood_group": "O+", "gender": "Male", "roll_no": "204", "class": "11", "section": "A",
    "attendance": "Present"
})

student_data_list.append({
    "student_name": "Tuntun Mausi", "father_name": "Unknown", "mother_name": "Unknown",
    "dob": "1950-01-01", "blood_group": "Unknown", "gender": "Female", "roll_no": "205", "class": "11", "section": "A",
    "attendance": "Present"
})

student_data_list.append({
    "student_name": "Light Yagami", "father_name": "Soichiro", "mother_name": "Sachiko",
    "dob": "1986-02-28", "blood_group": "A-", "gender": "Male", "roll_no": "206", "class": "11", "section": "A",
    "attendance": "Present"
})

# Start the main event loop
window.mainloop()
