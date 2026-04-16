from django.db import models
class Booking(models.Model):
    STATUS = (
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    )

    customer = models.ForeignKey('users.User', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS)


