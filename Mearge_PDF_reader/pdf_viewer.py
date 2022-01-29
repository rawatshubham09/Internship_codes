from tkinter import Tk
from tkPDFViewer import tkPDFViewer as pdf
import os

# Code
def second_window():
    root1 = Tk()
    root1.geometry("700x750")
    root1.title("Mearge_PDF Viewer")
    root1.config(bg="black")

    source_dir = os.getcwd()
    path = os.path.join(source_dir, "Merge_Pdf/New_PDF.pdf")

    #New
    v1 = pdf.ShowPdf()
    screen = v1.pdf_view(root1, pdf_location= path, width=77, height=100)
    screen.pack(pady=(0,0))

    root1.mainloop()


