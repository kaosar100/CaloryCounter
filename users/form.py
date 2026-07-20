from django import forms
from .models import PersonalInfo

class PersonalInfoForm(forms.ModelForm):
    class Meta:
        model = PersonalInfo
        
        def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)

             for field in self.fields.values():
                  if isinstance(field.widget, forms.Select):
                      field.widget.attrs["class"] = "form-select"
                  else:
                      field.widget.attrs["class"] = "form-control"
        
        exclude = [
            'user',
            'created_at',
            'updated_at',
        ]
    
        widgets = {
            "age": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "sex": forms.Select(attrs={
                "class": "form-select"
            }),

            "height": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "weight": forms.NumberInput(attrs={
                "class": "form-control"
            }),

            "goal": forms.Select(attrs={
                "class": "form-select"
            }),

            "activity_level": forms.Select(attrs={
                "class": "form-select"
            }),
        }