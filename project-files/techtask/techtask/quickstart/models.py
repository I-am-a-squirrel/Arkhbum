from django.db import models

class Person(Models.model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)
