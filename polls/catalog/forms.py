from django import forms


class InputForms(forms.Form):
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    roll_number = forms.IntegerField(help_text="minimum 6 digit required")

class EmployeeForm():
    first_name = forms.CharField(max_length=200)
    last_name = forms.CharField(max_length=200)
    contact_number = forms.IntegerField(label="contact number",required=True)
    email = forms.EmailField(label="Email")
    file = forms.FileField()
