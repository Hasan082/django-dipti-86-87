from django import forms
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

    isMaried = forms.BooleanField(
        label='isMaried?',
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
        }), required=False
    )

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            if field not in ['isMaried']:
                self.fields[field].widget.attrs.update({'class': 'form-control'})
