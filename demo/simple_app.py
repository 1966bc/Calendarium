#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from calendarium import Calendarium


class Main(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.init_ui()

    def init_ui(self):
        f0 = ttk.Frame(self, relief=tk.RIDGE, borderwidth=2, padding=8)
        f1 = ttk.Frame(f0, relief=tk.RIDGE, borderwidth=2, padding=8)

        self.start_date = Calendarium(f1, "Start Date")
        self.end_date = Calendarium(f1, "End Date")

        self.start_date.pack(padx=4, pady=4)
        self.end_date.pack(padx=4, pady=4)

        f2 = ttk.Frame(f0, relief=tk.RIDGE, borderwidth=2, padding=4)

        bts = (
            ("Print Date", 0, self.on_print_date, "<Alt-p>"),
            ("Set Today", 4, self.on_set_today, "<Alt-t>"),
            ("Compare", 0, self.on_compare, "<Alt-c>"),
            ("Difference", 0, self.on_difference, "<Alt-d>"),
            ("Close", 4, self.on_close, "<Alt-e>"),
        )

        for text, underline, cmd, key in bts:
            ttk.Button(
                f2,
                style="App.TButton",
                text=text,
                underline=underline,
                command=cmd,
            ).pack(fill=tk.X, padx=5, pady=5)
            self.parent.bind(key, cmd)

        f2.pack(side=tk.RIGHT, fill=tk.Y, padx=5, pady=5, expand=0)
        f1.pack(side=tk.LEFT, fill=tk.BOTH, padx=5, pady=5, expand=1)
        f0.pack(fill=tk.BOTH, expand=1)

    def on_open(self):
        # Calendarium uses StringVar: set strings to be explicit
        self.start_date.year.set("1970")
        self.start_date.month.set("1")
        self.start_date.day.set("1")

        self.end_date.set_today()

    # ---------------------- helpers ----------------------
    def _label(self, cal_widget: Calendarium) -> str:
        # Calendarium is a LabelFrame, so we can read its label text
        return cal_widget.cget("text")

    def _require_date(self, cal_widget: Calendarium):
        d = cal_widget.get_date()
        if d is None:
            messagebox.showwarning(self.parent.title(), f"Invalid date in '{self._label(cal_widget)}'", parent=self)
        return d

    # ---------------------- actions ----------------------
    def on_print_date(self, evt=None):
        d0 = self._require_date(self.start_date)
        if d0 is None:
            return
        d1 = self._require_date(self.end_date)
        if d1 is None:
            return
        msg = f"{self._label(self.start_date)}: {d0}\n{self._label(self.end_date)}: {d1}"
        messagebox.showinfo(self.parent.title(), msg, parent=self)

    def on_set_today(self, evt=None):
        self.start_date.set_today()
        self.end_date.set_today()

    def on_compare(self, evt=None):
        d0 = self._require_date(self.start_date)
        if d0 is None:
            return
        d1 = self._require_date(self.end_date)
        if d1 is None:
            return

        if d0 > d1:
            msg = f"{self._label(self.start_date)} is greater than {self._label(self.end_date)}"
        elif d0 < d1:
            msg = f"{self._label(self.start_date)} is less than {self._label(self.end_date)}"
        else:
            msg = f"{self._label(self.start_date)} is equal to {self._label(self.end_date)}"
        messagebox.showinfo(self.parent.title(), msg, parent=self)

    def on_difference(self, evt=None):
        d0 = self._require_date(self.start_date)
        if d0 is None:
            return
        d1 = self._require_date(self.end_date)
        if d1 is None:
            return

        delta = d1 - d0
        msg = f"Difference between {self._label(self.start_date)} and {self._label(self.end_date)} in days is:\n{delta.days}"
        messagebox.showinfo(self.parent.title(), msg, parent=self)

    def on_close(self, evt=None):
        self.parent.on_exit()


class App(tk.Tk):
    """Start here"""

    def __init__(self):
        super().__init__()
        self.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.set_title()
        w = Main(self)
        w.on_open()
        w.pack(fill=tk.BOTH, expand=1)

    def set_title(self):
        self.title("Calendarium Demo")

    def on_exit(self):
        if messagebox.askokcancel(self.title(), "Do you want to quit?", parent=self):
            self.destroy()


if __name__ == "__main__":
    app = App()
    app.mainloop()
