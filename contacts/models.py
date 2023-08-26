from django.db import models

# create a Contact model class with name, address, email and mobile fields
class Contact(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    mobile = models.CharField(max_length=20)

    # add __str__ method to return name
    def __str__(self):
        return self.name