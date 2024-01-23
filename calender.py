# Display Calendar year whose  month you want to display
import calendar

year=int(input("Enter year: "))
month=int(input("Enter month: "))

calendar= calendar.month(year,month)

print(calendar)