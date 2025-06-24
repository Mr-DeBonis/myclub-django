from django.urls import path

from events import views

urlpatterns = [
    # Path Converters
    # int: numbers
    # str: strings
    # path: whole urls
    # slug: hyphen-and_underscores_stuff
    # UUID: universally unique identifier

    path('', views.home, name="home"),
    path('<int:year>/<str:month>/', views.home, name="home"),
    path('events', views.all_events, name="list-events")
]
