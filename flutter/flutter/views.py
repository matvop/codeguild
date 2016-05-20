from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from . import settings
from django.contrib.auth.decorators import login_required
from . import models
from . import logic


def render_login(request):
    next = request.GET.get('next', '/')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print(username)
        print(password)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(next)
            else:
                return HttpResponse("Inactive User.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    return render(request, 'flutter/login.html', {'redirect_to': next})

def render_logout(request):
    logout(request)
    return HttpResponseRedirect(settings.LOGIN_URL)

def render_user_flutts(request):
    user_name = request.GET['query']
    flutts = logic.get_all_flutts_for_user(user_name)
    context = {
        'user_name': user_name,
        'flutts': flutts,
    }
    return render(request, 'flutter/results.html', context)

def render_index(request):
    flutts = logic.get_all_flutts()
    context = {
        'flutts': flutts,
    }
    return render(request, 'flutter/index.html', context)

@login_required
def render_ack(request):
    user_name = request.POST['user-name']
    comment = request.POST['comment']
    logic.save_flutt(user_name, comment)
    context = {
        'user_name': user_name,
        'comment': comment,
    }
    return render(request, 'flutter/ack.html', context)

def render_form_page(request):
    return render(request, 'flutter/form.html')
