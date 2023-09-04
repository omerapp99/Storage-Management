from tkinter import  Menu, Listbox, messagebox
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from tkinter.filedialog import askopenfilename, asksaveasfilename
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

        lbl1 = tb.Label(window, text="Item list:", bootstyle="info")
        lbl1.place(x=5, y=8)

        self.listb1 = listb1 = Listbox(window, width=32, height=40, selectmode="single", exportselection=False)
        self.listb1.place(x=5, y=34)

        #       ~~~ Item Name ~~~
        self.txt_name = tb.Text(window)
        self.txt_name.place(x=310, y=34, width=350, height=30)
        self.lbl_itname = tb.Label(window, text="Name: ", bootstyle="info")
        self.lbl_itname.place(x=220, y=34)

        self.txt_quan = tb.Text(window)
        self.txt_quan.place(x=310, y=74, width=350, height=30)
        self.lbl_quan = tb.Label(window, text="Quantity: ", bootstyle="info")
        self.lbl_quan.place(x=220, y=74)

        self.txt_serial = tb.Text(window)
        self.txt_serial.place(x=310, y=114, width=350, height=30)
        self.lbl_serial = tb.Label(window, text="Serial Number: ", bootstyle="info")
        self.lbl_serial.place(x=220, y=114)

        #       Update Item
        btn_update = tb.Button(window, text="Update Item", command=lambda: new.update_item(self),
                               bootstyle="outline-success")
        btn_update.place(x=310, y=194, width=350, height=30)

        #       Delete Item
        btn_delete = tb.Button(window, text="Delete Item", command=lambda: new.delete_item(self),
                               bootstyle="outline-danger")
        btn_delete.place(x=310, y=234, width=350, height=30)

        #       Import Items
        btn_import = tb.Button(window, text="Import", command=lambda: self.import_item(), bootstyle="outline-success")
        btn_import.place(x=310, y=274, width=350, height=30)

        #       Export Items
        btn_export = tb.Button(window, text="Export", command=lambda: self.export_item(), bootstyle="outline-success")
        btn_export.place(x=310, y=314, width=350, height=30)
        # ~~ Main window components End ~~

        #       Thread for the website updates, everytime that the user reload the page the user receive the data.
        t = threading.Thread(target=online_report.flasks, args=(self,))
        t.daemon = True
        t.start()

        def callback(event):
            new.on_select(self)

        self.listb1.bind("<<ListboxSelect>>", callback)

    # Import and Export Items Functions.
    def export_item(self):
        try:
            path = asksaveasfilename(defaultextension='.pickle', filetypes=[("Pickle Files", "*.pickle")])
            print(path)
            with open(path, 'wb') as fp:
                pickle.dump(self.item_list, fp)
        except:
            print("Use canceled the export")

    def import_item(self):
        try:
            path = askopenfilename(filetypes=[("Pickle Files", "*.pickle")])
            with open(path, 'rb') as fb:
                n_list = pickle.load(fb)
                self.item_list = n_list
                self.listb1.delete(0, END)
                item_count = int(len(self.item_list))
                for i in range(item_count):
                    self.listb1.insert(END, self.item_list[i]["name"])
        except:
            print("User canceled the import")


if __name__ == "__main__":
    window = tb.Window(themename="darkly")
    app = App(window)
    window.mainloop()

