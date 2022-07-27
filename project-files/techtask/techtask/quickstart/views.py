from django.contrib.auth.models import User, Group
from django.shortcuts import render

from rest_framework import viewsets, permissions
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from techtask.quickstart.models import Person
from techtask.quickstart.serializers import UserSerializer, GroupSerializer, PersonSerializer, ListPersonsSerializer
from techtask.permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class ListHTMLPersonsView(APIView):
    queryset = Person.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        self.object = self.queryset
        return Response({'Persons': self.object}, template_name='all-persons-list.html')

class ShowHTMLPersonSet(viewsets.GenericViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    
