from django.db import models


class AbstractTimeStamped(models.Model):

    """ Time Stamped Definition """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True
