from django.db import models


class ChatMessage(models.Model):
    message = models.CharField(max_length=500)
    response = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)
