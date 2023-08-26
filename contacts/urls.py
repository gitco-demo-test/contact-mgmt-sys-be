# import django path
from django.urls import path

# import ContactList and ContactDetail
from .views import ContactList, ContactDetail

app_name = 'contacts'

urlpatterns = [
    path(f'{app_name}/', ContactList.as_view(), name='list'),
    path(f'{app_name}/<int:pk>/', ContactDetail.as_view(), name='detail'),
]