from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class Board(models.Model):
    name = models.CharField(max_length=1000)
    users = models.ManyToManyField(get_user_model(), related_name='message_boards')


class Message(models.Model):
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='messages')
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='messages')
    x = models.IntegerField()
    y = models.IntegerField()
    def __str__(self):
        return f'{self.user} - {self.text}'
