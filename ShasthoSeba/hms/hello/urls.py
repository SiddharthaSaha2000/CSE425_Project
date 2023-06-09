from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("doctors", views.doctors, name="doctors"),
    path("scrap", views.scrap, name="scrap"),
    path("scrape_doctorsSquare",
         views.scrape_doctorsSquare, name="doctorslist"),
    
]


#Activate : c:\Users\WIN\OneDrive\Desktop\hospital\ShashtoSeba\Scripts\Activate.ps1