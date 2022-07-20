from django.db import models

class Person(Models.model):
    id = models.BigAutoField(primary_key = True)
    owner = models.ForeignKey('auth.User', related_name='snippets', on_delete=models.CASCADE)
    highlighted = models.TextField()
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    phone_number = models.CharField(max_length = 20)
    persons_list = models.ForeignKey('PersonsList', on_delete = models.CASCADE)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class Meta:
        ordering = ['created']

class PersonsList(Models.model):
    #id = models.BigAutoField(primary_key = True) #нужен ли идентификатор?
    pass
