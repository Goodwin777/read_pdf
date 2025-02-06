import PyPDF2
import tkinter as tk
from tkinter import filedialog, scrolledtext


def read_pdf(file_path, text_widget, open_button, close_button):
    open_button.config(text="Reading...", state=tk.DISABLED)
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)

        # Extract text from each page and insert it into the text widget
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text = page.extract_text()
            text_widget.insert(tk.END, f'Page {page_num + 1}:\n{text}\n\n')

    text_widget.config(state=tk.DISABLED)
    open_button.config(text="Open PDF", state=tk.NORMAL)
    close_button.config(state=tk.NORMAL)


def open_file(text_widget, open_button, close_button):
    file_path = filedialog.askopenfilename(
        filetypes=[("PDF files", "*.pdf")],
        title="Select a PDF file"
    )
    if file_path:
        text_widget.config(state=tk.NORMAL)
        text_widget.delete(1.0, tk.END)
        read_pdf(file_path, text_widget, open_button, close_button)


def close_pdf(text_widget, close_button):
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    close_button.config(state=tk.DISABLED)
    text_widget.config(state=tk.DISABLED)


# Set up the Tkinter window
root = tk.Tk()
root.title("NikitOS PDF Reader")  # Change the window title here
root.geometry("800x600")  # Set the window size to 800x600 pixels

# Add a Text widget with a scrollbar
text_widget = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=30)
text_widget.pack(pady=20)

# Add buttons
open_button = tk.Button(root, text="Open PDF", command=lambda: open_file(text_widget, open_button, close_button))
open_button.pack(pady=5)

close_button = tk.Button(root, text="Close PDF", command=lambda: close_pdf(text_widget, close_button),
                         state=tk.DISABLED)
close_button.pack(pady=5)

root.mainloop()
