from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ["name", "department","status", "salary"]

        labels={
            "name":"Name",
            "department":"Department",
            "salary":"Salary",
            "status":"Active"
        }

        help_texts={
            "salary":"Enter the monthly salary in INR"
        }

        error_messages = {
            "name": {
                "required": "Employee name is required."
            },
            "department": {
                "required": "Department cannot be empty.",
                "invalid": "Please enter your department."
            }
        }

        widgets = {
            "name": forms.TextInput(attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter employee name"
            }),
            "department": forms.TextInput(attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter department"
            }),
            "salary": forms.NumberInput(attrs={
                "class": "w-full border border-gray-300 rounded-lg px-4 py-3 mb-1 focus:outline-none focus:ring-2 focus:ring-blue-500",
                "placeholder": "Enter salary"
            }),
            "status": forms.CheckboxInput(attrs={
                "class": "w-5 h-5 ml-7 mr-3 text-blue-600 rounded focus:ring-blue-500"
            })
        }

