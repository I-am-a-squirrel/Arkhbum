from django.db import models
import uuid

class Person(Models.model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = false)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)

class ListPersons(Models.model):
    
