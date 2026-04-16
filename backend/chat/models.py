from django.db import models
class Conversation(models.Model):
    customer = models.ForeignKey('users.User', related_name='customer', on_delete=models.CASCADE)
    provider = models.ForeignKey('users.User', related_name='provider', on_delete=models.CASCADE)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    sender = models.ForeignKey('users.User', on_delete=models.CASCADE)
    content = models.TextField()
    is_seen = models.BooleanField(default=False)

