get days in python
===

get today
```python
import datetime

currentDate = datetime.date.today()
print(currentDate)
```

get the number of days in month
```python
import calendar

daysInMonth = calendar.monthrange(currentDate.year, currentDate.month)
print(daysInMonth)
```
