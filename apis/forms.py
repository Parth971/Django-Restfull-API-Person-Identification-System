from django.contrib.auth.forms import UserCreationForm
from django import forms
from apis.models import User
from django.contrib.auth.models import Group


class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]    
    
    def save(self, commit=True):
        user = super(RegisterForm, self).save(commit=False)
        if commit:
            user.save()
            my_group = Group.objects.get(name='Staff')
            my_group.user_set.add(User.objects.get(email=user.email, password=user.password))
            my_group.save()
        return user
