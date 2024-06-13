from django.db import models

from .Storage import Storage
from .Product import Product


class ProductStorage(models.Model):
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id_storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    stock = models.IntegerField()

    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status = models.BooleanField(default=True, null=False)
    modified = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.id_product.name, self.id_storage.name)
