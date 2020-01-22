"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import getopt
import sys
import calendar
from datetime import datetime

c = calendar.TextCalendar(calendar.SUNDAY)


x = datetime.now()
current_year = x.year
current_month = x.month

print('Argument list:', str(sys.argv))
print('Number of args', len(sys.argv))


def cal_function(yy=current_year, mm=current_month):
    try:
        if len(sys.argv) == 1:
            return c.formatmonth(current_year, current_month)
    #        return c.formatmonth(current_year, current_month)
        elif len(sys.argv) == 2:
            return c.formatmonth(current_year, int(sys.argv[1]))
          # return 'Month provided', sys.argv[1]
        elif len(sys.argv) == 3:
            return c.formatmonth(int(sys.argv[2]), int(sys.argv[1]))
    #        return 'Month and year provided', sys.argv[1], sys.argv[2]
    #        return c.formatmonth(current_year, sys.argv[1])
    except:
        return 'Please provide a numerical month and year(optional), ex: py 14_cal.py month year'


print(cal_function())
