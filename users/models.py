from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Admin(User):
    pass

class SiteUser(User):
    pass