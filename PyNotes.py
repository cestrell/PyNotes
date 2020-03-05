from tkinter import *
from tkinter import ttk
from tkinter import filedialog

def open_file():
    blank.delete("1.0", END)
    file = filedialog.askopenfile(mode='r', filetypes=[('text files', '*.txt')])
    if file is not None:
        text = file.read()
        blank.insert("1.0", text)

def save_file():
    notepad_text = blank.get("1.0", "end-1c")
    file = filedialog.asksaveasfilename(title="Save", filetypes=[('text files', '*.txt')])
    with open(file, 'w') as data:
        data.write(notepad_text)

window = Tk()
menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)

window.title("Notepad")
window.geometry("350x350")
window.config(menu=menubar)

menubar.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="Open", command=open_file)
filemenu.add_command(label="Save", command=save_file)
filemenu.add_command(label="Exit", command=window.destroy)

blank = Text(window, font=("arial", 10))
blank.pack()

window.mainloop()