from django.urls import path
from .views import *

app_name = 'account'
urlpatterns = [
    path('login/', loginView, name='login'),
    path('', loginView, name='login'),
    path('registration/', registerView, name='registration'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('logout/', loguotView, name='logout'),
]