
from django.test import TestCase
from django.urls import reverse
import ticket
from ticket.models import Ticket
from django.contrib.auth.models import User
from django.test import Client


# Create your tests here.
   
class TicketTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser8', password='123789')
        self.client.login(username='testuser8', password='123789')
        self.ticket_data = {
            'customer_name': 'John Doe',
            'ticket_subject': 'Test Ticket',
            'ticket_body': 'This is a test ticket.',
            'ticket_status': 'Open',
        }

    def test_ticket_list_view(self):
        
        self.ticket = Ticket.objects.create(customer_name='john',ticket_subject='Test',ticket_body='body',ticket_status='open')
        print(self.ticket)
        response = self.client.get('/ticket/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket_list.html')
       
    def test_ticket_detail_view(self):
        ticket = Ticket.objects.create(**self.ticket_data)
        response = self.client.get(f'/ticket/{ticket.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ticket/ticket_detail.html')
