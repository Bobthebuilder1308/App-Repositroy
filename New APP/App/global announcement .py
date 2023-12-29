# global_announcement.py
import csv
import os
from customtkinter import CTkButton, CTkToplevel
import tkinter as tk  
from tkinter import filedialog
from datetime import datetime

def load_global_announcements(filename):
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            announcements = list(reader)
            return announcements
    else:
        return []

def save_global_announcement(filename, announcement_text, attachment):
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, filename)
    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date_time, announcement_text, attachment])

def open_global_announcements_window():
    global_announcements_window = CTkToplevel()
    global_announcements_window.title("Global Announcements")
    global_announcements_window.geometry("600x400")

    def make_global_announcement():
        # Open the "Global Announcement Editor" directly
        announcement_editor = CTkToplevel(master=global_announcements_window)
        announcement_editor.title("Global Announcement Editor")
        announcement_editor.geometry("600x400")
        
        # Set the background color of the announcement editor window
        announcement_editor.configure(bg="#FFFFCC")  

        # Use tk.Text for entering and displaying the announcement text
        announcement_text = tk.Text(announcement_editor, wrap=tk.WORD)
        announcement_text.pack(pady=10)

        def attach_file():
            file_path = filedialog.askopenfilename()
            attachment_label.configure(text=file_path)

        # Button to attach a file
        attach_button = CTkButton(announcement_editor, text="Attach File", command=attach_file)
        attach_button.pack(pady=10)

        # Label to display the selected attachment file
        attachment_label = CTkButton(announcement_editor, text="No Attachment")
        attachment_label.pack(pady=10)

        def send_announcement():
            save_global_announcement("global_announcements.csv", announcement_text.get("1.0", "end-1c"), attachment_label.cget("text"))
            tk.messagebox.showinfo("Success", "Announcement made successfully!")

        send_button = CTkButton(announcement_editor, text="Send Announcement", command=send_announcement)
        send_button.pack()

    make_announcement_button = CTkButton(global_announcements_window, text="Make Global Announcement", command=make_global_announcement)
    make_announcement_button.pack(pady=10)

    # Display announcements in the main window
    announcements = load_global_announcements("global_announcements.csv")
    for announcement in announcements:
        # Create a button for each announcement
        announcement_label = CTkButton(global_announcements_window, text=f"{announcement[0]}: {announcement[1]}\nAttachment: {announcement[2]}", wraplength=500)
        announcement_label.pack(pady=5, padx=10)

    return global_announcements_window

if __name__ == "__main__":
    global_announcements_window = open_global_announcements_window()
    global_announcements_window.mainloop()
