
from django.urls import path

from .views import user_roles, aadhar_list, aadhar_detail, signup, signin, signout, aadhar_address, aadhar_address_detail, aadhar_qualification, aadhar_bank, aadhar_personaldetail, aadhar_contact, aadhar_contact_detail, aadhar_email, aadhar_email_detail, aadhar_past_job_experience, personal_details

urlpatterns = [
    path('users/<int:user_id>/', user_roles),
    path('signup/', signup),
    path('signin/', signin),
    path('signout/', signout),
    path('aadhar/', aadhar_list),
    path('aadhar/<int:aadhar_no>/', aadhar_detail),
    path('aadhar/<int:aadhar_no>/address/', aadhar_address),
    path('aadhar/<int:aadhar_no>/address/<int:address_id>/', aadhar_address_detail),
    path('aadhar/<int:aadhar_no>/qualification/', aadhar_qualification),
    path('aadhar/<int:aadhar_no>/bank/', aadhar_bank),
    path('aadhar/<int:aadhar_no>/personal_detail/', aadhar_personaldetail),
    path('aadhar/<int:aadhar_no>/personal_detail/contact/', aadhar_contact),
    path('aadhar/<int:aadhar_no>/personal_detail/contact/<int:contact_id>/', aadhar_contact_detail),
    path('aadhar/<int:aadhar_no>/personal_detail/email/', aadhar_email),
    path('aadhar/<int:aadhar_no>/personal_detail/email/<int:email_id>/', aadhar_email_detail),
    path('aadhar/<int:aadhar_no>/past_job_experience/', aadhar_past_job_experience),
    path('personal_details/', personal_details)
]
