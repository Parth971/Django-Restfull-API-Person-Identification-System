from rest_framework import serializers
from apis.models import Aadhar, Address, Bank, Contact, Email, PastJobExperience, PersonalDetail, Qualification, User


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ('username', 'role',)

class AadharSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aadhar
        fields = ('aadhar_no', 'is_active',)

class AddressSerializers(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'aadhar_no', 'street', 'city', 'state', 'postal_code',)

class QualificationSerializers(serializers.ModelSerializer):
    class Meta:
        model = Qualification
        fields = ('aadhar_no', 'institute_name', 'passing_year', 'percentage',)

class BankSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bank
        fields = ('aadhar_no', 'account_number', 'bank_name', 'ifsc_code',)

class PersonalDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetail
        fields = ('aadhar_no', 'full_name', 'dob', 'blood_group',)

class ContactSerializers(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'aadhar_no', 'contact',)

class EmailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = ('id', 'aadhar_no', 'email',)

class PastJobExperienceSerializers(serializers.ModelSerializer):
    class Meta:
        model = PastJobExperience
        fields = ('aadhar_no', 'company_name', 'job_role', 'year_of_work_experience',)



