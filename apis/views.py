
from django.contrib.auth.models import Group
from functools import partial
from django.http import JsonResponse
from apis.models import Aadhar, Address, Bank, Contact, Email, PastJobExperience, PersonalDetail, Qualification, User
from apis.serializer import AadharSerializers, AddressSerializers, BankSerializers, ContactSerializers, EmailSerializers, PastJobExperienceSerializers, PersonalDetailSerializers, QualificationSerializers, UserSerializers
from apis.forms import RegisterForm
from django.contrib.auth import login, authenticate, logout
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from django.core.exceptions import PermissionDenied


# For reference 
# manager_permissions = ['apis.add_aadhar', 'apis.view_aadhar', 'apis.change_aadhar', 'apis.delete_aadhar', 
# 'apis.add_address', 'apis.view_address', 'apis.change_address', 'apis.delete_address',
# 'apis.add_qualification', 'apis.view_qualification', 'apis.change_qualification', 'apis.delete_qualification',
# 'apis.add_bank', 'apis.view_bank', 'apis.change_bank', 'apis.delete_bank',
# 'apis.add_personaldetail', 'apis.view_personaldetail', 'apis.change_personaldetail', 'apis.delete_personaldetail', 
# 'apis.add_contact', 'apis.view_contact', 'apis.change_contact', 'apis.delete_contact',
# 'apis.add_email', 'apis.view_email', 'apis.change_email', 'apis.delete_email',
# 'apis.add_pastjobexperience', 'apis.view_pastjobexperience', 'apis.change_pastjobexperience', 'apis.delete_pastjobexperience']

# staff_permissions = ['apis.view_aadhar',
# 'apis.view_address',
# 'apis.view_qualification',
# 'apis.view_bank',
# 'apis.view_personaldetail',
# 'apis.view_contact',
# 'apis.view_email',
# 'apis.view_pastjobexperience']


@api_view(["POST"])
def user_roles(request, user_id):
    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.user.has_perm('apis.change_user'):
        data = {}
        role = request.data.get('role')
        if role:
            if role == 'Manager' or role == 'Staff':
                data['role'] = role
                my_group = Group.objects.get(name=role)
            else:
                return Response({'Message': 'Invalid Role! Manager and Staff are avilable roles.'})

        serializer = UserSerializers(user, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            user.groups.clear()
            my_group.user_set.add(user)
            my_group.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    else:
        raise PermissionDenied()

@api_view(["POST"])
@permission_classes([AllowAny])
def signup(request):
    try:
        data = {}
        form = RegisterForm(request.POST)
        if form.is_valid():
            account = form.save()
            account = User.objects.get(username=account.username, email=account.email)
            # token = Token.objects.create(user=account)
            data["message"] = "user registered successfully"
            data["email"] = account.email
            data["username"] = account.username
            # data["token"] = token.key
        else:
            data = form.errors
        return Response(data)
    except IntegrityError as e:
        account=User.objects.get(username='')
        account.delete()
        raise ValidationError({"400": f'{str(e)}'})
    except KeyError as e:
        raise ValidationError({"400": f'Field {str(e)} missing'})

@api_view(["POST"])
@permission_classes([AllowAny])
def signin(request):
    if request.user.is_authenticated or request.session.session_key:
        return Response({'Message': 'Currently Logged in, first signout then login.'})
    data = {}
    user = authenticate(username=request.POST.get('username', None), password=request.POST.get('password', None))
    if user is not None:
        token = Token.objects.get_or_create(user=user)[0].key
        login(request, user)
        data["message"] = "user logged in"
        data["email_address"] = user.email
        Res = {"data": data, "token": token}
        return Response(Res)
    else:
        return JsonResponse({'Error': 'User login failed!'})
       
@api_view(["GET"])
def signout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response('User Logged out successfully')

@api_view(['GET', 'POST'])
def aadhar_list(request):
    if request.method == 'GET':
        if request.user.has_perm('apis.view_aadhar'):
            queryset = Aadhar.objects.all()
            serializer = AadharSerializers(queryset, many=True)
            return JsonResponse(serializer.data, safe=False)
        else:
            raise PermissionDenied()

    elif request.method == 'POST':
        if request.user.has_perm('apis.add_aadhar'):
            data = {
                'aadhar_no': request.POST.get('aadhar_no'),
                'is_active': request.POST.get('is_active'),
            }
            aadhar_serializer = AadharSerializers(data=data)
            if aadhar_serializer.is_valid():
                aadhar_serializer.save()
                return JsonResponse(aadhar_serializer.data)
            else:
                return JsonResponse(aadhar_serializer.errors)
        else:
            raise PermissionDenied()

@api_view(['GET', 'PATCH', 'DELETE'])
def aadhar_detail(request, aadhar_no):
    try:
        aadhar = Aadhar.objects.get(aadhar_no=aadhar_no)
    except Aadhar.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.method == 'GET':
        if request.user.has_perm('apis.view_aadhar'):
            serializer = AadharSerializers(aadhar)
            return JsonResponse(serializer.data, safe=False)
        else:
            raise PermissionDenied()

    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_aadhar'):
            aadhar_serializer = AadharSerializers(aadhar, data=request.data, partial=True)
            if aadhar_serializer.is_valid():
                aadhar_serializer.save()
                return JsonResponse(aadhar_serializer.data)
            else:
                return JsonResponse(aadhar_serializer.errors)
        else:
            raise PermissionDenied()
    
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_aadhar'):
            aadhar.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()

@api_view(['GET', 'POST'])
def aadhar_address(request, aadhar_no):
    try:
        aadhar = Aadhar.objects.get(aadhar_no=aadhar_no)
    except Aadhar.DoesNotExist as e:
        return Response({'Error': str(e)})

    try:
        address_list = Address.objects.filter(aadhar_no=aadhar_no)
    except Address.DoesNotExist as e:
        return Response({'Error': str(e)})
    
    if request.method == 'GET':
        if request.user.has_perm('apis.view_address'):
            address_serializer = AddressSerializers(address_list, many=True)
            return Response(address_serializer.data)
        else:
            raise PermissionDenied()
        
    elif request.method == 'POST':
        if request.user.has_perm('apis.add_address'):
            data = request.data.copy()
            data['aadhar_no'] = aadhar_no
            address_serializer = AddressSerializers(data=data)
            if address_serializer.is_valid():
                address_serializer.save()
                return Response(address_serializer.data)
            else:
                return Response(address_serializer.errors)
        else:
            raise PermissionDenied()
        
@api_view(['GET', 'PATCH', 'DELETE'])
def aadhar_address_detail(request, aadhar_no, address_id):
    try:
        address = Address.objects.get(aadhar_no=aadhar_no, id=address_id)
    except Address.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.method == 'GET':
        if request.user.has_perm('apis.view_address'):
            address_serializer = AddressSerializers(address)
            return Response(address_serializer.data)
        else:
            raise PermissionDenied()
    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_address'):
            address_serializer = AddressSerializers(address, data=request.data, partial=True)
            if address_serializer.is_valid():
                address_serializer.save()
                return Response(address_serializer.data)
            else:
                return Response(address_serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_address'):
            address.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()
    
@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def aadhar_qualification(request, aadhar_no):
    if request.method != 'POST':
        try:
            qualification = Qualification.objects.get(aadhar_no=aadhar_no)
        except Qualification.DoesNotExist as e:
            return Response({'Error': str(e)})
    
    if request.method == 'GET':
        if request.user.has_perm('apis.view_qualification'):
            serializer = QualificationSerializers(qualification)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
    elif request.method == 'POST':
        if request.user.has_perm('apis.add_qualification'):
            data = request.data.copy()
            data['aadhar_no'] = aadhar_no
            serializer = QualificationSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_qualification'):
            serializer = QualificationSerializers(qualification, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_qualification'):
            qualification.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def aadhar_bank(request, aadhar_no):
    if request.method != 'POST':
        try:
            bank = Bank.objects.get(aadhar_no=aadhar_no)
        except Bank.DoesNotExist as e:
            return Response({'Error': str(e)})
    
    if request.method == 'GET':
        if request.user.has_perm('apis.view_bank'):
            serializer = BankSerializers(bank)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
    elif request.method == 'POST':
        if request.user.has_perm('apis.add_bank'):
            data = request.data.copy()
            data['aadhar_no'] = aadhar_no
            serializer = BankSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_bank'):
            serializer = BankSerializers(bank, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_bank'):
            bank.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def aadhar_personaldetail(request, aadhar_no):
    if request.method != 'POST':
        try:
            personal_detail = PersonalDetail.objects.get(aadhar_no=aadhar_no)
        except PersonalDetail.DoesNotExist as e:
            return Response({'Error': str(e)})
    
    if request.method == 'GET':
        if request.user.has_perm('apis.view_personaldetail'):
            serializer = PersonalDetailSerializers(personal_detail)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
    elif request.method == 'POST':
        if request.user.has_perm('apis.add_personaldetail'):
            data = request.data.copy()
            data['aadhar_no'] = aadhar_no
            serializer = PersonalDetailSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_personaldetail'):
            serializer = PersonalDetailSerializers(personal_detail, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_personaldetail'):
            personal_detail.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()

@api_view(['GET', 'POST'])
def aadhar_contact(request, aadhar_no):
    try:
        aadhar = Aadhar.objects.get(aadhar_no=aadhar_no)
    except Aadhar.DoesNotExist as e:
        return Response({'Error': str(e)})

    try:
        contact_list = Contact.objects.filter(aadhar_no=aadhar_no)
    except Contact.DoesNotExist as e:
        return Response({'Error': str(e)})
    
    if request.method == 'GET':
        if request.user.has_perm('apis.view_contact'):
            serializer = ContactSerializers(contact_list, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
        
    elif request.method == 'POST':
        if request.user.has_perm('apis.add_contact'):
            data = request.data.copy()
            data['aadhar_no'] = aadhar_no
            serializer = ContactSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
        
@api_view(['GET', 'PATCH', 'DELETE'])
def aadhar_contact_detail(request, aadhar_no, contact_id):
    try:
        contact = Contact.objects.get(aadhar_no=aadhar_no, id=contact_id)
    except Contact.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.method == 'GET':
        if request.user.has_perm('apis.view_contact'):
            serializer = ContactSerializers(contact)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_contact'):
            serializer = ContactSerializers(contact, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_contact'):
            contact.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()

@api_view(['GET', 'POST'])
def aadhar_email(request, aadhar_no):
    try:
        aadhar = Aadhar.objects.get(aadhar_no=aadhar_no)
    except Aadhar.DoesNotExist as e:
        return Response({'Error': str(e)})

    try:
        email_list = Email.objects.filter(aadhar_no=aadhar_no)
    except Email.DoesNotExist as e:
        return Response({'Error': str(e)})
    
    if request.method == 'GET':
        if request.user.has_perm('apis.view_email'):
            serializer = EmailSerializers(email_list, many=True)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
        
    elif request.method == 'POST':
        if request.user.has_perm('apis.add_email'):
            data = request.data.copy()
            data['aadhar_no'] = aadhar_no
            serializer = EmailSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
        
@api_view(['GET', 'PATCH', 'DELETE'])
def aadhar_email_detail(request, aadhar_no, email_id):
    try:
        email = Email.objects.get(aadhar_no=aadhar_no, id=email_id)
    except Email.DoesNotExist as e:
        return Response({'Error': str(e)})

    if request.method == 'GET':
        if request.user.has_perm('apis.view_email'):
            serializer = EmailSerializers(email)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_email'):
            serializer = EmailSerializers(email, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_email'):
            email.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()

@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def aadhar_past_job_experience(request, aadhar_no):
    if request.method != 'POST':
        try:
            pje = PastJobExperience.objects.get(aadhar_no=aadhar_no)
        except PastJobExperience.DoesNotExist as e:
            return Response({'Error': str(e)})
    
    if request.method == 'GET':
        if request.user.has_perm('apis.view_pastjobexperience'):
            serializer = PastJobExperienceSerializers(pje)
            return Response(serializer.data)
        else:
            raise PermissionDenied()
    elif request.method == 'POST':
        if request.user.has_perm('apis.add_pastjobexperience'):
            data = request.data.copy()
            data['aadhar_no'] = aadhar_no
            serializer = PastJobExperienceSerializers(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'PATCH':
        if request.user.has_perm('apis.change_pastjobexperience'):
            serializer = PastJobExperienceSerializers(pje, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors)
        else:
            raise PermissionDenied()
    elif request.method == 'DELETE':
        if request.user.has_perm('apis.delete_pastjobexperience'):
            pje.delete()
            return Response({'Message': 'Deleted Successfully.'})
        else:
            raise PermissionDenied()

@api_view(['GET'])
def personal_details(request):
    if request.user.has_perm('apis.view_personaldetail'):
        pds = PersonalDetail.objects.order_by('aadhar_no')

        if request.GET.get('is_active') == 'True':
            pds = pds.filter(aadhar_no__is_active=True)
        elif request.GET.get('is_active') == 'False':
            pds = pds.filter(aadhar_no__is_active=False)

        if request.GET.get('sort') == 'descending':
            pds = pds.order_by('-aadhar_no')

        if request.GET.get('aadhar_no') != None:
            pds = pds.filter(aadhar_no=request.GET.get('aadhar_no'))

        serializer = PersonalDetailSerializers(pds, many=True)

        return Response(serializer.data)
    else:
        raise PermissionDenied()