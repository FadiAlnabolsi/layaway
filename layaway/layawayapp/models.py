from django.db import models
from django.contrib.auth.models import User

TICKET_CHOICES = (
    ('VIP', 'VIP'),
    ('GEN', 'GENERAL')
)

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=12, null=True, blank=True)

class Artist(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    biography = models.TextField()
    image = models.TextField()

class Events(models.Model):
    name = models.TextField()
    date = models.DateTimeField(auto_now=True)
    city = models.TextField()
    state = models.TextField()
    artist = models.ForeignKey(Artist, related_name='artist', null=True, blank=True)

class TicketInfo(models.Model):
    ticket_type = models.CharField(max_length=12, choices=TICKET_CHOICES)
    maxTickets = models.IntegerField()
    event = models.ForeignKey(Events, related_name='ticket_info_events')

class Ticket(models.Model):
    ticket_type = models.CharField(max_length=12, choices=TICKET_CHOICES)
    event = models.ForeignKey(Events, related_name='ticket_events')
    price = models.DecimalField(max_digits=7, decimal_places=2)
    customer = models.ForeignKey(User)
    confirmation_number = models.CharField(max_length=20)
    ticket_number = models.CharField(max_length=20)

