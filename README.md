# Calendarium
a primitive light class to manage calendar date in tkinter projects using datetime lib.

![alt tag](https://user-images.githubusercontent.com/5463566/63707533-6e8a7b00-c832-11e9-8aa1-81784ec003a7.png)


Provides a primitive class widget to manage calendar date in tkinter projects.

## How import:

```python
from calendarium import Calendarium
```

## How instantiate in your frame:

```python
self.start_date = Calendarium(self,"Start Date")
```

## How pack:

f is a tkinter widget such as Frame,LabelFrame

# if use grid method

```python
self.start_date.get_calendarium(f, row, col)
```

# If use pack method

```python
self.start_date.get_calendarium(f,)
```

## How set today date:

```python
self.start_date.set_today()
```

## How check if a date is right formated:

```python
if self.start_date.get_date(self)==False:return
```


Notice that in the spinbox widget we allowed only integers.

Calendarium use datetime.date to set/get date.

** Calendarium it's primitive but It's working and it's light. **

