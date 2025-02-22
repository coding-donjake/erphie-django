from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_name = models.CharField(max_length=255, db_index=True)
    first_name = models.CharField(max_length=255, db_index=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    suffix = models.CharField(max_length=255, blank=True, null=True, db_index=True)
    gender = models.PositiveSmallIntegerField(db_index=True)
    birth_date = models.DateField(db_index=True)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    
class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    status = models.PositiveSmallIntegerField(db_index=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="account")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    deactivated_at = models.DateTimeField(blank=True, null=True, db_index=True)
    suspended_at = models.DateTimeField(blank=True, null=True, db_index=True)

class Email(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=255, db_index=True)
    domain_name = models.CharField(max_length=255, db_index=True)
    status = models.PositiveSmallIntegerField(db_index=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="emails")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
    
class Simcard(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    idc = models.CharField(max_length=5, db_index=True)
    number = models.CharField(max_length=20, db_index=True)
    status = models.PositiveSmallIntegerField(db_index=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name="simcards")
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    removed_at = models.DateTimeField(blank=True, null=True)
