import uuid
from django.db import models
from django.contrib.auth.models import User


class Base(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    create_at = models.DateTimeField(auto_now_add=True, verbose_name='Create_at')
    update_at = models.DateTimeField(auto_now=True, verbose_name='Update_at')


    class Meta:

        abstract = True

class Brand(Base):

    name = models.CharField(max_length=100, verbose_name='Name')
    description = models.TextField(null=True, blank=True, verbose_name='Description')


    class Meta:

        ordering = ['name']

    def __str__(self):
        return self.name


class Car(Base):

    model = models.CharField(max_length=100, verbose_name='Model')
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, null=True, verbose_name='Brand') 
    factory_year = models.IntegerField(null=True, verbose_name='Factory year')
    model_year = models.IntegerField(null=True, verbose_name='Model year')
    color = models.CharField(max_length=50, null=True, blank=True, verbose_name='Color')
    owner = models.ForeignKey(User, on_delete=models.PROTECT, null=True, verbose_name='Owner')
    description = models.TextField(null=True, blank=True, verbose_name='Description')


    class Meta:

        ordering = ['model']

    def __str__(self):
        return self.model