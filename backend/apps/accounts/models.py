from django.db import models

# Create your models here.

class User(models.Model):
    class Meta(object):
        db_table = 'user'

    name = models.CharField(
        'Name', blank = False, null = False, max_length = 150 
    )

    email = models.CharField(
        'Email', blank = False, null = False, max_length = 150
    )

    password = models.CharField(
        'Password', blank = False, null = False, max_length = 150
    )

    token = models.CharField(
        'Token', blank = True, null = True, max_length = 500, db_index = True
    )

    token_expires = models.DateTimeField(
        'Token Expiration Date', blank = True, null = True
    )

    created_at = models.DateTimeField(
        'Creation Date', blank = True, auto_now_add = True
    )

    updated_at = models.DateTimeField(
        'Update Date', blank = True, auto_now = True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    def getExp(self): 
        return self.token_expires