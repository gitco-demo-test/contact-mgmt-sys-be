# import hyperlinked serializers
from rest_framework import serializers

# import Contact model
from .models import Contact

# create a ContactSerializer class
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='contacts:detail')

    # specify the model and fields
    class Meta:
        model = Contact
        fields = ('url', 'id', 'name', 'address', 'email', 'mobile')