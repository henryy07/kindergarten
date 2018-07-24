from django.conf import settings
from django.db import models
from django.urls import reverse_lazy
from django.dispatch import receiver
from django.db.models.signals import post_save

User = settings.AUTH_USER_MODEL

GROUP = (('Y', 'Younger'),
         ('O','Older'))


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    type_of_group = models.CharField(max_length=1, choices=GROUP)
#	child = models.ForeignKey(Child) FK should be in child model so child will be assigned to the group
    #teachers = models.ManyToManyField(Teacher, related_name='teacher_of_group') // trzeba zaimportować z accounts

    def __str__(self):
        return self.group_name


class Child(models.Model):
    name = models.CharField(max_length=255)
    picture = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True, null=True)
    group = models.ForeignKey(Group, null=True, blank=True)
    # parent = models.ManyToMany(Parent, related_name='parent_of_child') // FK u parenta?

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("child-group:child-detail", kwargs={"pk": self.pk})





