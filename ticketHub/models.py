from django.contrib.auth.models import User
from django.db import models
class EventDb(models.Model):
    Poster = models.ImageField(upload_to='static/media', blank=True, null=True)
    Event_title = models.CharField(max_length=30, null=True)
    Date = models.DateField()
    Time = models.TimeField(null=True)
    Location = models.CharField(max_length=100)
    approved = models.BooleanField(default=False)

    advanced_price = models.IntegerField(default=0)
    gate_price = models.IntegerField(default=0)
    vip_price = models.IntegerField(default=0)
    vvip_price = models.IntegerField(default=0)

    # Currency symbol
    currency_symbol = models.CharField(max_length=5, default='Ksh')

    def request_approval(self):
        self.approved = False
        self.save()

    def __str__(self):
        return "%s %s %s %s %s" % (self.Poster, self.Event_title, self.Date, self.Time, self.Location)

class Ticket(models.Model):
    TYPE_CHOICES = [
        ('advanced', 'Advanced'),
        ('gate', 'Gate'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP'),
    ]

    event = models.ForeignKey(EventDb, on_delete=models.CASCADE, null=True, blank=True)
    ticket_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Set the price based on the associated event and ticket type
        if self.event:
            if self.ticket_type == 'advanced':
                self.price = self.event.advanced_price * self.quantity
            elif self.ticket_type == 'gate':
                self.price = self.event.gate_price * self.quantity
            elif self.ticket_type == 'vip':
                self.price = self.event.vip_price * self.quantity
            elif self.ticket_type == 'vvip':
                self.price = self.event.vvip_price * self.quantity
            else:
                self.price = 0

        super().save(*args, **kwargs)


class Payment(models.Model):
    calculated_amount = models.IntegerField(null=True)
    phone_number = models.CharField(max_length=12, null=True)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for Event {self.ticket.event.id} - ${self.calculated_amount} from {self.phone_number}"