from django.shortcuts import render

from django.contrib.auth.models import User, Group

from rest_framework import viewsets, permissions
from rest_framework.renderers import TemplateHTMLRenderer
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
    #serializer_class = ListPersonsSerializer
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'Persons': self.object}, template_name='persons-list.html')
