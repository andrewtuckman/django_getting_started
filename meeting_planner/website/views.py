from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse


def welcome(request):
    return HttpResponse("Welcome to the Meeting Planner!")


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def aboutme(request):
    return HttpResponse("Hi! My name is Andrew Tuckman and I am a student at Boston University studying Computer "
                        "Science and Business. Currently, I work for Liberty Mutual Insurance in the Investments "
                        "department as a TechStart summer intern. I am learning Django to assist in my project at LMI.")