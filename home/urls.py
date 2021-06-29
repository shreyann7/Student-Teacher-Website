from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.index,name='home'),
    
    path('about',views.about,name='about'),
    
    path('contact',views.contact,name='contact'),

    path('campus',views.campus,name='campus'),
    
    path('students',views.students,name='students'),

    path('faculty',views.faculty,name='faculty'),

    path('contactfaculty',views.contactfaculty,name='contactfaculty'),

    path('TechnicalClubs',views.TechnicalClubs,name='TechnicalClubs'),
    path('CulturalClubs',views.CulturalClubs,name='CulturalClubs'),
    path('SportsClub',views.SportsClub,name='SportsClub'),
    


]
