from django import forms
from . models import Participant

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        exclude = ['status']
        labels = {
            'first_name' : 'Nombre',
            'last_name' : 'Apellido',
            'document' : 'Documento',
            'email' : 'Email',
        }
        widgets ={
            'first_name': forms.TextInput(attrs={'placeholder': 'Ingrese nombre'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Ingrese apellido'}),
            'document': forms.TextInput(attrs={'placeholder': 'Ingrese documento'}),
            'email' : forms.EmailInput(attrs={'placeholder': 'Ingrese email'}),
}
