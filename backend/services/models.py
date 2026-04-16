from django.db import models
import uuid
class Service(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    provider = models.ForeignKey('users.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()

    def __str__(self):
     return self.title
