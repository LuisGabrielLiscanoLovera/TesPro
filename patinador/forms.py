from django import forms
from integrante.models import Integrante
from patinador.models import Patinador

class PatinadorCreationForm(forms.ModelForm):

    class Meta:
        model = Patinador
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['Integrante'].queryset = Integrante.objects.none()

        if 'Integrante' in self.data:
            self.fields['Integrante'].queryset = Integrante.objects.all()

        elif self.instance.pk:
            self.fields['Integrante'].queryset = Integrante.objects.all().filter(pk=self.instance.Integrante.pk)



''' from django import forms
from .models import *

class CustomerForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput) '''