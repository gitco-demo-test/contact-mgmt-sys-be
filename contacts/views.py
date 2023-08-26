from django.shortcuts import render

# import list create api view
from rest_framework import generics
# import search filter
from rest_framework import filters

# import Contact model
from .models import Contact
# import ContactSerializer
from .serializers import ContactSerializer

# create a list and create api view for contacts
class ContactList(generics.ListCreateAPIView):
    # specify serializer class
    serializer_class = ContactSerializer
    # specify queryset
    queryset = Contact.objects.all()
    # use search filter backend
    filter_backends = [filters.SearchFilter]
    # specify the fields to search
    search_fields = ['name', 'address', 'email', 'mobile']

# create a retrieve, update and destroy api view for contacts
class ContactDetail(generics.RetrieveUpdateDestroyAPIView):
    # specify serializer class
    serializer_class = ContactSerializer
    # specify queryset
    queryset = Contact.objects.all()