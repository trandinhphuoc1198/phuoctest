from .models import Profile
from django import forms

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['nick_name','gender','birthday']
        widgets={
            'nick_name': forms.TextInput(attrs={'class':"form-control", 
                                                'placeholder':"Jack Sparrow"}),
            'gender': forms.Select(attrs={'class':"form-select"}),
            'birthday': forms.DateInput(format=('%Y-%m-%d'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
class UpdateProfileImageForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=['image']
        labels={'image':"Picture"}
        widgets={'image': forms.FileInput(attrs={'type':"file", 
                                            'class':"form-control",
                                            'id':'formFile'
                                            })                                
        }