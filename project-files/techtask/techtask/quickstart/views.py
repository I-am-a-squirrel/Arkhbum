from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404, render

from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import BrowsableAPIRenderer, TemplateHTMLRenderer, JSONRenderer
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
    lookup_field = 'phone_number'
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def retrieve(self, request, *args, **kwargs):
        print("Запустили ShowHTMLPersonSet.retrieve()")
        person = Person.objects.get(phone_number = kwargs["phone_number"])
        print("person: {}".format(person))
        serializer = PersonSerializer(person)
        print("serializer.data: {}".format(serializer.data))
        return Response({'Person': serializer.data}, template_name = 'persons-profile.html')

class ListJSONPersonsView(APIView):
    #queryset = Person.objects.all()
    serializer_class = PersonSerializer
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, *args, **kwargs):
        queryset = Person.objects.all()
        persons_list = list()
        for person in queryset:
            serializer = PersonSerializer(person)
            persons_list.append(serializer.data)
        return Response(persons_list)
