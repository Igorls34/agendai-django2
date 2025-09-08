from django import forms
from .models import Appointment, Service

class BookingForm(forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = Appointment
        fields = ['customer_name', 'customer_email', 'customer_phone', 'notes']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class': 'input'}),
            'customer_email': forms.EmailInput(attrs={'class': 'input'}),
            'customer_phone': forms.TextInput(attrs={'class': 'input'}),
            'notes': forms.Textarea(attrs={'rows': 3, 'class': 'input'}),
        }

    def __init__(self, *args, **kwargs):
        self.service = kwargs.pop('service', None)
        super().__init__(*args, **kwargs)
        self.fields['date'].widget.attrs.update({'class': 'input'})
        self.fields['time'].widget.attrs.update({'class': 'input'})

    def clean(self):
        cleaned = super().clean()
        if not self.service:
            raise forms.ValidationError('Serviço inválido.')
        return cleaned
