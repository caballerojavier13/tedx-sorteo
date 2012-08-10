from django.template import Context, loader
from sorteo.models import Sorteo
from django.http import HttpResponse
import random 

def index(request):
    person_list = Sorteo.objects.all()
    # XXX list consturctor didnt work, i need a list for the shuffle
    # although it was made for less than 2000 items 
    lista = [i for i in person_list]
    # Here is where magic happens!
    random.shuffle(lista, random.random)
    # I use i+1 because humans are not yet ready to count starting from 0 
    result_list = [(i+1,x) for i,x in enumerate(lista[:100])]

    t = loader.get_template('index.html')
    c = Context({
            'person_list': result_list,
    })
    return HttpResponse(t.render(c))
