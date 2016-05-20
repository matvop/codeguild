from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse
from . import models
from . import logic


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


def render_index(request):
    flutts = logic.get_all_flutts()
    context = {
        'flutts': flutts,
    }
    return render(request, 'flutter/index.html', context)
