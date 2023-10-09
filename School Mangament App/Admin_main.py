import tkinter as tk
from tkinter import simpledialog, messagebox
import subprocess

# Create the Admin main page window
admin_window = tk.Tk()
admin_window.title("Admin Main Page")
admin_window.geometry("800x600")
admin_window.configure(bg="light blue")
admin_window.grab_set()
# Define a function to open the admin timetable
def open_admin_timetable():
    try:
        subprocess.run(['python', 'admin_timetable.py'], check=True)
    except FileNotFoundError:
        messagebox.showerror("Error", "Admin timetable code file not found.")

# Create a button to open the admin timetable
admin_timetable_button = tk.Button(admin_window, text="Open Admin Timetable", command=open_admin_timetable,
                                   bg="blue", fg="white", font=("Arial", 18))
admin_timetable_button.place(relx=0.5, rely=0.2, anchor=tk.CENTER)


# Define functions for buttons
def open_announcements_page():
    announcements_page = tk.Toplevel(admin_window)
    announcements_page.title("Announcements Page")

    def add_admin_announcement():
        announcement = simpledialog.askstring("Add Admin Announcement", "Enter Admin Announcement:")
        if announcement:
            announcements["admin"].append(announcement)
            messagebox.showinfo("Announcement Added", "Admin Announcement added successfully!")

    def add_student_announcement():
        announcement = simpledialog.askstring("Add Student Announcement", "Enter Student Announcement:")
        if announcement:
            announcements["student"].append(announcement)
            messagebox.showinfo("Announcement Added", "Student Announcement added successfully!")

    def view_student_announcements():
        announcements_text = "\n".join(announcements["student"])
        messagebox.showinfo("Student Announcements", announcements_text)

    def view_admin_announcements():
        announcements_text = "\n".join(announcements["admin"])
        messagebox.showinfo("Admin Announcements", announcements_text)

    add_admin_button = tk.Button(announcements_page, text="Add Admin Announcement", command=add_admin_announcement)
    add_admin_button.pack()

    add_student_button = tk.Button(announcements_page, text="Add Student Announcement", command=add_student_announcement)
    add_student_button.pack()

    view_student_button = tk.Button(announcements_page, text="View Student Announcements", command=view_student_announcements)
    view_student_button.pack()

    view_admin_button = tk.Button(announcements_page, text="View Admin Announcements", command=view_admin_announcements)
    view_admin_button.pack()

# Create a button to open the announcements page
announcements_button = tk.Button(admin_window, text="Announcements", command=open_announcements_page,
                                bg="blue", fg="white", font=("Arial", 18))
announcements_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

# Initialize the announcements dictionary
announcements = {
    "admin": [],
    "student": []
}
def button2_action():
    pass

def button3_action():
    pass

def button4_action():
    pass

def button5_action():
    pass

def button6_action():
    pass

# Create the other buttons
button2 = tk.Button(admin_window, text="Button 2", command=button2_action,
                    bg="blue", fg="white", font=("Arial", 18))
button2.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

button3 = tk.Button(admin_window, text="Button 3", command=button3_action,
                    bg="blue", fg="white", font=("Arial", 18))
button3.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

button4 = tk.Button(admin_window, text="Button 4", command=button4_action,
                    bg="blue", fg="white", font=("Arial", 18))
button4.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

button5 = tk.Button(admin_window, text="Button 5", command=button5_action,
                    bg="blue", fg="white", font=("Arial", 18))
button5.place(relx=0.5, rely=0.7, anchor=tk.CENTER)

button6 = tk.Button(admin_window, text="Button 6", command=button6_action,
                    bg="blue", fg="white", font=("Arial", 18))
button6.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

# Start the main event loop for the Admin main page
admin_window.mainloop()