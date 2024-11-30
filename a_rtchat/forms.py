from django.forms import ModelForm
from django import forms
from .models import *

class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Mandar mensagem ...', 'class': 'p-4 text-black', 'maxlength': '300', 'autofocus': True}),
        }