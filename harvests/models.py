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

    location = models.CharField(max_length=128, null=True, blank=True)
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
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Bunch'
        verbose_name_plural = 'Bunches'

    def __str__(self):
        return f'Bunch-{self.pk}'


class Vehicle(BaseModel, models.Model):
    """

    """

    enrollment = models.CharField(max_length=5)
    modelVehicle = models.IntegerField(default=0)
    brand = models.CharField(max_length=20)
    driver = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Vehicle'
        verbose_name_plural = 'Vehicles'

    def __str__(self):
        return self.enrollment

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})
