import tkinter as tk
from tkinter import simpledialog, messagebox
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
    "announcements": []
}

# Function to show teacher or student options
def show_teacher_student_options():
    def on_teacher():
        teacher_account_creation()

    def on_student():
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
        name = name_entry.get()
        class_ = class_entry.get()
        sec = sec_entry.get()
        password = password_entry.get()

        if name in predefined_credentials:
            predefined_data = predefined_credentials[name]
            if (class_ == predefined_data["class"] and
                sec == predefined_data["section"] and
                password == predefined_data["password"]):
                messagebox.showinfo("Login", "Login successful! You are now on the main page.")
                main_page(predefined_data)
            else:
                messagebox.showerror("Login Failed", "Invalid credentials. Please try again.")
        else:
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
    # Close the login window when done
    login_window.protocol("WM_DELETE_WINDOW", lambda: close_window(login_window))
    # Function to close a window
def close_window(window):
    window.destroy()

# Function for Main Page (after login)
def main_page(user_data):
    # Create the main page window
    main_window = tk.Toplevel(window)
    main_window.title("Main Page")
    main_window.geometry("800x600")
    main_window.configure(bg="khaki1")
    main_window.grab_set()

    tk.Label(main_window, text="Main Page", font=("Arial", 18), bg="lime green").pack(pady=10)

    # Check the user's role to determine available actions
    if user_data["role"] == "teacher":
        announcement_button = tk.Button(main_window, text="Announcements", command=teacher_announcement_page,
                                        bg="firebrick1", fg="blue", font=("Arial", 24))
        announcement_button.place(relx=0.2, rely=0.3, anchor=tk.CENTER)

        my_timetable_button = tk.Button(main_window, text="My Timetable",
                                       command=my_timetable_page,
                                       bg="cyan3", fg="white", font=("Arial", 24))
        my_timetable_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        class_timetable_button = tk.Button(main_window, text="Class Timetable",
                                           command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                           bg="pink", fg="white", font=("Arial", 24))
        class_timetable_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        create_test_button = tk.Button(main_window, text="Create Test",
                                       command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                       bg="light cyan", fg="white", font=("Arial", 24))
        create_test_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        check_grade_button = tk.Button(main_window, text="Check Student Grade",
                                       command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                       bg="red4", fg="white", font=("Arial", 24))
        check_grade_button.place(relx=0.2, rely=0.7, anchor=tk.CENTER)
        assignments_button = tk.Button(main_window, text="Assignments",
                                       command=teacher_assignments_page,
                                       bg="lawn green", fg="white", font=("Arial", 24))
        assignments_button.place(relx=0.5, rely=0.7, anchor=tk.CENTER)
    else:
        announcements_button = tk.Button(main_window, text="Announcements",
                                         command=student_announcement_page,
                                         bg="firebrick1", fg="white", font=("Arial", 24))
        announcements_button.place(relx=0.2, rely=0.3, anchor=tk.CENTER)
        assignments_button = tk.Button(main_window, text="Assignments",
                                       command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                       bg="red2", fg="white", font=("Arial", 24))
        assignments_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        see_grade_button = tk.Button(main_window, text="See My Grade",
                                     command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                     bg="green3", fg="white", font=("Arial", 24))
        see_grade_button.place(relx=0.2, rely=0.5, anchor=tk.CENTER)
        test_button = tk.Button(main_window, text="Test",
                                command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                bg="steelblue1", fg="white", font=("Arial", 24))
        test_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        timetable_button = tk.Button(main_window, text="Timetable",
                                     command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                                     bg="deep sky blue", fg="white", font=("Arial", 24))
        timetable_button.place(relx=0.2, rely=0.7, anchor=tk.CENTER)
    profile_button = tk.Button(main_window, text="Profile",
                               command=lambda: messagebox.showinfo("Work in Progress", "Feature coming soon."),
                               bg="deepskyblue2", fg="white", font=("Arial", 24))
    profile_button.place(relx=0.85, rely=0.05, anchor=tk.CENTER)

# Function for Quiz Page
def create_test():
    webbrowser.open("https://quizizz.com/?lng=en")

# Function For Timetable Page
def my_timetable_page():
    timetable_window = tk.Toplevel(window)
    timetable_window.title("My Timetable")
    timetable_window.geometry("800x600")
    timetable_window.configure(bg="white")
    timetable_window.grab_set()
    class TimetableApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Timetable App")
            self.timetable_data = {}
            self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
            self.periods = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
            self.subject_colors = {
                    "Maths": "#FF6AFF",
                    "Physics": "#00FFFF",
                    "Chemistry": "#00FF00",
                    "Biology": "#FFD700",  
                    "CS": "#FF1493"
                    #"English":"steelblue"
            }
            self.button_frame = tk.Frame(root)
            self.button_frame.pack(pady=10)
            self.add_button = tk.Button(self.button_frame, text="Add Entry", command=self.add_entry)
            self.add_button.pack(side=tk.LEFT, padx=10)
            self.edit_button = tk.Button(self.button_frame, text="Edit Entry", command=self.edit_entry)
            self.edit_button.pack(side=tk.LEFT, padx=10)
            self.display_button = tk.Button(self.button_frame, text="Display Timetable", command=self.display_timetable)
            self.display_button.pack(side=tk.LEFT, padx=10)
            self.timetable_frame = tk.Frame(root)
            self.timetable_frame.pack()
            for i, day in enumerate(self.days):
                tk.Label(self.timetable_frame, text=day.capitalize(), padx=10, pady=5, relief=tk.RIDGE, width=12).grid(row=0, column=i+1)
            for j, period in enumerate(self.periods):
                tk.Label(self.timetable_frame, text=period, padx=10, pady=5, relief=tk.RIDGE, width=6).grid(row=j+1, column=0)
            for i, day in enumerate(self.days):
                for j, period in enumerate(self.periods):
                    label = tk.Label(self.timetable_frame, textvariable=self.get_subject_var(day, period), padx=10, pady=5, relief=tk.RIDGE, width=12)
                    label.grid(row=j+1, column=i+1)
                    label.config(bg="spring green", fg="skyblue")

        def get_subject_var(self, day, period):
            return tk.StringVar(value=self.timetable_data.get(day, {}).get(period, "-----"))

        def add_entry(self):
            day = simpledialog.askstring("Add Entry", "Enter the day (1-6):")
            period = simpledialog.askstring("Add Entry", "Enter the period (1-9):")
            if day and period:
                subject = self.choose_subject()
                if subject is not None:
                    day = int(day) - 1
                    period = int(period) - 1
                    if 0 <= day < len(self.days) and 0 <= period < len(self.periods):
                        if self.days[day] not in self.timetable_data:
                            self.timetable_data[self.days[day]] = {}
                        self.timetable_data[self.days[day]][self.periods[period]] = subject
                        messagebox.showinfo("Success", "Entry added successfully!")
                        self.update_timetable()
                    else:
                        messagebox.showerror("Error", "Invalid day or period.")
            else:
                messagebox.showerror("Error", "All fields are required.")

        def choose_subject(self):
            subject_choice = tk.StringVar(value=list(self.subject_colors.keys())[0])
            subject_menu = tk.OptionMenu(self.root, subject_choice, *self.subject_colors.keys())
            subject_menu.pack()
            ok_button = tk.Button(self.root, text="OK", command=lambda: subject_menu.destroy())
            ok_button.pack()
            self.root.wait_window(subject_menu)
            subject = subject_choice.get()
            return subject

        def update_timetable(self):
            for i, day in enumerate(self.days):
                for j, period in enumerate(self.periods):
                    label = tk.Label(self.timetable_frame, textvariable=self.get_subject_var(day, period), padx=10, pady=5, relief=tk.RIDGE, width=12)
                    label.grid(row=j+1, column=i+1)
                    subject = self.timetable_data.get(day, {}).get(period, "-----")
                    label.config(bg=self.subject_colors.get(subject, "lightgray"), fg="white")

        def edit_entry(self):
            day = simpledialog.askstring("Edit Entry", "Enter the day (1-6):")
            period = simpledialog.askstring("Edit Entry", "Enter the period (1-9):")
            if day and period:
                day = int(day) - 1
                period = int(period) - 1
                if 0 <= day < len(self.days) and 0 <= period < len(self.periods):
                    if self.days[day] in self.timetable_data and self.periods[period] in self.timetable_data[self.days[day]]:
                        new_subject = self.choose_subject()
                        if new_subject is not None:
                            self.timetable_data[self.days[day]][self.periods[period]] = new_subject
                            messagebox.showinfo("Success", "Entry edited successfully!")
                            self.update_timetable()
                    else:
                        messagebox.showerror("Error", "Entry not found.")
                else:
                    messagebox.showerror("Error", "Invalid day or period.")
            else:
                messagebox.showerror("Error", "Day and period are required.")

        def display_timetable(self):
            if not self.timetable_data:
                messagebox.showinfo("Timetable", "No entries to display.")
            else:
                timetable_text = ""
                for day in self.days:
                    timetable_text += f"{day.capitalize()}:\n"
                    for period in self.periods:
                        subject = self.timetable_data.get(day, {}).get(period, "-----")
                        timetable_text += f"  {period} - {subject}\n"
                messagebox.showinfo("Timetable", timetable_text)
                def main():
                    root = tk.Tk()
                    app = TimetableApp(root)
                    root.mainloop()
                if __name__ == "__main__":
                     main()
  

# Function for Teacher's Announcement Page
def teacher_announcement_page():
    announcement_window = tk.Toplevel(window)
    announcement_window.title("Teacher's Announcements")
    announcement_window.geometry("800x600")
    announcement_window.configure(bg="light green")
    announcement_window.grab_set()

    tk.Label(announcement_window, text="Teacher's Announcements", font=("Arial", 18), bg="light green").pack(pady=10)

    announcements = predefined_credentials["announcements"]
    for announcement in announcements:
        tk.Label(announcement_window, text=announcement, font=("Arial", 12), bg="light green").pack(pady=5)

    add_announcement_button = tk.Button(announcement_window, text="Add Announcement", command=add_announcement_page,
                                        bg="firebrick1", fg="blue", font=("Arial", 16))
    add_announcement_button.pack(pady=20)

# Function for Student's Announcement Page
def student_announcement_page():
    announcement_window = tk.Toplevel(window)
    announcement_window.title("Student's Announcements")
    announcement_window.geometry("800x600")
    announcement_window.configure(bg="light blue")
    announcement_window.grab_set()

    tk.Label(announcement_window, text="Student's Announcements", font=("Arial", 18), bg="light blue").pack(pady=10)

    announcements = predefined_credentials["announcements"]
    for announcement in announcements:
        tk.Label(announcement_window, text=announcement, font=("Arial", 12), bg="light blue").pack(pady=5)

# Function to save an announcement
def save_announcement(announcement_text):
    # Save the announcement to a file or database (to be implemented)
    print("Announcement saved:", announcement_text)

# Function for Teacher's Assignments Page
def teacher_assignments_page():
    # Create the teacher's assignments page window
    assignments_window = tk.Toplevel(window)
    assignments_window.title("Teacher's Assignments")
    assignments_window.geometry("800x600")
    assignments_window.configure(bg="light green")
    assignments_window.grab_set()

    tk.Label(assignments_window, text="Teacher's Assignments", font=("Arial", 18), bg="light green").pack(pady=10)
    assignments = predefined_credentials.get("teacher_assignments", [])
    for assignment in assignments:
        tk.Label(assignments_window, text=assignment, font=("Arial", 12), bg="light green").pack(pady=5)

# Function to add an announcement
def add_announcement_page():
    def save_announcement(announcement_text, window):
        predefined_credentials["announcements"].append(announcement_text)
        window.destroy()

    add_announcement_window = tk.Toplevel(window)
    add_announcement_window.title("Add Announcement")
    add_announcement_window.geometry("800x600")
    add_announcement_window.configure(bg="light yellow")
    add_announcement_window.grab_set()

    tk.Label(add_announcement_window, text="Add Announcement", font=("Arial", 18), bg="red").pack(pady=10)

    tk.Label(add_announcement_window, text="Announcement (200 words limit):").pack(pady=10)
    announcement_entry = tk.Text(add_announcement_window, height=10, width=50)
    announcement_entry.pack(pady=10)

    save_button = tk.Button(add_announcement_window, text="Save Announcement",
                            command=lambda: save_announcement(announcement_entry.get(1.0, tk.END), add_announcement_window),
                            bg="firebrick1", fg="blue", font=("Arial", 16))
    save_button.pack(pady=20)

# Start the main event loop
window.mainloop()
