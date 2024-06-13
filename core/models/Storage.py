from django.db import models


class Storage(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status = models.BooleanField(default=True, null=False)
    modified = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.address)
