from django.contrib import admin

from .models import Person, PersonsList

admin.site.register(Person)
admin.site.register(PersonsList)
# Register your models here.
