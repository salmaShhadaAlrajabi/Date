# Date
Write a class named “Date” that handles the date, containing day, month, and year. 
The class should provide the following:
a. You should be able to instantiate an instance using a constructor as follows
d1 = Date(23, 12, 2020)
b. The class has a method “order” that returns the order of a specific date in the year, e.g.,
d3 = Date(15, 2, 2020)
print(d3.order()) 
➔ The output should be 46, since 15/2 is the 46th day in the year. 
c. The print statement should print the date in the format dd/mm/yyyy, e.g.,
d4 = Date(5, 6, 1997)
print(d4) 
➔ The output should be 5/6/1997
d. You use addition to find the date after a number of days, e.g.,
d2 = d1 + 22 
➔ d2 is the date 22 days after d1
e. You use subtraction to find the difference (number of days) between two dates, e.g.,
number_of_days = d2 – d1 
f. You use comparison to find if a date precedes the other, e.g.,
if d1 < 22:
do_something
