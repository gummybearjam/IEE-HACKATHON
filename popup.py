from cProfile import label
from importlib.resources import files
from tkinter import*
from unittest import result
from httpx import delete
from tkinterdnd2 import TkinterDnD, DND_FILES
from subprocess import call 
from main import AIreadsThrough



window = TkinterDnD.Tk()
window.geometry("540x960")
window.title("Weekday")

icon = PhotoImage(file ='Design/Untitled design.png')
window.iconphoto(True, icon)
window.config(background = "#1800ad")

def open_py_file(self):
    call(["python", "main.py"])

class fileUpload:
    def __init__(self,master):
        self.master = master

        '''self.popup = Toplevel(self.master)
        self.popup.title("Please Drag and Drop your Files")
        self.popup.geometry("540x960")'''

        self.drop_label = Label(self.master, text="Please Drag and Drop your Files here.", relief="solid", bd=2, width=68, height=8, bg="#1800ad")
        self.drop_label.pack(pady=20)

        self.drop_label.drop_target_register(DND_FILES)
        self.drop_label.dnd_bind("<<Drop>>", self.drop)

        self.dropped_files = []
    
        self.result_box = Text(self.master, height =40, width =68)
        self.result_box.pack(pady=20, fill = BOTH, expand = True)
        self.result_box.insert(END, "Your results will appear here.")

    def drop(self, event):
        files = self.master.tk.splitlist(event.data)
        self.dropped_files.extend(files)
        print("File:", self.dropped_files)

        pdf_path = self.dropped_files[-1]
        print(pdf_path)

        result = AIreadsThrough(pdf_path)
        self.result_box.delete(1.0, END)
        self.result_box.insert(END, result)


app = fileUpload(window)

window.mainloop()
