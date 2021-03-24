from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import IntegrityError
from django.db.models import Q
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.db.models import Q
from .forms import *
from .models import *
import requests
import json


def loginView(request):

    template_name = 'auth/login.html'
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    if request.method == 'POST':

        form = UserLoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # str_relace = str.replace(username, '/', f'')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'login was successful')
            return redirect('/dashboard/')
        else:
            messages.warning(
                request, f'login Error !!!! Provide Correct Username And Password')
            return redirect('/')
    else:
        form = UserLoginForm()

    return render(request, template_name, {'form': form})


def registerView(request):

    template_name = 'auth/register.html'

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(
                request, f'Account created for {username}! Now Login')
            form.save()
            return redirect('/login/')
        else:
            messages.warning(
                request, f'Something went wrong please fil in the form correctly')
            form.save()
            return redirect('/registration/')

    else:
        form = UserRegisterForm()

    return render(request, template_name, {'form': form})


class DashboardView(View):


    
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect("account:login")
        try:

            records = RecordModel.objects.filter(user=request.user.farmermodel)
            total_cash = RecordModel.get_total_cash(self, request)
            total_kilo = RecordModel.get_total_kilos(self, request)
            farmers = FarmerModel.objects.count()

            profile = request.user.farmermodel

            context = {
                "records": records,
                "profile": profile,
                "farmers": farmers,
                "total_cash": total_cash,
                "total_kilo": total_kilo,
            }

            template_name = 'pages/dashboard.html'

            return render(self.request, template_name, context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have a Profile, Contact Admin.")
            return redirect("account:logout")






def loguotView(request): 
    logout(request)  
    messages.success(request, f'You Have logout !!!')
    return redirect('/login/')
