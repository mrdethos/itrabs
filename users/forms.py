from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Insira seu e-mail'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insira seu nome'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Insira seu sobrenome'}))


    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user