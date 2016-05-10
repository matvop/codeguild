from django.http import HttpResponse
from .logic import check_count


def render_word_and_count(request):
    word = request.GET['word']
    if word:
        result = check_count(word)
        return(HttpResponse(result))
    else:
        return HttpResponse(status=400)
