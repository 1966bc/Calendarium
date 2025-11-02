# Calendarium

A primitive light class to manage calendar date in tkinter projects using datetime lib.

![alt tag](https://user-images.githubusercontent.com/5463566/193236323-077a6141-f4f5-463b-9fd1-a0eb1aa4a0e3.png)


Provides a primitive class widget to manage calendar date in tkinter projects.

## How import:

```python
from calendarium import Calendarium
```

## How instantiate in your frame:

```python
self.start_date = Calendarium(self,"Start Date")
```

## How pass background color, optional:

```python
self.start_date = Calendarium(self,"Start Date", base_bg_color=(240, 240, 237))
```

## How pack:

- if use grid method

```python
 self.start_date.grid(row=r, column=c, sticky=tk.W) 
```

- If use pack method

```python
self.start_date.pack(padx=2, pady=2)
```

## How set today date:

```python
self.start_date.set_today()
```

## How check if a date is right formated:

```python
if not self.start_date.is_valid:return
```


Notice that in the spinbox widget we allowed only integers.

Calendarium use datetime.date to set/get date.

#  Calendarium it's primitive but It's working and it's light.
