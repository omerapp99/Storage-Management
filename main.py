import time
from tkinter import Tk, Button, Label, Text, END, Menu, Listbox, messagebox
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.font import Font
import online_report, pickle, threading
from new_item import new

f_array = []


# Stops the program with messagebox
def stop_prog():
    messagebox.showinfo(title='', message='Thank You')
    window.destroy()


# Main Window, the one that open when starting the app.
class App:
    def __init__(self, window):
        window.title("Storage Management")
        window.geometry("700x700")
        window.resizable(False, False)
        window.iconbitmap("app.ico")
        # ~~ Menu window components START ~~
        self.item_list = f_array
        menu = Menu(window)
        menu_item = Menu(menu, tearoff="off")
        menu_item.add_command(label="New Item", command=lambda: new(listb1, self.item_list))
        menu_item.add_separator()
        menu_item.add_command(label="Exit", command=stop_prog)

        menu.add_cascade(label="File", menu=menu_item)
        window.config(menu=menu)

        lbl1 = Label(window, text="Item list:")
        lbl1.place(x=5, y=8)

        self.listb1 = listb1 = Listbox(window, width=32, height=40, selectmode="single", )
        self.listb1.place(x=5, y=34)

        #       ~~~ Item Name ~~~
        self.txt_name = Text(window)
        self.txt_name["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        self.txt_name["font"] = ft
        self.txt_name["fg"] = "#333333"
        self.txt_name.place(x=310, y=34, width=350, height=30)
        self.lbl_itname = Label(window, text="Name: ")
        self.lbl_itname["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        self.lbl_itname["font"] = ft
        self.lbl_itname["fg"] = "#333333"
        self.lbl_itname.place(x=220, y=34)

        self.txt_quan = Text(window)
        self.txt_quan["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        self.txt_quan["font"] = ft
        self.txt_quan["fg"] = "#333333"
        self.txt_quan.place(x=310, y=74, width=350, height=30)
        self.lbl_quan = Label(window, text="Quantity: ")
        self.lbl_quan["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        self.lbl_quan["font"] = ft
        self.lbl_quan["fg"] = "#333333"
        self.lbl_quan.place(x=220, y=74)

        self.txt_serial = Text(window)
        self.txt_serial["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        self.txt_serial["font"] = ft
        self.txt_serial["fg"] = "#333333"
        self.txt_serial.place(x=310, y=114, width=350, height=30)
        self.lbl_serial = Label(window, text="Serial Number: ")
        self.lbl_serial["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        self.lbl_serial["font"] = ft
        self.lbl_serial["fg"] = "#333333"
        self.lbl_serial.place(x=220, y=114)

        #       Select the item
        self.btn_select = Button(window, text="Select Item", command=lambda: new.on_select(self))
        self.btn_select["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        self.btn_select["font"] = ft
        self.btn_select["fg"] = "#333333"
        self.btn_select.place(x=310, y=154, width=350, height=30)

        #       Update Item
        btn_update = Button(window, text="Update Item", command=lambda: new.update_item(self))
        btn_update["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        btn_update["font"] = ft
        btn_update["fg"] = "#333333"
        btn_update.place(x=310, y=194, width=350, height=30)

        #       Import Items
        btn_import = Button(window, text="Import", command=lambda: self.import_item())
        btn_import["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        btn_import["font"] = ft
        btn_import["fg"] = "#333333"
        btn_import.place(x=310, y=234, width=350, height=30)

        #       Export Items
        btn_export = Button(window, text="Export", command=lambda: self.export_item())
        btn_export["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        btn_export["font"] = ft
        btn_export["fg"] = "#333333"
        btn_export.place(x=310, y=274, width=350, height=30)
        # ~~ Main window components End ~~

        #       Thread for the website updates, everytime that the user reload the page the user receive the data.
        t = threading.Thread(target=online_report.flasks, args=(self,))
        t.daemon = True
        t.start()



    # Import and Export Items Functions.
    def export_item(self):
        path = asksaveasfilename(defaultextension='.pickle', filetypes=[("Pickle Files", "*.pickle")])
        print(path)
        with open(path, 'wb') as fp:
            pickle.dump(self.item_list, fp)

    def import_item(self):
        path = askopenfilename(filetypes=[("Pickle Files", "*.pickle")])
        with open(path, 'rb') as fb:
            n_list = pickle.load(fb)
            self.item_list = n_list
            self.listb1.delete(0, END)
            item_count = int(len(self.item_list))
            for i in range(item_count):
                self.listb1.insert(END, self.item_list[i]["name"])


if __name__ == "__main__":
    window = Tk()
    app = App(window)
    # window.protocol('WM_DELETE_WINDOW', stop_prog)
    window.mainloop()
