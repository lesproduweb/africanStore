from django import forms
from django.contrib.auth import get_user_model, authenticate, login

User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        super(LoginForm, self).clean()
        if self.is_valid():
            user = authenticate(
                username=self.cleaned_data['username'],
                password=self.cleaned_data['password'])
        if not user is None:
            if user.is_active:
                # login(self.request, user)
                return self.cleaned_data
            else:
                raise forms.ValidationError(
                    "Sorry. Your account is not active. Most likely is that you didn't confirm your registration")
        else:
            raise forms.ValidationError("Mots de passe ou Nom de d'ultilisateur incorect")

class ResgisterForm(forms.Form):
    username = forms.CharField()
    email =  forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password" ,widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        print(username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")

        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is taken")
        return email
    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError("Passwords must match.")
        return data

class ContactForm(forms.Form):
    fullname = forms.CharField(
            widget=forms.TextInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Your full name"
                    }
                    )
            )
    email    = forms.EmailField(
            widget=forms.EmailInput(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Your email"
                    }
                    )
            )
    content  = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class': 'form-control',
                    "placeholder": "Your message"
                    }
                )
            )

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("Email has to be gmail.com")
        return email