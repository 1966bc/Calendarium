#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calendarium import Calendarium


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent
        
        self.text = tk.StringVar()
        
        self.init_ui()
          
    def init_ui(self):

        self.pack(fill=tk.BOTH, expand=1)

        f = ttk.Frame()

        self.start_date = Calendarium(self,"Start Date")
        self.end_date = Calendarium(self,"End Date")
        
        self.start_date.get_calendarium(f,)
        self.end_date.get_calendarium(f,)
              
        w = ttk.Frame()

        ttk.Button(w, text="Print Date", command=self.on_callback).pack()
        ttk.Button(w, text="Set Today", command=self.on_reset).pack()
        ttk.Button(w, text="Close", command=self.on_close).pack()

        f.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        w.pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

    def on_open(self):
        pass
        #self.start_date.set_today()
        #self.end_date.set_today()

    def on_callback(self,):

        if self.start_date.get_date(self)==False:return
            
            
        if self.end_date.get_date(self)==False:
            return
        else:
            msg = "{0}: {1}\n{2}: {3}".format(self.start_date.name,self.start_date.get_date(self),
                                              self.end_date.name,self.end_date.get_date(self))
            
        messagebox.showinfo(self.parent.title(), msg, parent=self)            
        
    def on_reset(self):
        self.start_date.set_today()
        self.end_date.set_today()
      
    def on_close(self):
        self.parent.on_exit()

class App(tk.Tk):
    """Start here"""

    def __init__(self):
        super().__init__()

        self.protocol("WM_DELETE_WINDOW", self.on_exit)
            
        self.set_title()
        self.set_style()
       
        frame = Main(self,)
        frame.pack(fill=tk.BOTH, expand=1)
        frame.on_open()

    def set_style(self):
        self.style = ttk.Style()
        #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        self.style.theme_use("clam")
        

    def set_title(self):
        s = "{0}".format('My App')
        self.title(s)
        
    def on_exit(self):
        """Close all"""
        if messagebox.askokcancel(self.title(), "Do you want to quit?", parent=self):
            self.destroy()               
    
if __name__ == '__main__':
    app = App()
    app.mainloop()
