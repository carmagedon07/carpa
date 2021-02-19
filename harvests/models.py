from django.contrib.gis.db import models as gis_models
from django.db import models
from main.models import BaseModel


class CategoryBunch(BaseModel, models.Model):
    """

    """

    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'BunchCategory'
        verbose_name_plural = 'BunchCategories'

    def __str__(self):
        return self.name


class BatchSource(BaseModel, models.Model):
    """

    """

    location = gis_models.PolygonField(
        help_text='Select at least 3 points to delimit a region. When finished, press click twice.',
        null=True,
        blank=True
    )
    city = models.CharField(max_length=64, null=True, blank=True)

    class Meta:
        verbose_name = 'BatchSource'
        verbose_name_plural = 'BatchSources'

    def __str__(self):
        return self.location


class Bunch(BaseModel, models.Model):
    """

    """

    category = models.ForeignKey(CategoryBunch, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Bunch'
        verbose_name_plural = 'Bunches'

    def __str__(self):
        return f'Bunch-{self.pk}'
