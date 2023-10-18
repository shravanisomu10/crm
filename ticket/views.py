from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Ticket
from .forms import TicketForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def ticket_list(request):
    tickets = Ticket.objects.all()
    return render(request, 'ticket_list.html', {'tickets': tickets})
@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'ticket/ticket_detail.html', {'ticket': ticket})
@login_required
def ticket_new(request):
    if request.method == 'POST':
        customer_name= request.POST['customer_name']
        ticket_subject = request.POST['ticket_subject']
        ticket_body = request.POST['ticket_body']
        ticket_status= request.POST['ticket_status']

        ticket = Ticket(customer_name=customer_name,ticket_subject=ticket_subject,ticket_body=ticket_body,ticket_status=ticket_status)

        ticket.save()

        messages.success(request, 'Ticket created successfully')
        return render(request, 'ticket/ticket_new.html')
        

    else:
    
        return render(request, 'ticket/ticket_new.html')
@login_required
def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)

    if request.method == 'POST':
        customer_name = request.POST['customer_name']
        ticket_subject = request.POST['ticket_subject']
        ticket_body = request.POST['ticket_body']
        ticket_status = request.POST['ticket_status']

        ticket.customer_name = customer_name
        ticket.ticket_subject = ticket_subject
        ticket.ticket_body = ticket_body
        ticket.ticket_status = ticket_status

        ticket.save()

        return redirect('ticket_list')

    return render(request, 'ticket_edit.html', {'ticket': ticket})


@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, id=pk)
    ticket.delete()
    return redirect('ticket_list')