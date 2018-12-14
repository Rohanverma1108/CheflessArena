from django import forms
from .models import *

class SuggestionForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Enter Your Name'}
    ),required=True,max_length=100)
    suggestions = forms.CharField(widget=forms.Textarea(
    attrs={'class':'form-control','placeholder':'Enter your comment here....'}
    ),required=True,max_length=None)
    class Meta:
        model = Suggestions
        fields = '__all__'

class SignUpForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Enter UserName'}
    ),required=True,max_length=30)

    email = forms.CharField(widget=forms.EmailInput(
    attrs={'class':'form-control','placeholder':'Enter E-mail'}
    ),required=True,max_length=30)

    first_name = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Enter First Name'}
    ),required=True,max_length=30)

    last_name = forms.CharField(widget=forms.TextInput(
    attrs={'class':'form-control','placeholder':'Enter Last Name'}
    ),required=True,max_length=30)

    password = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Enter Password'}
    ),required=True,max_length=30)

    confirm_password = forms.CharField(widget=forms.PasswordInput(
    attrs={'class':'form-control','placeholder':'Re-Enter Password'}
    ),required=True,max_length=30)

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password','confirm_password']


    def clean_confirm_password(self):
        p = self.cleaned_data['password']
        cp = self.cleaned_data['confirm_password']
        if(p!=cp):
            raise forms.ValidationError("Confirm Password and Password must be same")
        else:
            if(len(p)<8):
                raise forms.ValidationError("Password must be atleast 8 characters.")
            elif(p.isdigit()):
                raise forms.ValidationError("Password must contain atleast a character.")


class ChangePasswordForm(forms.ModelForm):

    old_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class':'form-control'}),
    label="Old Password",
    required=True
    )

    new_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class':'form-control'}),
    label="New Password",
    required=True
    )

    confirm_password = forms.CharField(
    widget=forms.PasswordInput(attrs={'class':'form-control'}),
    label="Confirm Password",
    required=True
    )

    class Meta:
        model = User
        fields= ['old_password','new_password','confirm_password']
