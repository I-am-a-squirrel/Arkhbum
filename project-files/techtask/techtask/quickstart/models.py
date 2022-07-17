from django.db import models

class Person(Models.model):
    id = models.BigAutoField(primary_key = True)
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)
    persons_list = models.ForeignKey('PersonsList', on_delete = models.CASCADE)

class PersonsList(Models.model):
    #id = models.BigAutoField(primary_key = True) #нужен ли идентификатор?
    pass
