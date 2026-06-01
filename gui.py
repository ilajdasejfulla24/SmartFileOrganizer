import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

from organizer import FileOrganizer
from undo_manager import UndoManager


class OrganizerGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Smart File Organizer")
        self.root.geometry("700x500")

        self.organizer = FileOrganizer()
        self.undo_manager = UndoManager()

        self.folder_path = ""
        self.stop_requested = False

        self.label = tk.Label(
            root,
            text="No folder selected"
        )
        self.label.pack(pady=10)

        browse_btn = tk.Button(
            root,
            text="Browse Folder",
            command=self.select_folder
        )
        browse_btn.pack()

        start_btn = tk.Button(
            root,
            text="Start Organizing",
            command=self.organize
        )
        start_btn.pack(pady=5)

        stop_btn = tk.Button(
            root,
            text="Stop",
            command=self.stop_organizing
        )
        stop_btn.pack(pady=5)

        undo_btn = tk.Button(
            root,
            text="Undo Last Action",
            command=self.undo_last
        )
        undo_btn.pack(pady=5)

        self.log_box = tk.Text(
            root,
            height=15,
            width=80
        )
        self.log_box.pack(pady=10)

    def select_folder(self):

        self.folder_path = filedialog.askdirectory()

        self.label.config(
            text=self.folder_path
        )

    def stop_organizing(self):

        self.stop_requested = True

    def organize(self):

        if not self.folder_path:

            messagebox.showerror(
                "Error",
                "Select a folder first."
            )
            return

        self.stop_requested = False

        try:

            result = self.organizer.organize(
                self.folder_path,
                lambda: self.stop_requested
            )

            self.log_box.insert(
                tk.END,
                result + "\n"
            )

            messagebox.showinfo(
                "Success",
                result
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def undo_last(self):

        result = self.undo_manager.undo_last()

        self.log_box.insert(
            tk.END,
            result + "\n"
        )

        messagebox.showinfo(
            "Undo",
            result
        )
