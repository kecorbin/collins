from django import forms
from discover.models import Job


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['destination', 'ports']
