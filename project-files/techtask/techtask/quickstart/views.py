from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404, render

from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet, ModelViewSet

from techtask.quickstart.models import Person
from techtask.quickstart.serializers import UserSerializer, GroupSerializer, PersonSerializer
from techtask.permissions import IsOwnerOrReadOnly

class UserViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]

class ListHTMLPersonsView(APIView):
    queryset = Person.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        self.object = self.queryset
        return Response({'Persons': self.object}, template_name = 'all-persons-list.html')

class ShowHTMLPersonSet(GenericViewSet, RetrieveModelMixin):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_field = 'phone_number'
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    #def get(self, request, *args, **kwargs):
    #    self.object = self.retrieve(request, *args, **kwargs)
    #    return Response({'Person': self.object}, template_name = 'persons-profile.html')

    def retrieve(self, request, pk = None):
        person = get_object_or_404(queryset, pk = pk)
        serializer = PersonSerializer(person)
        return Response({'Person': serializer.data}, template_name = 'persons-profile.html')
