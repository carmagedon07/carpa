
from django.db import models
# from django.db.models.signals import post_save
from main.models import BaseModel


class CategoryBunch(BaseModel):
    """

    """

    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Bunch Category'
        verbose_name_plural = 'Bunch Categories'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'Category-{self.pk}'


class Bunch(BaseModel):
    """

    """

    category = models.ForeignKey(CategoryBunch, on_delete=models.CASCADE, null=True, blank=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Bunch'
        verbose_name_plural = 'Bunches'

    def __str__(self):
        return f'Bunch-{self.pk}'


class Harvester(BaseModel):
    """

    """

    name = models.CharField(max_length=128, blank=True)
    address = models.CharField(max_length=64, blank=True)
    email = models.EmailField(max_length=64, blank=True)
    phone = models.CharField(max_length=16, blank=True)
    web = models.CharField(max_length=128, blank=True)

    class Meta:
        verbose_name = 'Harvester'
        verbose_name_plural = 'Harvesters'

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'Harvester-{self.pk}'
