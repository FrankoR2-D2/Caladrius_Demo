from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.core.exceptions import ValidationError
 
from .models import User
 
 
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
    first_name = forms.CharField(
                                    max_length=30,
                                    
                                    required=True,
                                    help_text='Required: First Name',
                                    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(max_length=12,
                                    
                                    required=True, help_text='Required: Last Name',
                                    widget=(forms.TextInput(
                                        attrs={'class': 'form-control', 'placeholder': 'Last Name'})
                                            )
                                    )
    phone = forms.CharField(max_length=12)
    
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'password1', 'password2')
    
    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2
    
    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user





#--------------------------------------------------------------------------------------------------



# from dataclasses import field
# from logging import PlaceHolder
# from django import forms
# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
# # from django.contrib.auth.models import CustomUserManager
# from django.contrib.auth import password_validation

# from django.contrib.auth import get_user_model
# User = get_user_model()


# class CustomUserForm(UserCreationForm):
    # first_name = forms.CharField(
    #                             max_length=30,
                                
    #                             required=True,
    #                             help_text='Required: First Name',
    #                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    
    # last_name = forms.CharField(max_length=12,
                                
    #                             required=True, help_text='Required: Last Name',
    #                             widget=(forms.TextInput(
    #                                 attrs={'class': 'form-control', 'placeholder': 'Last Name'})
    #                                     )
    #                             )
    # phone = forms.CharField(max_length=12)
    
#     class Meta: 
#         model = User
#         fields = ['email', 'first_name', 'last_name', 'phone', 'password1', 'password2']

#---------------------------------------------------------------------------------------------------------
# class UserLoginForm(forms.Form):
#     email = forms.EmailField()
#     password= forms.CharField(widget=forms.PasswordInput)

#     def clean(self, *args, **kwargs):


#         email = self.cleaned_data.get('email')
#         password = self.cleaned_data.get('password')


#         if email and password:
#             user = authenticate(email=email, password=password)
#             if not user:
#                 raise forms.ValidationError('This user does not exist')
#             if not user.check_password(password):
#                 raise forms.ValidationError('Mot de passe incorrecte')
#             if not user.is_active:
#                 raise forms.ValidationError('plus valide')
#         return super(UserLoginForm, forms).clean(*args, **kwargs)



# class RegisterForm(User):
#     first_name = forms.CharField(
#                                 max_length=30,
                                
#                                 required=True,
#                                 help_text='Required: First Name',
#                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    
#     last_name = forms.CharField(max_length=12,
                                
#                                 required=True, help_text='Required: Last Name',
#                                 widget=(forms.TextInput(
#                                     attrs={'class': 'form-control', 'placeholder': 'Last Name'})
#                                         )
#                                 )
#     email = forms.EmailField(
#                             max_length=200,
#                             help_text='Required. Inform a valid email address.',
#                             widget=(forms.TextInput(
#                             attrs={'class': 'form-control', 'placeholder': 'Enter your email.'})
#                                     )
#                              )
#     phone = forms.CharField(
#                             label=('Phone number'),
#                             max_length=15,
#                             )                            
#     password1 = forms.CharField(
#                                 label=('Password'),
#                                 widget=(forms.PasswordInput(
#                                     attrs={'class': 'form-control', 'placeholder': 'Enter your password.'})),
#                                 help_text=password_validation.password_validators_help_text_html()
#                                 )
#     password2 = forms.CharField(
#                                 label=('Password Confirmation'),
#                                 widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password again.'}),
#                                 help_text=('Just Enter the same password, for confirmation'))

