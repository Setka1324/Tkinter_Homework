import tkinter as tk
from tkinter import ttk
import sqlite3
from os import startfile

class Main(tk.Frame):
    def __init__(self, root):
        super().__init__(root)
        self.init_main()
        self.db = db
        self.view_records()

    def init_main(self):
        toolbar = tk.Frame(bg='#d7d8e0', bd=2)
        toolbar.pack(side=tk.TOP, fill=tk.X)

        self.add_img = tk.PhotoImage(file='add.gif')
        self.add_img_2 = tk.PhotoImage(file='add1.gif')
        self.add_img_3 = tk.PhotoImage(file='add2.gif')
        self.add_img_4 = tk.PhotoImage(file='add3.gif')
        self.add_img_5 = tk.PhotoImage(file='add4.gif')

        btn_open_dialog = tk.Button(toolbar, text='Добавить', command=self.open_dialog, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img)
        btn_open_dialog.pack(side=tk.LEFT)

        

        self.tree = ttk.Treeview(self, columns=('ID', 'product', 'costs'), height=15, show='headings')

        self.tree.column('ID', width=30, anchor=tk.CENTER)
        self.tree.column('product', width=365, anchor=tk.CENTER)
        self.tree.column('costs', width=150, anchor=tk.CENTER)
        

        self.tree.heading('ID', text='ID')
        self.tree.heading('product', text='Name')
        self.tree.heading('costs', text='Цена')
      

        self.tree.pack()

        btn_open_dialog = tk.Button(toolbar, text='Удалить', command=self.records_delete, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img_2)
        btn_open_dialog.pack(side=tk.LEFT)

        btn_open_dialog = tk.Button(toolbar, text='Редактировать', command=self.open_update, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img_3)
        btn_open_dialog.pack(side=tk.LEFT)
    
        btn_open_dialog = tk.Button(toolbar, text='Состав', command=self.open_composition, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img_4)
        
        btn_open_dialog.pack(side=tk.LEFT)

        btn_open_dialog = tk.Button(toolbar, text='Xcel', command=self.excel_import, bg='#d7d8e0', bd=0,
                                    compound=tk.TOP, image=self.add_img_5)
        
        btn_open_dialog.pack(side=tk.LEFT)

    def records_delete(self):
        selected= self.tree.focus()
        values_from_selected = self.tree.item(selected, 'values')
        self.tree.delete(selected)
        self.db.delete_data(values_from_selected)


    def records_update(self, product, price, composition):
        
        selected= self.tree.focus()
        values_from_selected = self.tree.item(selected, 'values')
        self.tree.delete(selected)
        self.db.update_data(values_from_selected, product, price, composition)
        self.view_records()
   
    def records_composition(self):
        selected= self.tree.focus()
        values_from_selected = self.tree.item(selected, 'values')
        mix = self.db.find_composition(values_from_selected)
        return mix

    def records(self, product, composition, price):
        self.db.insert_data(product, composition, price)
        self.view_records()

    def view_records(self):
        self.db.c.execute('''SELECT * FROM price''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end', values=row) for row in self.db.c.fetchall()]

    

    def open_dialog(self):
        Child()

    def open_update(self):
        Child_update()

    def open_composition(self):
        Child_composition()

    def excel_import(self):
        Excel()
    


class Child(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Добавить продукт')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_product = tk.Label(self, text='Name:')
        label_product.place(x=50, y=50)
        label_select = tk.Label(self, text='Состав:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Цена:')
        label_sum.place(x=50, y=110)

        self.entry_product = ttk.Entry(self)
        self.entry_product.place(x=200, y=50)


        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=200, y=80)

        self.entry_composition = ttk.Entry(self)
        self.entry_composition.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Добавить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records(self.entry_product.get(),
                                                                  self.entry_price.get(),
                                                                  self.entry_composition.get()
                                                                  ))

        self.grab_set()
        self.focus_set()

class Child_update(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.init_child()
        self.view = app

    def init_child(self):
        self.title('Редактировать продукт')
        self.geometry('400x220+400+300')
        self.resizable(False, False)

        label_product = tk.Label(self, text='Name:')
        label_product.place(x=50, y=50)
        label_select = tk.Label(self, text='Состав:')
        label_select.place(x=50, y=80)
        label_sum = tk.Label(self, text='Цена:')
        label_sum.place(x=50, y=110)

        self.entry_product = ttk.Entry(self)
        self.entry_product.place(x=200, y=50)


        self.entry_price = ttk.Entry(self)
        self.entry_price.place(x=200, y=80)

        self.entry_composition = ttk.Entry(self)
        self.entry_composition.place(x=200, y=110)

        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        btn_ok = ttk.Button(self, text='Изменить')
        btn_ok.place(x=220, y=170)
        btn_ok.bind('<Button-1>', lambda event: self.view.records_update(self.entry_product.get(),
                                                                  self.entry_composition.get(),
                                                                  self.entry_price.get()))

        self.grab_set()
        self.focus_set()

class Child_composition(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.view = app
        self.init_child()
        

    def init_child(self):
        self.title('Состав')
        self.geometry('400x220+400+300')
        self.resizable(False, False)
        mix = self.view.records_composition()
        print(mix[0])
        btn_cancel = ttk.Button(self, text='Закрыть', command=self.destroy)
        btn_cancel.place(x=300, y=170)

        label_product = tk.Label(self, text=("Name: "+str(mix[0])))
        label_product.place(x=50, y=50)

        label_product_1 = tk.Label(self, text=("Цена: " + str(mix[1])))
        label_product_1.place(x=50, y=70)

        label_product_2 = tk.Label(self, text=("Состав: "+ (str(mix[2]).strip("()''','"))))
        label_product_2.place(x=50, y=90)
        
        self.grab_set()
        self.focus_set()

class Excel(tk.Toplevel):
    def __init__(self):
        super().__init__(root)
        self.view = app
        self.init_child()
        

    def init_child(self):
        label_product = tk.Label(self, text='Done')
        label_product.place(x=50, y=50)
        self.view.db.excel()

        self.grab_set()
        self.focus_set()

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('Comus.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS composition (id integer primary key, product text unique, composition text unique)''')
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS price (id integer primary key, product text unique, price text)''')
        self.conn.commit()

    def insert_data(self, product, composition, price):
        try:
            self.c.execute('''INSERT INTO composition(product, composition) VALUES (?, ?)''',
                            (product, composition))
            self.c.execute('''INSERT INTO price(product, price) VALUES (?, ?)''',
                            (product, price))
            self.conn.commit()
            
        except:
            
            label = tk.Label(text="Состав и name уникальны!")
            label.pack()
        
    def delete_data(self,values_from_selected):
        
        self.c.execute(f'''DELETE from composition where product = "{values_from_selected[1]}"''')
        self.c.execute(f'''DELETE from price where product = "{values_from_selected[1]}" and price = "{values_from_selected[2]}"''')
        self.conn.commit()
    
    def update_data(self,values_from_selected, product, price, composition):
        
        self.c.execute(f'''update composition set product = "{product}", composition = "{composition}"  where product = "{values_from_selected[1]}"''')
        self.c.execute(f'''update price set product = "{product}", price = "{price}"  where product = "{values_from_selected[1]}"''')
        self.conn.commit()
            
    def find_composition(self, values_from_selected):
        self.c.execute(f'''select composition from composition where product = "{values_from_selected[1]}"''')
        a = self.c.fetchall()[0]

        mix = [values_from_selected[1], values_from_selected[2], a]
       
        return mix
    
    def excel(self):
        self.c.execute('''SELECT price.product, price, composition
            FROM price JOIN composition
            on price.product=composition.product''')
        results = self.c.fetchall()
        with open('xcel.csv', 'w') as f:
            for row in results:
                print(row, file=f)
        startfile('xcel.csv')
        
        

        
            


if __name__ == "__main__":
    root = tk.Tk()
    db = DB()
    app = Main(root)
    app.pack()
    root.title("Comus")
    root.geometry("660x560+300+200")
    root.resizable(False, False)
    root.mainloop()