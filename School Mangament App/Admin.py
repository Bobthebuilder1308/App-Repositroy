import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import subprocess
import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create an empty list to store announcements
global_announcements = []
admin_announcements = []

def open_announcement_editor(is_global):
    def save_announcement(announcement_text):
        if is_global:
            global_announcements.append(announcement_text)
        else:
            admin_announcements.append(announcement_text)
        save_to_csv()
        announcement_editor_window.destroy()

    def send_announcement_email(announcement_text):
        recipient_email = "meetchangela1308@gmail.com"

        subject = 'Announcement'
        send_email(subject, announcement_text, recipient_email)

        save_announcement(announcement_text)

    def save_to_csv():
        with open('global_announcements.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([announcement for announcement in global_announcements])

        with open('admin_announcements.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([announcement for announcement in admin_announcements])

    def send_email(subject, body, to_email):
        email = 'meetpythontest@gmail.com'
        password = 'YourAppPasswordHere'  # Replace with your app password

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login(email, password)

        message = MIMEMultipart()
        message['From'] = email
        message['To'] = to_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        smtp.sendmail(email, to_email, message.as_string())
        smtp.quit()

    announcement_editor_window = tk.Toplevel()
    announcement_editor_window.title("Announcement Editor")
    announcement_editor_window.geometry("600x400")
    announcement_editor_window.configure(bg="light green")

    announcement_entry = tk.Text(announcement_editor_window, height=10, width=40)
    announcement_entry.pack(pady=20)

    send_on_app_button = tk.Button(announcement_editor_window, text="Send Announcement On App", bg="blue", fg="white", width=20, height=2, command=lambda: save_announcement(announcement_entry.get("1.0", "end-1c")))
    send_on_app_button.pack(pady=10)

    send_through_email_button = tk.Button(announcement_editor_window, text="Send Announcement Through Email", bg="blue", fg="white", width=20, height=2, command=lambda: send_announcement_email(announcement_entry.get("1.0", "end-1c")))
    send_through_email_button.pack(pady=10)

def view_announcements(is_global):
    announcements = global_announcements if is_global else admin_announcements
    if not announcements:
        messagebox.showinfo("Announcements", "No announcements available.")
    else:
        announcements_text = "\n".join(announcements)
        messagebox.showinfo("Announcements", announcements_text)

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

# Create a button to open the announcements page
announcements_button = tk.Button(admin_window, text="Announcements", bg="blue", fg="white", font=("Arial", 18))
announcements_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

def open_announcement_options():
    announcement_options_window = tk.Toplevel(master=admin_window)
    announcement_options_window.title("Announcement Options")
    announcement_options_window.geometry("400x400")

    view_global_announcement_button = tk.Button(announcement_options_window, text="View Global Announcements", command=lambda: view_announcements(True),
                                   bg="dodger blue", fg="white", font=("Arial", 16), width=20, height=2)
    view_global_announcement_button.pack(pady=10)

    view_admin_announcement_button = tk.Button(announcement_options_window, text="View Admin Announcements", command=lambda: view_announcements(False),
                                   bg="dodger blue", fg="white", font=("Arial", 16), width=20, height=2)
    view_admin_announcement_button.pack(pady=10)

    add_admin_announcement_button = tk.Button(announcement_options_window, text="Add Admin Announcement", command=lambda: open_announcement_editor(False),
                                   bg="dodger blue", fg="white", font=("Arial", 16), width=20, height=2)
    add_admin_announcement_button.pack(pady=10)

    add_global_announcement_button = tk.Button(announcement_options_window, text="Add Global Announcement", command=lambda: open_announcement_editor(True),
                                   bg="dodger blue", fg="white", font=("Arial", 16), width=20, height=2)
    add_global_announcement_button.pack(pady=10)

announcements_button.configure(command=open_announcement_options)

# Define actions for button2, button3, and so on
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

# Create buttons 2 to 6
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
