from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render
from django.contrib.auth import authenticate, login


# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')
    # return HttpResponse("This is aboutpage")


def faculty(request):
    return render(request, 'faculty.html')
    # return HttpResponse("This is facultypage")


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email,
                          desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message has been sent :)')

    def __str__(self):
        return self.name

    return render(request, 'contact.html')
    # return HttpResponse("This is contactpage")


def TechnicalClubs(request):
    return render(request, 'TechnicalClubs.html')
    # return HttpResponse("This is academicspage")


def CulturalClubs(request):
    return render(request, 'CulturalClubs.html')
    # return HttpResponse("This is academicspage")


def SportsClub(request):
    return render(request, 'sportsclub.html')
    # return HttpResponse("This is academicspage")


def campus(request):
    return render(request, 'campus.html')


def students(request):
    return render(request, 'students.html')


def contactfaculty(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        facultyname = request.POST.get('facultyname')
        desc = request.POST.get('desc')
        contactfaculty = faculty(name=name, email=email,
                                 facultyname=facultyname, date=datetime.today())
        contactfaculty.save()
        messages.success(request, 'Your Message has been sent :)')

    def __str__(self):
        return self.facultyname

    return render(request, 'contactfaculty.html')
