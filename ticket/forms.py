from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['customer_name', 'ticket_subject', 'ticket_body', 'ticket_status']
