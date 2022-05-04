from dataclasses import field
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apis.models import User, Aadhar, Address, Qualification, Bank, PersonalDetail, PastJobExperience, Email, Contact


# Register your models here.
admin.site.register([User, Aadhar, Address, Qualification, Bank, PersonalDetail, PastJobExperience, Email, Contact])
