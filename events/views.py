import calendar
import io
from calendar import HTMLCalendar
from datetime import datetime

from django.http import HttpResponseRedirect, FileResponse
from django.shortcuts import render
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas

from events.forms import VenueForm
from events.models import Event, Venue


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


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'events/event_list.html', {'event_list': event_list})


def add_venue(request):
    submitted = False

    if request.method == "POST":
        form = VenueForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')
    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True

    context = {
        'form': form,
        'submitted': submitted,
    }
    return render(request, 'events/add_venue.html', context=context)


def list_venues(request):
    venue_list = Venue.objects.all()
    return render(request, 'events/venue.html', {'venue_list': venue_list})


def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)

    return render(request, 'events/show_venue.html', {'venue': venue})

def venue_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textObj = c.beginText()
    textObj.setTextOrigin(inch, inch)
    textObj.setFont("Helvetica", 14)

    venues = Venue.objects.all()
    lines = []

    for venue in venues:
        lines.append(venue.name)
        lines.append(venue.address)
        lines.append(venue.zip_code)
        lines.append(venue.phone)
        lines.append(venue.web)
        lines.append(venue.email_address)
        lines.append(" ")

    for line in lines:
        textObj.textLine(line)

    c.drawText(textObj)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')



    pass
