
from .models import Product
from django import forms

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder" : "Yoouur title: "}))
    description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField() 
    reviews = forms.CharField()

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get("title")
        if "CFE" in title:
            return title
        else:
            raise forms.ValidationError("not valid title")    

    class Meta:
        model = Product
        fields = [
            "title", 
            "description",
            "price",
            "reviews"
        ]



class RawProductForm(forms.Form):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder" : "Yoouur title: "}))
    description = forms.CharField(required=False, widget=forms.Textarea)
    price = forms.DecimalField() 
    reviews = forms.CharField()
