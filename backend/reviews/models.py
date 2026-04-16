from django.db import models
class Review(models.Model):
    booking = models.OneToOneField('bookings.Booking', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Service', on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
