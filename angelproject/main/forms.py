from django.forms import ModelForm, TextInput, Textarea
from .models import *


class AdmissionForm(ModelForm):

    class Meta:
        model = Admission
        fields = ['fname', 'lname', 'email', 'message']

        widgets = {
            'fname': TextInput(attrs={
                'placeholder': 'First Name'
            }),
            'lname': TextInput(attrs={
                'placeholder': 'Last Name'
            }),
            'email': TextInput(attrs={
                'placeholder': 'Email'
            }),
            'message': Textarea(attrs={
                'placeholder': 'Message'
            }),
        }