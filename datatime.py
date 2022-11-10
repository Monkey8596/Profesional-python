
import datetime


my_time = datetime.datetime.now()
print(my_time)

print('///////////////////////')

my_date = datetime.date.today()
print(f'Year: {my_date.year}')
print(f'Month: {my_date.month}')
print(f'Day: {my_date.day}')

print('///////////////////////')

from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

my_str = my_datetime.strftime('%d/%m/%Y')
print(f'LATAM: {my_str} ')

my_str = my_datetime.strftime('%m/%d/%Y')
print(f'USA: {my_str} ')

my_str = my_datetime.strftime('The year is %Y ')
print(f'Random: {my_str} ')


