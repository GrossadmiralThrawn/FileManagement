import os
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk
from implementations.PDFImplementation import PDFImplementation


class PDFApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Management")
        self.geometry("500x400")  # Fenstergröße
        self.sTDFileInterface = None

        # Start with the Wellbeing view
        self.show_wellbeing_view()

    def show_wellbeing_view(self):
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self)
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=(150, 20))  # Verschieben nach unten

        tk.Label(frame, text="Wie geht es dir?").pack(pady=20)

        button_frame = tk.Frame(frame)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Gut", command=self.on_good).pack(side=tk.LEFT, padx=20)
        tk.Button(button_frame, text="Schlecht", command=self.on_bad).pack(side=tk.RIGHT, padx=20)

    def on_good(self):
        messagebox.showinfo("Schön zu hören", "Schön zu hören. :)")
        self.show_file_selection_view()

    def on_bad(self):
        messagebox.showinfo("Das tut mir leid", "Das tut mir leid. Ich hoffe es geht dir bald wieder besser.")
        self.show_file_selection_view()

    def show_file_selection_view(self):
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self)
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=(150, 20))  # Verschieben nach unten

        tk.Label(frame, text="Bitte wähle eine Option:").pack(pady=10)

        self.option = tk.StringVar()
        self.option.set("1: Zwei PDFs mergen")

        options = [
            "1: Zwei PDFs mergen",
            "2: Mehrere PDFs mergen",
            "3: Mehrere PDFs mergen, aber ohne die Objektinitialisierungsdatei."
        ]

        # OptionMenu wird sauber neu erstellt
        if hasattr(self, "option_menu"):
            self.option_menu.destroy()

        self.option_menu = ttk.OptionMenu(frame, self.option, options[0], *options)
        self.option_menu.pack(pady=10)

        tk.Button(frame, text="Weiter", command=self.on_next).pack(pady=20)

    def on_next(self):
        selected_option = self.option.get()

        if selected_option.startswith("1"):
            self.merge_two_pdfs_view()
        elif selected_option.startswith("2"):
            messagebox.showinfo("Noch nicht implementiert", "Option 2: Mehrere PDFs mergen ist noch nicht implementiert.")
            self.show_file_selection_view()
        elif selected_option.startswith("3"):
            messagebox.showinfo("Noch nicht implementiert", "Option 3: Mehrere PDFs ohne Init-Datei ist noch nicht implementiert.")
            self.show_file_selection_view()
        else:
            self.quit()

    def merge_two_pdfs_view(self):
        for widget in self.winfo_children():
            widget.destroy()

        frame = tk.Frame(self)
        frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=(150, 20))  # Verschieben nach unten

        tk.Label(frame, text="Datei 1 auswählen:").pack(pady=5)
        self.file1_path = tk.Entry(frame, width=50)
        self.file1_path.pack(pady=5)
        tk.Button(frame, text="Durchsuchen", command=self.select_file1).pack(pady=5)

        tk.Label(frame, text="Datei 2 auswählen:").pack(pady=5)
        self.file2_path = tk.Entry(frame, width=50)
        self.file2_path.pack(pady=5)
        tk.Button(frame, text="Durchsuchen", command=self.select_file2).pack(pady=5)

        tk.Label(frame, text="Speicherort auswählen:").pack(pady=5)
        self.save_path = tk.Entry(frame, width=50)
        self.save_path.pack(pady=5)
        tk.Button(frame, text="Durchsuchen", command=self.select_save_path).pack(pady=5)

        tk.Label(frame, text="Ausgabedatei-Name:").pack(pady=5)
        self.output_name = tk.Entry(frame, width=50)
        self.output_name.pack(pady=5)

        button_frame = tk.Frame(frame)
        button_frame.pack(pady=20)

        tk.Button(button_frame, text="Merge PDFs", command=self.merge_pdfs).pack(side=tk.LEFT, padx=10)
        tk.Button(button_frame, text="Zurück", command=self.show_file_selection_view).pack(side=tk.RIGHT, padx=10)

    def select_file1(self):
        self.file1_path.delete(0, tk.END)
        self.file1_path.insert(0, filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))

    def select_file2(self):
        self.file2_path.delete(0, tk.END)
        self.file2_path.insert(0, filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")]))

    def select_save_path(self):
        self.save_path.delete(0, tk.END)
        self.save_path.insert(0, filedialog.askdirectory())

    def merge_pdfs(self):
        file1 = self.file1_path.get()
        file2 = self.file2_path.get()
        save_dir = self.save_path.get()
        output_name = self.output_name.get()

        if not all([file1, file2, save_dir, output_name]):
            messagebox.showerror("Fehler", "Bitte füllen Sie alle Felder aus.")
            return

        # Initialisiere die PDFImplementation und merge die Dateien
        self.sTDFileInterface = PDFImplementation(os.path.dirname(file1), os.path.basename(file1))
        self.sTDFileInterface.mergeFile(os.path.dirname(file2), os.path.basename(file2), save_dir, output_name)

        messagebox.showinfo("Erfolg", "Die Dateien wurden erfolgreich gemerged.")
        self.clear_fields()

    def clear_fields(self):
        self.file1_path.delete(0, tk.END)
        self.file2_path.delete(0, tk.END)
        self.save_path.delete(0, tk.END)
        self.output_name.delete(0, tk.END)


if __name__ == "__main__":
    app = PDFApp()
    app.mainloop()
