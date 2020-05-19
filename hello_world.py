# Started playing with python
int_str = 100
print(int_str)
long_str = 125478963012365478965
print(long_str)

# String basic methods
string = "'single'"
print(string)
string = '"double"'
print(string)
string = "upper"
print(string.upper())
string = "lower"
print(string.lower())
string = "capitalize"
print(string.capitalize())
string = "count"
print(string.count("n"))
string = "endswith"
print(string.endswith("s"))

# String Formatting method
first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
output = "Hello, " + last_name + " " + first_name
print(output)
output = "Hello, {} {}".format(first_name, last_name)
print(output)
output = "Hello, {1} {0}".format(first_name, last_name)
print(output)
output = f"Hello, {first_name} {last_name}"
print(output)

# Integer Processing
first_number = 10  # input("Please enter a number: ")
print("Print int with stringas first number: " + str(first_number))
last_number = 2  # input("Please enter a number: ")
print("Print int with stringas last number: " + str(last_number))

print("Addition: " + str(int(first_number + last_number)))
print("Subraction: " + str(int(first_number - last_number)))
print("Multiply: " + str(int(first_number * last_number)))
print("Division: " + str(int(first_number / last_number)))
print("Power: " + str(int(first_number ** last_number)))

first_number = input("Please enter a first number: ")
last_number = input("Please enter a last number: ")

print("Addition: " + str(int(first_number) + int(last_number)))
print("Subraction: " + str(int(first_number) - int(last_number)))
print("Multiply: " + str(int(first_number) * int(last_number)))
print("Division: " + str(int(first_number) / int(last_number)))
print("Power: " + str(int(first_number) ** int(last_number)))

# Float Processing
first_number = 15.4  # input("Please enter a number: ")
print("Print int with stringas first number: " + str(first_number))
last_number = 2.4  # input("Please enter a number: ")
print("Print int with stringas last number: " + str(last_number))

print("Addition: " + str(float(first_number + last_number)))
print("Subraction: " + str(float(first_number - last_number)))
print("Multiply: " + str(float(first_number * last_number)))
print("Division: " + str(float(first_number / last_number)))
print("Power: " + str(float(first_number ** last_number)))

first_number = input("Please enter a first number: ")
last_number = input("Please enter a last number: ")

print("Addition: " + str(float(first_number) + float(last_number)))
print("Subraction: " + str(float(first_number) - float(last_number)))
print("Multiply: " + str(float(first_number) * float(last_number)))
print("Division: " + str(float(first_number) / float(last_number)))
print("Power: " + str(float(first_number) ** float(last_number)))

# Date library datetime method
from datetime import datetime, timedelta

today = datetime.now()
print("Today day: " + str(today.day))
print("Today date: " + str(today.date()))
print("Today month: " + str(today.month))
print("Today year: " + str(today.year))
print("Today weekday: " + str(today.weekday()))
print("Today hour: " + str(today.hour))
print("Today minute: " + str(today.minute))
print("Today second: " + str(today.second))
print("Today microsecond: " + str(today.microsecond))
print("Today now: " + str(today.now()))

# Date library timedelta method
one_day = timedelta(days=1)
print("Yesterday was " + str(today - one_day))

one_week = timedelta(weeks=1)
print("Lat week was " + str(today - one_week))

birthday = input("When is your birthday (dd/mm/yyyy): ")
birthday_date = datetime.strptime(birthday, "%d/%m/%Y")

print("Birthday : " + str(birthday_date))

one_year = timedelta(days=365)
next_birthday = birthday_date + one_year
print("One year before day: " + str(next_birthday.weekday()))
