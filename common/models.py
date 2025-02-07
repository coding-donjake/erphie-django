from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils import timezone
import uuid

# Create your models here.
class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    a2 = models.CharField(max_length=2, blank=True, null=True)
    a3 = models.CharField(max_length=3, blank=True, null=True)
    num = models.PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(999)])
    status = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    
    def soft_delete(self):
        self.removed_at = timezone.now()
        self.save()
    
class Province(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="provinces")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField()
    province = models.ForeignKey(Province, on_delete=models.CASCADE, related_name="cities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    
class Module(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    
class Privilege(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField()
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name="privileges")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
