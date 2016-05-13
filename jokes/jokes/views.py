from django.http import HttpResponse
from django.shortcuts import render

from . import logic


def render_ack(request):
    setup = request.POST['setup']
    punchline = request.POST['punchline']
    joke = {
                'setup': setup,
                'punchline': punchline,
    }
    logic.save_joke(joke)
    template_arguments = {
        'joke': joke,
    }
    return render(request, 'jokes/ack.html', template_arguments)

def favicon(request):
    return render(request, 'static/jokes/favicon.ico')

def render_form_page(request):
    return render(request, 'jokes/form.html')

def render_index(request):
    jokes = logic.get_all_jokes()
    context = {
        'jokes': jokes,
    }
    return render(request, 'jokes/index.html', context)
