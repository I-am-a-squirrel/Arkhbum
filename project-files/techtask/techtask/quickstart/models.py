from django.db import models

class PhonePersonManager(models.Manager):
    def all(self, number):
        queryset = super().get_queryset().filter(phone_number = number)
        person_name = queryset[0]
        print("person_name: {}".format(person_name))
        return {'Person': person_name, 'phone_number': number}

class Person(models.Model):
    id = models.BigAutoField(primary_key = True)
    first_name = models.CharField(max_length = 50, null = True)
    last_name = models.CharField(max_length = 50, null = True)
    phone_number = models.CharField(max_length = 20, null = True)
    persons_list = models.ForeignKey('PersonsList', on_delete = models.CASCADE)
    objects = models.Manager()
    phone_objects = PhonePersonManager()
    

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

class PersonsList(models.Model):
    id = models.BigAutoField(primary_key = True)
    list_name = models.CharField(max_length = 50, null = True)

    def __str__(self):
        return '%s' % (self.list_name)
