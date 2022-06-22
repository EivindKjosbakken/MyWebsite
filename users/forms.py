from .models import User
from django import forms


class UserForm(forms.ModelForm):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"placeholder" : "Your name: "})) 
    age = forms.DecimalField(decimal_places=2, max_digits=10000)
    gender = forms.CharField(max_length=10)
    description = forms.CharField(max_length=150)
    
    
    def cleanName(self, *args, **kwargs):
        name = self.cleaned_data.get("name")
        if not "@" in name:
            return name
        else:
            raise forms.ValidationError("not valid name")

    class Meta:
        model = User
        fields = ["name", "age", "gender", "description"]  