import customtkinter as ctk
import subprocess


def view_admin_announcement():
    subprocess.run(['python', r'New APP\App\view_admin_announcement.py'], check=True)

def view_global_announcement():
    subprocess.run(['python', r'New APP\App\View Global Announcement.py'], check=True)

def add_admin_announcement():
    subprocess.run(['python', r'New APP\App\Admin announcement.py'], check=True)

def add_global_announcement():
    subprocess.run(['python', r'New APP\App\global announcement.py'], check=True)

# Create the Admin main page window
admin_window = ctk.CTk()
admin_window.title("Admin Main Page")
admin_window.geometry("800x600")
admin_window.configure(bg="light blue")
admin_window.grab_set()

# Define a function to open the admin timetable
def open_admin_timetable():
    try:
        subprocess.run(['python', 'admin_timetable.py'], check=True)
    except FileNotFoundError:
        ctk.messagebox.showerror("Error", "Admin timetable code file not found.")

# Create a button to open the admin timetable
admin_timetable_button = ctk.CTkButton(
    admin_window, text="Open Admin Timetable", command=open_admin_timetable, font=("Arial", 18)
)
admin_timetable_button.place(relx=0.5, rely=0.2, anchor=ctk.CENTER)

# Create a button to open the announcements page
announcements_button = ctk.CTkButton(admin_window, text="Announcements", font=("Arial", 18))
announcements_button.place(relx=0.5, rely=0.3, anchor=ctk.CENTER)

def open_announcement_options():
    announcement_options_window = ctk.CTkToplevel(master=admin_window)
    announcement_options_window.title("Announcement Options")
    announcement_options_window.geometry("400x400")

    view_global_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="View Global Announcements",
        command=lambda: view_global_announcement(),
        font=("Arial", 16)
    )
    view_global_announcement_button.pack(pady=10)

    view_admin_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="View Admin Announcements",
        command=lambda: view_admin_announcement(),
        font=("Arial", 16)
    )
    view_admin_announcement_button.pack(pady=10)

    add_admin_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="Add Admin Announcement",
        command=lambda: add_admin_announcement(),
        font=("Arial", 16)
    )
    add_admin_announcement_button.pack(pady=10)

    add_global_announcement_button = ctk.CTkButton(
        announcement_options_window,
        text="Add Global Announcement",
        command=lambda: add_global_announcement(),
        font=("Arial", 16)
    )
    add_global_announcement_button.pack(pady=10)

announcements_button.configure(command=open_announcement_options)

# Start the main event loop for the Admin main page
admin_window.mainloop()
