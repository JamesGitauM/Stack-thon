from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def index(request):
    data = {
        'name': 'John Doe',
        'email': 'john@example.com'
    }

    # return JsonResponse(data)
    template='core/index-4.html'
    return render(request, template)