from django import forms
from .models import Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        
        def __init__(self, *args, **kwargs):
             super().__init__(*args, **kwargs)

             for field in self.fields.values():
                  if isinstance(field.widget, forms.Select):
                      field.widget.attrs["class"] = "form-select"
                  else:
                      field.widget.attrs["class"] = "form-control"
        
        exclude = (
            'user',
            'created_at',
            'updated_at',
        )
        widgets = {
    "food_name": forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "Enter food name"
    }),

    "meal_type": forms.Select(attrs={
        "class": "form-select"
    }),

    "quantity": forms.NumberInput(attrs={
        "class": "form-control"
    }),

    "calory": forms.NumberInput(attrs={
        "class": "form-control"
    }),

    "meal_date": forms.DateInput(attrs={
        "class": "form-control",
        "type": "date"
    }),
}
    