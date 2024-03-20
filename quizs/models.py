from django.db import models

class Quiz(models.Model):
    question = models.TextField(max_length=200)
    answer = models.TextField(max_length=200)