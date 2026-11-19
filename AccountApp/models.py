from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator,RegexValidator
from django.utils import timezone
from django.core.exceptions import ValidationError 

class User(AbstractUser):
    pass
class Doctor(User):
    license_number = models.CharField(max_length=6, unique=True, validators=[MinLengthValidator(6), MaxLengthValidator(6)])
    phone=models.CharField(max_length=8)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #related_name permet de définir le nom utilisé pour accéder à la relation depuis l'autre modèle.
    specialities=models.ManyToManyField("AccountApp.Speciality", related_name="doctors")

number_validator=RegexValidator(regex=r'^\d{8}$', message='this number must be exactly 8 digits.')

def validate_birth_date(v):
    if v>=timezone.now().localdate():
        raise ValidationError("la date de naissance n'est pas valide ")

class Patient(User):
    national_id=models.CharField(max_length=8, unique=True, validators=[number_validator])
    phone=models.CharField(max_length=8)
    birth_date=models.DateField(validators=[validate_birth_date])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

class Speciality(models.Model):
    name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #doctors=models.ManyToManyField("AccountApp.Doctor")
    

