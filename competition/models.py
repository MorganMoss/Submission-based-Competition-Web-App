from django.db import models
#from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator#, RegexValidator
# from phonenumber_field.modelfields import PhoneNumberField

MIN_GRADE:int = 7
MAX_GRADE:int = 12
ROUNDS:int = 3


# Create your models here.
class UserType(models.Model):
    type = models.CharField(primary_key=True, max_length=255)


# class User(AbstractUser):
#     phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
#     phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # Validators should be a list
#     user_type = models.ForeignKey(UserType, on_delete=models.CASCADE)


class Student(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(MIN_GRADE),
            MinValueValidator(MAX_GRADE)
        ])


class Judge(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    round = models.PositiveBigIntegerField(
       validators=[
            MaxValueValidator(1),
            MinValueValidator(ROUNDS)
        ])
    
    committed = models.BooleanField(default=False)

