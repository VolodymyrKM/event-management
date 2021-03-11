from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    info = models.JSONField()
    timestamp = models.DateTimeField(verbose_name='Дата та час проведення')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата та час створення')
    event_type = models.ForeignKey('EventType', on_delete=models.CASCADE,
                                   related_name='event_type', verbose_name='Тип події')

    def __str__(self):
        return f'{self.event_type}'


class EventType(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='Тип події')

    def __str__(self):
        return self.name
