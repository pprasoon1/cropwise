from django import forms

class AgriForm(forms.Form):
    state = forms.CharField(max_length=100)
    district = forms.CharField(max_length=100)
    block = forms.CharField(max_length=100, required=False)
    crop = forms.CharField(max_length=100, required=False)
    start_month = forms.ChoiceField(choices=[(str(i), i) for i in range(1, 13)], required=False)

    