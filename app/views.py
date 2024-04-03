from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def home_page_view(request):
    return render(request, "teams.html")


def team_details_view(request, team_name):
    context = {"team_name": team_name, "members": ["one", "two", "three"]}
    return render(request, "team_details.html", context)
