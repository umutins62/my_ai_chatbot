from django.db import models


class ChatMessage(models.Model):
    message = models.CharField(max_length=500)
    response = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)



class genaiSetting(models.Model):
    temperture = models.FloatField(default=0.99)
    max_length = models.IntegerField(default=1000)
    top_p = models.FloatField(default=0.9)
    top_k = models.IntegerField(default=0)
    num_return_sequences = models.IntegerField(default=1)
    repetition_penalty = models.FloatField(default=1.0)
    length_penalty = models.FloatField(default=1.0)
    do_sample = models.BooleanField(default=True)
    early_stopping = models.BooleanField(default=True)
    num_beams = models.IntegerField(default=1)



