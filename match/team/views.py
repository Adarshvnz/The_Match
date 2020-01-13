from django.shortcuts import render
from .models import team, matchset
from django.views.generic import (CreateView, TemplateView,
                                 ListView, DetailView)
from django.contrib.auth.mixins import(
    LoginRequiredMixin,
    PermissionRequiredMixin
)
# Create your views here.
class CreateTeam(LoginRequiredMixin, CreateView):
    fields = ( "userid", "team_name", "team_motto", "contact_no", "location", "confirm")
    model = team

class SingleTeam(LoginRequiredMixin, DetailView):
    model = team

class ListTeam(ListView):
    model = team

class CreateMatch(LoginRequiredMixin, CreateView):
    fields = ("match_date", "team1", "team2", "match_location")
    model = matchset

class ListMatch(ListView):
    model = matchset
