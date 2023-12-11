from django import forms
from .models import Servicio

class ServicioForm(forms.ModelForm):
   

    class Meta: 
        #Espeficiar a que modelo está asociado el formulario
        model = Servicio

        fields = [
            'servicio',
            'calificacion',
        ]

        labels = {
            'servicio':'servicio',
            'calificacion':'calificacion',
        }

        widgets = {
            'servicio':forms.TextInput(attrs={'class':'form-control','rows':3}),
            'calificacion':forms.NumberInput(attrs={'class':'form-control'})
        }
    
    def __init__(self, *args, **kwargs):
        super(ServicioForm, self).__init__(*args, **kwargs)
        self.fields['servicio'].error_messages = {'required': 'custom required message'}

        # if you want to do it to all of them
        for field in self.fields.values():
            field.error_messages = {'required':'El campo {fieldname} es obligatorio'.format(
                fieldname=field.label)}