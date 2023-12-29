import os
from customtkinter import CTkButton, CTkToplevel
import tkinter as tk
import csv
from tkinter import filedialog
from datetime import datetime

attachment_label = None

def make_admin_announcement():
    global attachment_label
    admin_announcement_editor = CTkToplevel()
    admin_announcement_editor.title("Admin Announcement Editor")
    admin_announcement_editor.geometry("400x400")
    admin_announcement_editor.configure(bg="#FFD700")

    # Display The Announcement
    announcement_text = tk.Text(admin_announcement_editor, wrap=tk.WORD)
    announcement_text.pack(pady=10)

    def attach_file():
        # Open file explorer for attaching a file
        file_path = filedialog.askopenfilename()
        attachment_label.config(text=file_path)

    attach_file_button = CTkButton(admin_announcement_editor, text="Attach File", command=attach_file)
    attach_file_button.pack(pady=10)

    attachment_label = tk.Label(admin_announcement_editor, text="", wraplength=300, justify="left")
    attachment_label.pack()

    def save_admin_announcement():
        announcement_text_content = announcement_text.get("1.0", "end-1c")
        attachment_path = attachment_label.cget("text")

        current_directory = os.path.abspath(os.path.dirname(__file__))
        file_path = os.path.join(current_directory, "admin_announcements.csv")

        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([datetime.now().strftime("%Y-%m-%d %H:%M:%S"), announcement_text_content, attachment_path])

        tk.messagebox.showinfo("Success", "Announcement made successfully!")

    send_button = CTkButton(admin_announcement_editor, text="Send Announcement", command=save_admin_announcement)
    send_button.pack()

    admin_announcement_editor.mainloop()

if __name__ == "__main__":
    make_admin_announcement()
