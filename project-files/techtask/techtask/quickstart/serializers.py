from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from techtask.quickstart.models import Person, PersonsList
from rest_framework.serializers import HyperlinkedModelSerializer

class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PersonSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'phone_number']

    def create(self, validated_data):
        return Person(**validated_data)

#class PersonsListSerializer(HyperlinkedModelSerializer):
#    class Meta:
#        model = PersonsList
