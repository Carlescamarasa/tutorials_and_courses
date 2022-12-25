### Dates ###

from datetime import datetime, time, date, timedelta

now = datetime.now()

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)
    print(date.timestamp())

# Indica una marca de tiempo única para cada momento
timestamp = now.timestamp()

print(timestamp)

# Lo mínimo que necesitamos para definir una fecha (año, mes y día)
year_2023 = datetime(2023, 1, 1, 3)

ahora =  datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

print_date(year_2023)

# TIME

current_time = time(21, 6, 0)

print(current_time.hour)
print(current_time.minute)
print(current_time.second)

# DATE

current_date = date.today()

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday()) # Returns int: Monday == 0, Tuesday == 1, etc

current_date = date(2022, 12, 25)

print(current_date.year)
print(current_date.month)
print(current_date.day)
print(current_date.weekday())

# Podemos alterar los datos capturados en date()
current_date = date(current_date.year, current_date.month - 1, current_date.day)
print(current_date)

# Los objetos deben de ser del mismo tipo para poderse restar (date, time o datetime)
diff = year_2023 - now
print(diff)

diff = year_2023.date() - current_date
print(diff)

# print(year_2023 - current_date)

# TIMEDELTA

start_timedelta = timedelta(200, 100, 100, weeks = 10)

end_timedelta = timedelta(300, 100, 100, weeks= 13)

print(end_timedelta - start_timedelta)
print(end_timedelta + start_timedelta)
