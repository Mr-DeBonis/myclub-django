import calendar
from calendar import HTMLCalendar
from datetime import datetime

from django.shortcuts import render


# Create your views here.
def home(request, year=datetime.now().year, month=datetime.now().strftime('%B')):
    name = "John"
    month = month.title()
    # Convert month from name to number
    month_number = int(list(calendar.month_name).index(month))

    # Create a calendar
    cal = HTMLCalendar().formatmonth(theyear=year, themonth=month_number)

    # Get current year
    now = datetime.now()
    current_year = now.year

    # Get current time
    time = now.strftime('%I:%M %p')

    return render(request, 'events/home.html', {
        "name": name,
        "year": year,
        "month": month,
        "cal": cal,
        "current_year": current_year,
        "time": time,
    })
