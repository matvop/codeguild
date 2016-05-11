from django.http import HttpResponse
from django.shortcuts import render
from . import logic


def render_page(request):
    """Renders the HTML for some random page."""
    return HttpResponse('This will be HTML.')

def jokes(request):
    return render(request, 'jokes/jokes.html')
