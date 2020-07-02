from django import forms


class EmployeeForm(forms.Form):
    fullname = forms.CharField(max_length=30, required=True, label="Fullname")
    job = forms.CharField(max_length=10, required=True, label="Job")
    salary = forms.IntegerField(required=True, label="Salary")
