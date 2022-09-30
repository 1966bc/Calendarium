#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calendarium import Calendarium


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        self.init_ui()
          
    def init_ui(self):

        f0 = ttk.Frame(self, relief=tk.RIDGE, borderwidth=2, padding=8)
        
        f1 = ttk.Frame(f0,  relief=tk.RIDGE, borderwidth=2, padding=8)

        self.start_date = Calendarium(f1, "Start Date")
        
        self.end_date = Calendarium(f1, "End Date")
        
        self.start_date.get_calendarium(f1,)
        
        self.end_date.get_calendarium(f1,)
              
        f2 = ttk.Frame(f0, relief=tk.RIDGE, borderwidth=2, padding=4)

        bts = (("Print Date", 0, self.on_print_date, "<Alt-p>"),
               ("Set Today", 4, self.on_set_today, "<Alt-t>"),
               ("Compare", 0, self.on_compare, "<Alt-c>"),
               ("Difference", 0, self.on_difference, "<Alt-d>"),
               ("Close", 4, self.on_close, "<Alt-e>"))

        for btn in bts:
            ttk.Button(f2,
                       style="App.TButton",
                       text=btn[0],
                       underline=btn[1],
                       command=btn[2],).pack(fill=tk.X, padx=5, pady=5)
            self.parent.bind(btn[3], btn[2])

       
        f2.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5, expand=0)
        f1.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=1)
        f0.pack(fill=tk.BOTH, expand=1)

    def on_open(self):
        
        self.start_date.year.set(1970)
        self.start_date.month.set(1)
        self.start_date.day.set(1)

        self.end_date.set_today()

    def on_print_date(self, evt=None):

        if self.start_date.get_date(self)==False:return
               
        if self.end_date.get_date(self)==False:
            return
        else:
            msg = "{0}: {1}\n{2}: {3}".format(self.start_date.description,self.start_date.get_date(self),
                                              self.end_date.description,self.end_date.get_date(self))
            
        messagebox.showinfo(self.parent.title(), msg, parent=self)            
        
    def on_set_today(self, evt=None):
        self.start_date.set_today()
        self.end_date.set_today()

    def on_compare(self, evt=None):

        if self.start_date.get_date(self)==False:
            return
        else:
            d0 = self.start_date.get_date(self)

        if self.end_date.get_date(self)==False:
            return

        else:
            d1 = self.end_date.get_date(self)

        if d0 > d1:
            msg = "{0} is greater than {1}".format(self.start_date.description, self.end_date.description)
        elif d0 < d1:
            msg = "{0} is less than {1}".format(self.start_date.description, self.end_date.description)
        else:
            msg = "{0} is equal than {1}".format(self.start_date.description, self.end_date.description)
            
        messagebox.showinfo(self.parent.title(), msg, parent=self)                   

    def on_difference(self, evt=None):

        if self.start_date.get_date(self)==False:
            return
        else:
            d0 = self.start_date.get_date(self)

        if self.end_date.get_date(self)==False:
            return

        else:
            d1 = self.end_date.get_date(self)

        delta = d1 - d0

        msg = "Difference between {0} and {1} in days is:\n{2}".format(self.start_date.description, self.end_date.description, delta.days)

        messagebox.showinfo(self.parent.title(), msg, parent=self)                   

        
      
    def on_close(self, evt=None):
        self.parent.on_exit()

class App(tk.Tk):
    """Start here"""

    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.on_exit)
            
        self.set_title()
        
        w = Main(self,)
        w.on_open()
        w.pack(fill=tk.BOTH, expand=1)
        
    def set_title(self):
        s = "{0}".format("Calendarium Demo")
        self.title(s)
        
    def on_exit(self):
        """Close all"""
        if messagebox.askokcancel(self.title(), "Do you want to quit?", parent=self):
            self.destroy()               
    
if __name__ == '__main__':
    app = App()
    app.mainloop()
