from datetime import date, datetime, time
 

data = (2023, 1, 4)
print(data)

print(date.today())

data_hora = datetime(2023, 7, 10)
print(data_hora)

print(datetime.today())

hora = time(10, 20, 0)
print(hora)

date_string = "2023-05-01" 
date_string = datetime.strptime(date_string, "%Y-%d-%m")
print(date_string)