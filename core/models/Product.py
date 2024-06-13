from django.db import models


class Product(models.Model):
    # id = models.IntegerField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=20)
    TYPES = [
        (0, "Sin tipo"),
        (1, "Panes"),
        (2, "Tortas"),  # comas en las tuplas
    ]
    type_id = models.IntegerField(null=False, choices=TYPES, default=0)
    price = models.DecimalField(default=0.0, null=False, max_digits=8, decimal_places=2)
    created = models.DateTimeField(editable=False, null=False, auto_now_add=True)
    status = models.BooleanField(default=True, null=False)
    modified = models.DateTimeField(null=False, auto_now=True)

    def __str__(self):
        return "%s %s" % (self.name, self.price)
