from tkinter import Entry, Label, Toplevel, Button, messagebox, END
from tkinter.font import Font


# New window, where you add new items.
class new(object):
    def __init__(self, listb1, f_array):
        top = Toplevel()
        top.title("New Item")
        top.geometry("500x500")
        top.resizable(False, False)
        top.iconbitmap("app.ico")

        # ~~ Item Name Start ~~
        lb_name = Label(top)
        ft = Font(family='Times', size=10)
        lb_name["font"] = ft
        lb_name["fg"] = "#333333"
        lb_name["justify"] = "center"
        lb_name["text"] = "Item Name:"
        lb_name.place(x=20, y=10, width=97, height=42)
        en_name = Entry(top)
        en_name["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        en_name["font"] = ft
        en_name["fg"] = "#333333"
        en_name["justify"] = "left"
        en_name["text"] = "Name"
        en_name.place(x=120, y=20, width=350, height=30)
        # ~~ Item Name END ~~

        # ~~ Serial ID Start ~~
        lb_serial = Label(top)
        ft = Font(family='Times', size=10)
        lb_serial["font"] = ft
        lb_serial["fg"] = "#333333"
        lb_serial["justify"] = "center"
        lb_serial["text"] = "Serial ID:"
        lb_serial.place(x=30, y=160, width=70, height=25)
        en_serial = Entry(top)
        en_serial["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        en_serial["font"] = ft
        en_serial["fg"] = "#333333"
        en_serial["justify"] = "left"
        en_serial["text"] = "serial"
        en_serial.place(x=120, y=160, width=350, height=30)

        # ~~ Quantity Start ~~
        lb_quan = Label(top)
        ft = Font(family='Times', size=10)
        lb_quan["font"] = ft
        lb_quan["fg"] = "#333333"
        lb_quan["justify"] = "center"
        lb_quan["text"] = "Quantity:"
        lb_quan.place(x=30, y=90, width=70, height=25)
        en_quan = Entry(top)
        en_quan["borderwidth"] = "1px"
        ft = Font(family='Times', size=10)
        en_quan["font"] = ft
        en_quan["fg"] = "#333333"
        en_quan["justify"] = "left"
        en_quan["text"] = "Quantity"
        en_quan.place(x=120, y=90, width=350, height=30)
        # ~~ Quantity End ~~
        self.top = top
        self.en_quan = en_quan
        self.en_serial = en_serial
        self.en_name = en_name
        self.listb1 = listb1
        self.item_list = f_array
        self.btn1 = Button(top, command=lambda: new.on_closing(self))
        ft = Font(family='Times', size=10)
        self.btn1["fg"] = "#333333"
        self.btn1["text"] = "Add Item"
        self.btn1.place(x=210, y=200, width=100)
        # ~~ Serial ID END ~~

        # Set the "Tab" Order
        widgets = [en_name, en_quan, en_serial]
        for widget in widgets:
            widget.lift()
        top.mainloop()

    # Save the new Item
    def save_item(self):
        self.item = item = {
            "name": self.en_name.get(),
            "serial": self.en_serial.get(),
            "quantity": self.en_quan.get()
        }
        dic_copy = self.item.copy()
        self.item_list.append(dic_copy)
        #        item_list_globel = self.f_array
        self.listb1.insert(END, self.item["name"])
        print(self.item_list)

        # Clear the entries
        self.en_name.delete(0, 'end')
        self.en_quan.delete(0, 'end')
        self.en_serial.delete(0, 'end')

    # Popup window when saving item
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to save the item?", parent=self.top):
            new.save_item(self)

    # Update the item
    def update_item(self):
        self.dict_data = {
            "name": self.txt_name.get("1.0", "end-1c"),
            "serial": self.txt_serial.get("1.0", "end-1c"),
            "quantity": self.txt_quan.get("1.0", "end-1c")
        }
        self.item_list[self.dict_id] = self.dict_data
        print(self.item_list)
        for i in self.listb1.curselection():
            self.listb1.delete(i)
            self.listb1.insert(i, self.txt_name.get("1.0", "end-1c"))

    # Receive the selected item data
    def on_select(self):
        print(self.item_list)
        for i in self.listb1.curselection():
            self.dict_id = str(self.listb1.curselection())
            self.dict_id = int(self.dict_id[1:2])
            #            self.list_data = list_data = new.get_item_list(self)

            self.dict_data = self.item_list[self.dict_id]

            # Name
            self.txt_name.delete("1.0", "end-1c")
            self.txt_name.insert(END, self.dict_data["name"])
            # Quantity
            self.txt_quan.delete("1.0", "end-1c")
            self.txt_quan.insert(END, self.dict_data["quantity"])
            # Serial ID
            self.txt_serial.delete("1.0", "end-1c")
            self.txt_serial.insert(END, self.dict_data["serial"])


if __name__ == "__main__":
    new()
