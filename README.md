# Calendarium
a primitive light class to manage calendar date in tkinter projects using datetime lib.

![alt tag](https://user-images.githubusercontent.com/5463566/63707533-6e8a7b00-c832-11e9-8aa1-81784ec003a7.png)


Provides a primitive class widget to manage calendar date in tkinter projects.

## How import;

from calendarium import Calendarium

## How nstantiate in your frame:

self.start_date = Calendarium(self,"Start Date")

## How pack:

f is a tkinter widget such as Frame

if use row and col

self.start_date.get_calendarium(f, row, col)

If use pack()

self.start_date.get_calendarium(f,)

## How set today date:

self.start_date.set_today()

## How check if a date is right formated do something like:

before you must import this:
from tkinter import messagebox

```python

if self.start_date.get_date()==False:
    msg = "Date format error"
    messagebox.showerror('My Title', msg, parent=self)
```


Notice that in the spinbox widget we allowed only integers.

Calendarium use datetime.date to set/get date.

** Calendarium it's primitive but It's working and it's light. **

