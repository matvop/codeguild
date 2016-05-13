from django.http import HttpResponse
from django.shortcuts import render
from . import logic


def save_vote(request):
    vote = request.POST['icecream']
    logic.save_vote(vote)
    return render(request, 'polls/summary.html')

def render_summary(request):
    save_vote(request)
    results = logic.get_summary()
    context = {
        'results': results,
    }
    return render(request, 'polls/summary.html', context)

def render_index(request):
    return render(request, 'polls/index.html')
