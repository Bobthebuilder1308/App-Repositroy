#Teacher Main Page
import customtkinter as ctk
from customtkinter import CTkButton, CTkToplevel, CTkLabel
import webbrowser
import os
import subprocess
import tkinter as tk

# Create the main window
window = ctk.CTk()
window.title("Teacher Dashboard")
window.geometry("200x535")
window.configure(bg="skyblue1")

# Initialize user role
user_role = None

# Predefined login credentials
predefined_credentials = {
    "John": {"class": "11", "section": "A", "password": "123", "role": "teacher"},
}

def open_announcement_handler():
    subprocess.run(['python', r'New APP\App\global announcement .py'], check=True)

# Create a directory to store uploaded assignments
upload_dir = os.path.expanduser("~")

# Function to handle assignment upload by the teacher
def upload_assignment():
    file_path = ctk.filedialog.asksaveasfilename(
        title="Upload Assignment",
        filetypes=[("PDF Files", "*.pdf"), ("PNG Files", "*.png")]
    )
    if file_path:
        if file_path.endswith((".pdf", ".png")):
            assignment_filename = os.path.basename(file_path)
            save_path = os.path.join("Assignments", assignment_filename)
            os.makedirs(os.path.dirname(save_path), exist_ok=True)
            os.replace(file_path, save_path)
            instruction = ctk.simpledialog.askstring(
                "Assignment Instructions",
                "Enter assignment instructions (optional):"
            )
            if instruction:
                tk.messagebox.showinfo("Assignment Instructions", instruction)
            else:
                tk.messagebox.showinfo(
                    "Assignment Instructions",
                    "No additional instructions provided."
                )
        else:
            tk.messagebox.showerror(
                "Invalid File",
                "Only PDF and PNG files are allowed."
            )

def view_global_announcement():
    subprocess.run(['python', r'New APP\App\View Global Announcement.py'], check=True)

def view_admin_announcement():
    subprocess.run(['python', r'New APP\App\view_admin_announcement.py'], check=True)

def show_teacher_options():
    def on_announcements():
        open_announcement_handler()

    def on_my_timetable():
        my_timetable_page()

    def on_create_test():
        create_test()

    def on_check_grade():
        check_grade()

    def view_announcement():
        view_global_announcement()

    button_width = 16
    button_height = 3

    announcements_button = CTkButton(
        window,
        text="Announcements",
        command=on_announcements,
        font=("Arial", 16),
        width=button_width,
        height=button_height
    )
    announcements_button.grid(row=1, column=1)

    my_timetable_button = CTkButton(
        window,
        text="My Timetable",
        command=on_my_timetable,
        font=("Arial", 16),
        width=button_width,
        height=button_height
    )
    my_timetable_button.grid(row=4, column=1)

    create_test_button = CTkButton(
        window,
        text="Create Test",
        command=on_create_test,
        font=("Arial", 16),
        width=button_width,
        height=button_height
    )
    create_test_button.grid(row=7, column=1)

    check_grade_button = CTkButton(
        window,
        text='''Check
Student
Grade''',
        command=on_check_grade,
        font=("Arial", 16),
        width=button_width,
        height=button_height
    )
    check_grade_button.grid(row=11, column=1)

    assignments_button = CTkButton(
        window,
        text="Assignments",
        command=upload_assignment,
        font=("Arial", 16),
        width=button_width,
        height=button_height
    )
    assignments_button.grid(row=14, column=1)

    announcement_button = CTkButton(
        window,
        text="View Global Announcement",
        command=view_announcement,
        font=("Arial", 16),
        width=16,
        height=3
    )
    announcement_button.grid(row=23, column=1)

    # Add a button for viewing admin announcements
    view_admin_announcement_button = CTkButton(
        window,
        text="View Admin Announcement",
        command=view_admin_announcement,
        font=("Arial", 16),
        width=button_width,
        height=button_height
    )
    view_admin_announcement_button.grid(row=20, column=1)

# Function For Teacher's Create Test
def create_test():
    webbrowser.open("https://quizizz.com/?lng=en")

# Function for Teacher's Assignments Page
def teacher_assignments_page():
    assignments_window = CTkToplevel(master=window)
    assignments_window.title("Teacher's Assignments")
    assignments_window.geometry("800x600")
    assignments_window.configure(bg="light green")
    assignments_window.grab_set()
    CTkLabel(assignments_window, text="Teacher's Assignments", font=("Arial", 18), bg="light green").pack(pady=10)

# Function to check student grade
def check_grade():
    tk.messagebox.showinfo("Work in Progress", "Feature coming soon.")

# Function for My Timetable Page
def my_timetable_page():
    message_box = ctk.CTkToplevel()
    message_box.title("Work in Progress")
    message_box.geometry("300x100")
    message_label = ctk.CTkLabel(message_box, text="Feature coming soon.", font=("Arial", 14))
    message_label.pack(pady=20)
    ok_button = ctk.CTkButton(message_box, text="OK", command=message_box.destroy)
    ok_button.pack()
    message_box.update_idletasks()
    x = (message_box.winfo_screenwidth() - message_box.winfo_reqwidth()) / 2
    y = (message_box.winfo_screenheight() - message_box.winfo_reqheight()) / 2
    message_box.geometry(f"+{int(x)}+{int(y)}")

'''# Define the send_email function at the global scope
def send_email(subject, body, to):
    from_email = 'meetpythontest@gmail.com'
    from_password = 'Python@123!test'
    send_email = 'meetchangela1308@gmail.com'
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to, msg.as_string())
    server.quit()
'''
# Show teacher options 
show_teacher_options()

# Start the main event loop
window.mainloop()
