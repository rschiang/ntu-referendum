from django.shortcuts import render
from referendum.models import Referendum

def home(request):
    return render(request, 'referendum.html', {
        'items': Referendum.objects.all(),
    })
