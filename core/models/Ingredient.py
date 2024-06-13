from django.db import models

from django.utils.translation import gettext_lazy as _

import uuid

class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    stack = models.IntegerField(default=0,null=False)
    price = models.DecimalField(default=0.0, null=False, max_digits=8, decimal_places=2)
    
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status = models.BooleanField(default=True, null=False)
    modified = models.DateTimeField(null=False, auto_now=True)

    def __str__ (self):
        return "%s %s %s" % (self.name, self.stack, self.price)