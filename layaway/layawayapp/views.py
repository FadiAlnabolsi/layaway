from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.models import User
from .models import Ticket, Events, TicketInfo


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
    user = User.objects.get(username=request.user.username)
    data['user'] = user

    return render(request, 'about_us.html', {
        'data': data
        })

def my_account(request):
    if request.user.is_anonymous():
        return HttpResponseRedirect('/')

    tickets = Ticket.objects.filter(customer=request.user)
    user = User.objects.get(username=request.user.username)

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

    user = User.objects.get(username=request.user.username)
    data['user'] = user

    return render(request, 'events.html', {
        'data':data
        })

def event_instance(request, id):
    event = Events.objects.get(id=id)
    data = {}
    data['event'] = event
    data['alreadyPurchased'] = False

    if (request.user.is_anonymous()):
        return render(request, 'event.html', {
            'data':data
            })

    TI = TicketInfo.objects.get(event=event)

    try:
        Ticket.objects.get(customer=request.user, event=event)
        data['alreadyPurchased'] = True

    except Exception as e:
        data['alreadyPurchased'] = False

    user = User.objects.get(username=request.user.username)
    data['user'] = user
    data['ticketInfo'] = TI

    totalTix = TI.maxTickets
    usedTix = Ticket.objects.filter(event=event).count()
    financePrice = float(TI.price) * .25

    remainingTix = totalTix - usedTix

    if remainingTix <= 0:
        data['canPurchase'] = False
    else:
        data['canPurchase'] = True

    data['totalTix'] = TI.maxTickets
    data['usedTix'] = Ticket.objects.filter(event=event).count()
    data['remainingTix'] = TI.maxTickets - data['usedTix']
    data['financePrice'] = financePrice

    return render(request, 'event.html', {
        'data':data
        })

def purchaseTix(request, id):
    event = Events.objects.get(id=id)
    data = {}
    data['event'] = event

    if request.user.is_anonymous():
        return render(request, 'event.html', {
            'data':data
            })

    try:
        Ticket.objects.get(customer=request.user, event=event)
        data['alreadyPurchased'] = True
    except Exception as e:
        data['alreadyPurchased'] = False

    if data['alreadyPurchased'] == True:
        return HttpResponseRedirect('/events/' + event.id)

    TI = TicketInfo.objects.get(event=event)

    Ticket.objects.create(
                customer=request.user, 
                event=event, 
                price=TI.price,
                ticket_type=TI.ticket_type,
                )

    return HttpResponseRedirect('/my_account')





