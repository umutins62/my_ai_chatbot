from django.db import models


class Conversation(models.Model):
    id = models.AutoField(primary_key=True)
    start_date = models.DateTimeField(auto_now_add=True, blank=True, null=True)

class ChatMessage(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    message = models.TextField(blank=True, null=True  , default="")
    response = models.TextField(blank=True, null=True  , default="")
    sender = models.CharField(max_length=100, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)



class genaiSetting(models.Model):
    temperture = models.FloatField(default=0.99)
    max_length = models.IntegerField(default=1000)
    top_p = models.FloatField(default=0.9)
    top_k = models.IntegerField(default=0)




