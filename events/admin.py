from django.contrib import admin

from events.models import Venue, MyClubUser, Event

admin.site.register(Venue)
admin.site.register(MyClubUser)
admin.site.register(Event)
