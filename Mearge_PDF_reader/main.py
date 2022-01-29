from pydoc import text
from tkinter import BOTH, LEFT, RIGHT, VERTICAL, Y, Tk, IntVar, Label, Checkbutton, Button, Frame, Canvas, ttk
from tkPDFViewer import tkPDFViewer as pdf
from PyPDF2 import PdfFileMerger
import os
from pdf_viewer import second_window



root = Tk()
root.geometry("630x700")
root.title("Mearge_PDF Viewer")


#current working directory
source_dir = os.getcwd()
# merge Pdf Path
path = os.path.join(source_dir, "Merge_Pdf")




#creating PdfFileMerger object
merge_pdf_obj = PdfFileMerger()

#list of directory
list_of_directory = os.listdir(source_dir)
#print(list_of_directory)

#creating list containing name of PDFs
pdf_list = [name for name in list_of_directory if name.endswith(".pdf")]
#print(pdf_list)
no_of_pdf = len(pdf_list)

# creating IntVar Objects:
int_obj = [IntVar(root) for i in range(no_of_pdf)]

# Create A Main Frame
main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=1)

# Create A Canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")


Label(second_frame,text="PDF AVILABLEs:").pack()


i = 0
for name in pdf_list:
    c = Checkbutton(second_frame, text= name, variable= int_obj[i], padx=5, pady=2)
    c.deselect()
    c.pack(expand = True)
    i += 1

#Creating new pdf name function
def merge_all_pdf():
    #creating new directory
    try :
        os.mkdir(path)
        for i in range(no_of_pdf):
            if int_obj[i].get():
                merge_pdf_obj.append(pdf_list[i])
        merge_pdf_obj.write("./Merge_Pdf/New_PDF.pdf")
        root.destroy()
        second_window()
    except :
        Label(second_frame, text="Directory Alredy Exist... Delete it and Re Run The Programe")

def merge_pdf():
    #creating new directory
    try :
        os.mkdir(path)
        for i in pdf_list:
            merge_pdf_obj.append(i)
        merge_pdf_obj.write("./Merge_Pdf/New_PDF.pdf")
        root.destroy()
        second_window()
    except :
        Label(second_frame, text="Directory Alredy Exist... Delete it and Re Run The Programe")

Button(second_frame, text="Merge PDFs", command=merge_all_pdf).pack()
Button(second_frame, text= "Select All And Merge PDFs", command=merge_pdf).pack()


if __name__=="__main__":
    root.mainloop()

