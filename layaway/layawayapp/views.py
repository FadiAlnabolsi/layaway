from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Ticket, Events

# Create your views here.
def homepage(request):
    if request.user.is_anonymous():
        return render(request, 'homepage.html')
    else:
        return render(request, 'homepage.html')

def about_us(request):
    if (request.user.is_anonymous()):
        return render(request, 'about_us.html')

    data = {}
    user = User.objects.get(user=request.user)
    data['user'] = user

    return render('about_us.html', {
        'data': data
        })

def my_account(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('/')

    tickets = Ticket.objects.filter(customer=request.user)
    user = User.objects.get(user=request.user)

    data = {}

    data['tickets'] = tickets
    data['user'] = user

    return render(request, 'my_account.html', {
        'data':data
        })

def events(request):
    events = Events.objects.all().order_by('date')
    data = {}
    data['events'] = events

    if (request.user.is_anonymous()):
        return render(request, 'events.html', {
            'data':data
            })

    #paginator for events

    data = {}
    user = User.objects.get(user=request.user)
    data['user'] = user

    return render(request, 'events.html', {
        'data':data
        })

def event_instance(request, id):
    event = Events.objects.get(id=id)
    data = {}
    data['event'] = event

    if (request.user.is_anonymous()):
        return render(request, 'event.html', {
            'data':data
            })

    data = {}
    user = User.objects.get(user=request.user)
    data['user'] = user

    return render(request, 'event.html', {
        'data':data
        })




