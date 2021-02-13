from django.db import models
from main.models import BaseModel

class CategoryBunch(BaseModel, models.Model):
    BUNCH_TYPE = (
        ('GREEN', 'GREEN'),
        ('MATURE', 'MATURE'),
        ('OVERMATURE', 'OVERMATURE'),
        ('MATURE', 'MATURE'),
        ('COBS', 'COBS'),
        ('IMPURITIES', 'IMPURITIES')
    )

    name = models.CharField(choices=BUNCH_TYPE, max_length=128)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Bunch(BaseModel, models.Model):
    category = models.OneToOneField(to=CategoryBunch, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Bunch'
        verbose_name_plural = 'Bunches'

    def __str__(self):
        return self.pk