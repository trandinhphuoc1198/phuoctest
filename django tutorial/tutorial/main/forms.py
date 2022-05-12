from attr import field, fields
from django.forms import ModelForm
from .models import Room,Message

class Roomform(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
class Messageform(ModelForm):
    class Meta:
        model=Room
        fields='__all__'