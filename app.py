import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
import pandas as pd
from extract_data import extract_data_from_html

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("ASSET MANAGEMENT")
        self.root.geometry("500x300")
        self.root.resizable(False, False)
        
        self.file_paths = []

        # Style Configuration
        self.style = ttk.Style()
        self.style.theme_use('clam')  # You can choose a different theme if you like
        self.style.configure('TFrame', background='white')
        self.style.configure('TButton', font=('Helvetica', 12), padding=10, background='skyblue', foreground='white')
        self.style.map('TButton', background=[('active','#2980b9')])  # Active state color for buttons
        self.style.configure('TLabel', font=('Helvetica', 12), background='#f0f0f0')
        self.style.configure('Header.TLabel', font=('Helvetica', 14, 'bold'), background='yellow')

        # Frame for the content
        self.frame = ttk.Frame(root, padding="20")
        self.frame.pack(expand=True, fill='both')

        # Header Label
        self.header_label = ttk.Label(self.frame, text="ASSET MANAGEMENT", style='Header.TLabel')
        self.header_label.pack(pady=(0, 20))

        # Upload Button
        self.upload_button = ttk.Button(self.frame, text="Upload HTML Files", command=self.upload_files, style='TButton')
        self.upload_button.pack(pady=10)

        # Convert Button
        self.convert_button = ttk.Button(self.frame, text="SUBMIT", command=self.convert_to_excel, style='TButton')
        self.convert_button.pack(pady=10)

    def upload_files(self):
        files = filedialog.askopenfilenames(filetypes=[("HTML files", "*.html")])
        if files:
            self.file_paths = files
            messagebox.showinfo("Selected Files", f"{len(self.file_paths)} files selected")
        else:
            messagebox.showwarning("No Selection", "No files were selected")

    def convert_to_excel(self):
        if not self.file_paths:
            messagebox.showerror("Error", "No files selected")
            return

        df = extract_data_from_html(self.file_paths)
        save_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
        if save_path:
            df.to_excel(save_path, index=False)
            messagebox.showinfo("Success", f"Data saved to {save_path}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
