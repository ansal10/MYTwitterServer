from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    emailId = models.EmailField(unique=True)
    # username = models.CharField(max_length=100, unique=True, db_index=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    contactNumber = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def to_json(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'username': self.username
        }
