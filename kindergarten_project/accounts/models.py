from django.conf import settings
from django.db import models



from groups.models import Child, Group
from django.contrib.auth.models import User
#User = settings.AUTH_USER_MODEL


class Parent(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    child = models.ManyToManyField(Child, related_name="childs_parent")

    timestamp = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    # child = models.ForeignKey(Child)



<<<<<<< HEAD
class Guardian(models.Model):
=======

class Guardian(models.Model):

>>>>>>> 4c6d812c630ebc3efe17f9e4593d7c00e36c19ce
    user = models.OneToOneField(User)
    parent = models.ManyToManyField(Parent, related_name='guardian_parent') # czy potrzebne?
    group = models.ManyToManyField(Group, related_name='group')

    def __str__(self):
        return self.user
