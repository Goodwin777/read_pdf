import PyPDF2
import tkinter as tk
from tkinter import filedialog, scrolledtext, messagebox

class PDFReaderApp:
    def __init__(self, master):
        self.master = master
        master.title("PDF Reader")
        master.geometry("800x600")

        self.text_widget = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=80, height=30)
        self.text_widget.pack(pady=20)

        self.open_button = tk.Button(master, text="Open PDF", command=self.open_file)
        self.open_button.pack(pady=5)

        self.close_button = tk.Button(master, text="Close PDF", command=self.close_pdf, state=tk.DISABLED)
        self.close_button.pack(pady=5)

    def read_pdf(self, file_path):
        self.open_button.config(text="Reading...", state=tk.DISABLED)
        try:
            with open(file_path, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)

                for page_num in range(num_pages):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    self.text_widget.insert(tk.END, f'Page {page_num + 1}:\n{text}\n\n')

            self.text_widget.config(state=tk.DISABLED)
            self.open_button.config(text="Open PDF", state=tk.NORMAL)
            self.close_button.config(state=tk.NORMAL)

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.open_button.config(text="Open PDF", state=tk.NORMAL)
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.insert(tk.END, f"Error reading PDF: {e}\n")
            self.text_widget.config(state=tk.DISABLED)

    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("PDF files", "*.pdf")],
            title="Select a PDF file"
        )
        if file_path:
            self.text_widget.config(state=tk.NORMAL)
            self.text_widget.delete(1.0, tk.END)
            self.read_pdf(file_path)
        else:
            self.open_button.config(state=tk.NORMAL)

    def close_pdf(self):
        self.text_widget.config(state=tk.NORMAL)
        self.text_widget.delete(1.0, tk.END)
        self.close_button.config(state=tk.DISABLED)
        self.text_widget.config(state=tk.DISABLED)


root = tk.Tk()
app = PDFReaderApp(root)
root.mainloop()