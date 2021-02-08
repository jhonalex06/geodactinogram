#import pdb; pdb.set_trace() debuger

# Django
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime

def hello_world(request):
    # Return a greeting

    return HttpResponse('Oh, hi! Current server time is {now}'.format(
        now=str(datetime.now().strftime('%b %dth, %Y - %H:%M hrs'))
        ))

def sort_integers(request):
    # Return a JSON response with sorted integers.
    numbers = [int (i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)

    data = {
        'status':'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfully.'
    }

    return JsonResponse(data)
    #return HttpResponse(str(numbers))

def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Geodactinogram'.format(name)

    return HttpResponse(message)