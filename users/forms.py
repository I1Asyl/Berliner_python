from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser


def makeCustomForm(fields):
        for field_name in fields:
            field = fields.get(field_name)
            placeHolder = "Enter " + field.label.lower()
            field.widget.attrs.update({'placeholder': placeHolder, 'class': "form-control"})   

class customAuthenticationForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        makeCustomForm(self.fields)
        self.hidePassword()

    def showPassword(self):
        attrs = {'type' : 'text'} 
        self.fields['password'].widget.attrs.update(attrs)        

    def hidePassword(self):
        attrs = {'type' : 'password'} 
        self.fields['password'].widget.attrs.update(attrs)   

    error_messages = {
        "invalid_login": "The username or password is incorrect",
        "inactive": "Permission denied",
    }


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        makeCustomForm(self.fields)

    

        
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')
        print(UserCreationForm.Meta.fields)

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email')