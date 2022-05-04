from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLES = (
        ('Manager', 'Manager'),
        ('Staff', 'Staff'),
    )
    user_id = models.IntegerField(primary_key=True, auto_created=True)
    role = models.CharField(max_length=50, choices = ROLES, null=True, default='Staff')                 

class Aadhar(models.Model):
    aadhar_no = models.BigIntegerField(primary_key=True)
    is_active = models.BooleanField()

    def __str__(self):
        return '(Adhar: ' + str(self.aadhar_no) + ', Active: ' + str(self.is_active) + ')'

class Address(models.Model):
    aadhar_no = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    street = models.CharField(max_length=20, null=False, blank=False)
    city = models.CharField(max_length=20, null=False, blank=False)
    state = models.CharField(max_length=20, null=False, blank=False)
    postal_code = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return '(' + str(self.id) + ' | ' + str(self.aadhar_no) + ')'

class Qualification(models.Model):
    aadhar_no = models.OneToOneField(Aadhar, blank=False, primary_key=True, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=50, null=False, blank=False)
    passing_year = models.IntegerField(null=False, blank=False)
    percentage = models.IntegerField(null=False, blank=False)

class Bank(models.Model):
    aadhar_no = models.OneToOneField(Aadhar, blank=False, primary_key=True, on_delete=models.CASCADE)
    account_number = models.BigIntegerField(null=False, blank=False)
    bank_name = models.CharField(max_length=50, null=False, blank=False)
    ifsc_code = models.BigIntegerField(null=False, blank=False)

class PersonalDetail(models.Model):
    aadhar_no = models.OneToOneField(Aadhar, blank=False, primary_key=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    blood_group = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return '( Fullname: ' + str(self.full_name) + ' | ' + str(self.aadhar_no) + ')'

class Contact(models.Model):
    aadhar_no = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    contact = models.BigIntegerField(null=False, blank=False)

class Email(models.Model):
    aadhar_no = models.ForeignKey(Aadhar, on_delete=models.CASCADE)
    email = models.EmailField(null=False, blank=False)

class PastJobExperience(models.Model):
    aadhar_no = models.OneToOneField(Aadhar, blank=False, primary_key=True, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=50, null=False, blank=False)
    job_role = models.CharField(max_length=50, null=False, blank=False)
    year_of_work_experience = models.IntegerField(null=False, blank=False)


