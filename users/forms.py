from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}
    ))

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control'}
    ))

class UserUpdateFormAboutGeneral(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['about_general']

class UserUpdateFormAboutLooking(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['about_looking']

class UserUpdateFormAboutExpectation(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['about_expectation']

class UserUpdateFormRightInfo(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = get_user_model()
        fields = [
            'email',
            'phone_number',
            ]