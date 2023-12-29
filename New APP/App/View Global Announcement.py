# view_global_announcement.py
import csv
import os
import tkinter as tk
from tkinter import Button, filedialog
import shutil
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
def download_attachment(attachment_path):
    save_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile=os.path.basename(attachment_path))
    if save_path:
        shutil.copyfile(attachment_path, save_path)
        tk.messagebox.showinfo("Download Attachment", f"Downloading {os.path.basename(attachment_path)} to {save_path}")
def open_global_announcements_viewer():
    global_announcements_viewer = tk.Toplevel()
    global_announcements_viewer.title("View Global Announcements")
    global_announcements_viewer.geometry("600x400")
    announcements = load_global_announcements("global_announcements.csv")
    for announcement in announcements:
        announcement_text = f"{announcement[0]}: {announcement[1]}\nAttachment: {announcement[2]}"
        announcement_label = tk.Label(global_announcements_viewer, text=announcement_text, wraplength=500, justify="left")
        announcement_label.pack(pady=5, padx=10)
        if announcement[2]:
            download_button = Button(global_announcements_viewer, text="Download Attachment", command=lambda path=announcement[2]: download_attachment(path))
            download_button.pack(pady=5, padx=10)
    return global_announcements_viewer
if __name__ == "__main__":
    global_announcements_viewer = open_global_announcements_viewer()
    global_announcements_viewer.mainloop()
