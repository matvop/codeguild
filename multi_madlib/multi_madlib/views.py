from django.http import HttpResponse


def build_madlib(request):
    verb = str(request.GET['verb'])
    noun = str(request.GET['noun'])
    name = str(request.GET['name'])
    adj = str(request.GET['adj'])
    return ('Once upon a ' + noun + '. There was a man called ' + name + ' .'
        'He was very ' + adj + ', but he could ' + verb + ' all nigt long.')
