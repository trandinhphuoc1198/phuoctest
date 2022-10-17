from django.forms import ModelForm
from django import forms
from .models import Post,PostGerne,Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField(required=False)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class CustomCheckboxInput(forms.CheckboxSelectMultiple):
    attributes={'class':'btn-check'}
    def __init__(self, attrs=attributes, check_test=None):
        super().__init__(attrs)

class PostCreationForm2(ModelForm):
    gerne=forms.ModelMultipleChoiceField(queryset=PostGerne.objects.all(),widget=CustomCheckboxInput)
    class Meta:
        model=Post
        fields=['gerne']
class PostCreationForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
        widgets={
            'title': forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Title'
            }),
            'content': forms.Textarea(attrs={
                'class':"form-control",
                'placeholder':'Content',
                'cols':'50',
                'rows':'20',
                'style':"height: 200px"
            })}

class PostUpdateForm(ModelForm):
    class Meta:
        model=Post
        fields=['title','content']
        widgets={
            'title': forms.TextInput(attrs={
                'class':"form-control",
                'placeholder':'Title'
            }),
            'content': forms.Textarea(attrs={
                'class':"form-control",
                'placeholder':'Content',
                'cols':'50',
                'rows':'20',
                'style':"height: 200px"
            })}

class PostGerneCreationForm(ModelForm):
    class Meta:
        model=PostGerne
        fields=['gerne']

class UserUpdateForm(ModelForm):
    class Meta:
        model=User
        fields=['email']
        widgets={
            'email':forms.EmailInput(attrs={'type':"email", 
                                                'class':"form-control", 
                                                'id':"floatingInput", 
                                                'placeholder':"name@example.com"}),
        }

