from django.db import models

class Ticket(models.Model):
    customer_name = models.CharField(max_length=100)
    ticket_subject = models.CharField(max_length=200)
    ticket_body = models.TextField()
    ticket_status = models.CharField(
        max_length=10,
        choices=[('open', 'Open'), ('close', 'Close'), ('pending', 'Pending')],
        default='open'
    )

    class Meta:
        db_table = "ticket"
