from django import forms
from client.models import Record


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = "__all__"
