from django.db import models
from datetime import date


class Note(models.Model):
    note = models.CharField(max_length=100, default='')
    note_title = models.CharField(max_length=100, default='')
    note_body = models.TextField(default='')
    date = models.DateField(auto_now_add=True)
