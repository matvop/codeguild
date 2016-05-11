from django.http import HttpResponse
from django.shortcuts import render
from . import logic


# def render_submit(request):
#     """Renders the HTML for the submition result page."""
#     setup = request.POST['setup']
#     punchline = request.POST['punchline']
#     logic.save_joke(setup, punchline)
#     return HttpResponse('This will be HTML.')

def jokes(request):
    return render(request, 'jokes/jokes.html')
