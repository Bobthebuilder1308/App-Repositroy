# view_admin_announcement.py
import csv
import os
import tkinter as tk
from tkinter import Button, filedialog
import shutil
def load_admin_announcements(filename):
    current_directory = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_directory, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            announcements = list(reader)
            return announcements
    else:
        return []
def download_attachment(attachment_path):
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=os.path.basename(attachment_path))
    if save_path:
        shutil.copyfile(attachment_path, save_path)
        tk.messagebox.showinfo("Download Attachment", f"Downloading {os.path.basename(attachment_path)} to {save_path}")
def open_admin_announcements_viewer():
    admin_announcements_viewer = tk.Toplevel()
    admin_announcements_viewer.title("View Admin Announcements")
    admin_announcements_viewer.geometry("600x400")
    announcements = load_admin_announcements("admin_announcements.csv")
    for announcement in announcements:
        announcement_text = f"{announcement[0]}: {announcement[1]}\nAttachment: {announcement[2]}"
        # Create a label for each announcement
        announcement_label = tk.Label(admin_announcements_viewer, text=announcement_text, wraplength=500, justify="left")
        announcement_label.pack(pady=5, padx=10)
        # Check if there is an attachment
        if announcement[2]:
            # Create a download button for the attachment
            download_button = Button(admin_announcements_viewer, text="Download Attachment", command=lambda path=announcement[2]: download_attachment(path))
            download_button.pack(pady=5, padx=10)
    return admin_announcements_viewer
if __name__ == "__main__":
    admin_announcements_viewer = open_admin_announcements_viewer()
    admin_announcements_viewer.mainloop()
