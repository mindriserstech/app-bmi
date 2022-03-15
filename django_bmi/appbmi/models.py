import email
from statistics import mode
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class BmiUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    user_email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        db_table = "bmi_users"

class UserDiet(models.Model):
    bmi_index_range = models.CharField(max_length=10)
    diet_description = models.CharField(max_length=200)

    class Meta:
        db_table = "bmi_diet"

class UserBmi(models.Model):
    weight = models.CharField(max_length=20)
    height = models.CharField(max_length=20)
    bmi_unit = models.CharField(max_length=10)
    bmi = models.CharField(max_length=20)
    added_at = models.DateTimeField(null=False)
    user_id = models.BigIntegerField()

    class Meta:
        db_table = "bmi_userbmi"

class UserBmiLog(models.Model):
    bmi_id = models.BigIntegerField()
    log_date = models.DateTimeField(null=False)

    class Meta:
        db_table = "bmi_log"