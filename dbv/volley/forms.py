from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *



class FeedbackForm(forms.ModelForm):
    captcha=CaptchaField()
    class Meta:
        model=Feedback
        fields=['title', 'content', 'email']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-input'}),
            'content':forms.Textarea(attrs={'cols':30,'rows':8}),
            'email':forms.TextInput(attrs={'class':'form-input'}),
        }


    def clean_title(self):
        title=self.cleaned_data['title']
        if len(title)>30:
            raise ValidationError('Количество символов превышает 30')
        return title


    def clean_content(self):
        content=self.cleaned_data['content']
        if len(content)>250 or len(content)<30:
            raise ValidationError('Недопустимое количество символов')
        return content


    def clean_email(self):
        email=self.cleaned_data['email']
        if len(email)<5 or len(email)>30 or email[-2:]=='ru':
            raise ValidationError('Недопустимый email')
        return email


class ApplicationForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ApplicationForm, self).__init__(*args,**kwargs)
        self.fields['tour_category'].empty_label='Категория не выбрана'

    captcha = CaptchaField()

    class Meta:
        model=Application
        fields = ['team_name', 'tour_category', 'player_1', 'player_2', 'city', 'phone']
        widgets = {
            'team_name': forms.TextInput(attrs={'class': 'form-input'}),
            'tour_category': forms.TextInput(attrs={'class': 'form-input'}),
            'player_1': forms.TextInput(attrs={'class': 'form-input'}),
            'player_2': forms.TextInput(attrs={'class': 'form-input'}),
            'city': forms.TextInput(attrs={'class': 'form-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-input'}),
        }

        def clean_tour_category(self):
            tour_category = self.cleaned_data['tour_category']
            if str(tour_category)!= 'Основная сетка' or str(tour_category)!= 'Ветераны' or str(tour_category)!= 'Женщины':
                raise ValidationError('Существуют только следующие категории: "Основная сетка", "Ветераны" и "Женщины"!')
            return tour_category


        def cleaned_phone(self):
            phone=self.cleaned_data['phone']
            if type(phone) is not int:
                raise ValidationError('Недопустимый номер телефона!')
            return phone



class RegisterUserForm(UserCreationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    first_name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={'class': 'form-input'}))
    last_name = forms.CharField(label='Фамилия', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))

    class Meta:
        model=User
        fields=('username','password1','password2','first_name','last_name','email')


class LoginForm(AuthenticationForm):
    username=forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class':'form-input'}))


