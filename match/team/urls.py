from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'team'

urlpatterns = [
    path('',views.ListTeam.as_view(),name='all'),
    path('new/',views.CreateTeam.as_view(),name='createteam'),
    path('detail/in/<slug>/',views.SingleTeam.as_view(),name='teamdetail'),
    path('setmatch/',views.CreateMatch.as_view(),name='creatematch'),
    path('matchlist/',views.ListMatch.as_view(),name='matchlist'),

 ]
