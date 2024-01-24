import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter

# Create the main window
root = tk.Tk()
root.title("PDF Splitter")
root.geometry("400x200")

# Function to open a file dialog and select PDF
def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)

# Add a button to open file dialog
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

open_button = tk.Button(root, text="Open PDF", command=open_file)
open_button.pack()

# Labels and entry fields for page range
tk.Label(root, text="Start Page:").pack()
start_page = tk.Entry(root)
start_page.pack()

tk.Label(root, text="End Page:").pack()
end_page = tk.Entry(root)
end_page.pack()

# Function to split the PDF
def split_pdf():
    file_path = entry.get()
    start = int(start_page.get()) - 1  # Adjusting for zero-indexing
    end = int(end_page.get())

    pdf_reader = PdfReader(file_path)
    pdf_writer = PdfWriter()

    # Add the pages to the new file
    for page in range(start, end):
        pdf_writer.add_page(pdf_reader.pages[page])

    # Save the new PDF
    output_filename = f"split_{start+1}_to_{end}.pdf"
    with open(output_filename, "wb") as out:
        pdf_writer.write(out)

    messagebox.showinfo("Done", f"PDF split! Saved as {output_filename}")

# Split button
split_button = tk.Button(root, text="Split PDF", command=split_pdf)
split_button.pack(pady=10)

# Run the application
root.mainloop()
