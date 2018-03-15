from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'w3-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'w3-input'}))


class MessageForm(forms.Form):
    addressee = forms.CharField(label='Кому', widget=forms.TextInput(attrs={'class': 'w3-input'}))
    subject = forms.CharField(label='Тема письма', widget=forms.TextInput(attrs={'class': 'w3-input'}))
    body = forms.CharField(label='Текс сообщения', widget=forms.Textarea(attrs={'class': 'w3-input'}))


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Старый пароль', widget=forms.PasswordInput(attrs={'class': 'w3-input'}))
    new_password = forms.CharField(label='Новый пароль', widget=forms.PasswordInput(attrs={'class': 'w3-input'}))
    repeat_password = forms.CharField(label='Ещу раз новый пароль', widget=forms.PasswordInput(attrs={'class': 'w3-input'}))