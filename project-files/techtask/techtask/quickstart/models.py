from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import uuid

class Person(Models.model):
    #id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = false)
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)

class PersonsList(Models.model):
    persons_list = models.JSONField() #заменить на отношения
