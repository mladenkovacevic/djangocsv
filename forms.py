import io
from django import forms

from django.contrib.auth.models import User

import csv

class DataForm(forms.Form):
    datafile = forms.FileField()

    def clean_datafile(self):
        f = self.cleaned_data['datafile']
        if f:
            ext = f.name.split('.')[-1]
            if ext != 'csv':
                raise forms.ValidationError('File Type not Supported')
        return f

    def process_data(self):
        f = io.TextIOWrapper(self.cleaned_data['datafile'].file)
        reader = csv.DictReader(f)

        for user in reader:
            User.objects.create_user(user['username'], first_name=user['firstname'], last_name=user['lastname'], email=user['email'])
