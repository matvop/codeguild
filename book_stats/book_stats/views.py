from django.http import HttpResponse
from django.shortcuts import render
from . import logic

def render_top10(request):
    result = logic.get_top_10()
    return(HttpResponse(result))

def render_book_title(request):
    result = logic.get_book_title()
    return(HttpResponse(result))

def render_word_and_count(request):
    word = request.GET['word']
    if word:
        result = logic.check_count(word)
        return(HttpResponse(result))
    else:
        return HttpResponse(status=400)

def book_stats(request):
    return render(request, 'book_stats/book_stats.html')

top10 = logic.get_top_10
