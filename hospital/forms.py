from django import forms

class LabReportForm(forms.Form):
    report = forms.FileField()
