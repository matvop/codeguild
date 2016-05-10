from django.http import HttpResponse


def render_madlib1(request):
    verb = request.GET['verb']
    noun = request.GET['noun']
    name = request.GET['name']
    adj = request.GET['adj']
    if all((verb, noun, name, adj)):
        result = ('Once upon a ' + noun + '. There was a man called ' + name + '.'
            ' He was very ' + adj + ', and he could ' + verb + ' all nigt long.')
        return HttpResponse(result)
    else:
        return HttpResponse(status=400)

def render_madlib2(request):
    verb = request.GET['verb']
    noun = request.GET['noun']
    name = request.GET['name']
    adj = request.GET['adj']
    if all((verb, noun, name, adj)):
        result = ('Once upon a ' + noun + '. There was a man called ' + name + '.'
            ' He was very ' + adj + ', and he could ' + verb + ' all nigt long.')
        return HttpResponse(result)
    else:
        return HttpResponse(status=400)

def render_madlib3(request):
    verb = request.GET['verb']
    noun = request.GET['noun']
    name = request.GET['name']
    adj = request.GET['adj']
    if all((verb, noun, name, adj)):
        result = ('Once upon a ' + noun + '. There was a man called ' + name + '.'
            ' He was very ' + adj + ', and he could ' + verb + ' all nigt long.')
        return HttpResponse(result)
    else:
        return HttpResponse(status=400)
