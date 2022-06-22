from django import forms
from .models import FamilyMember

class FamilyMemberForm(forms.ModelForm):
    name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={"placeholder" : "Name: "}))
    age = forms.DecimalField(decimal_places=0 ,max_digits=3, widget=forms.TextInput(attrs={"placeholder" : "Age: "}))
    description = forms.CharField(max_length=1000, widget=forms.TextInput(attrs={"placeholder" : "Description: "}))
    #picture = forms.ImageField()

    class Meta:
        model = FamilyMember
        fields = ["name", "age", "description"]