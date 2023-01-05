from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from uaspbo.models import *


class FormIkan(ModelForm):
    class Meta:
        model = Ikan
        fields = '__all__'

        widgets = {
            'nama' : forms.TextInput({'class':'form-control', 'placeholder':' Masukkan Nama Ikan', 'required':'required'}),
            'nama_ilmiah' : forms.TextInput({'class':'form-control', 'placeholder':' Masukkan Nama Ilmiah', 'required':'required'}),
            'img' : forms.TextInput({'class':'form-control', 'placeholder':'Masukkan LInk Gambar', 'required':'required'}),
            'detail' : forms.URLInput({'class':'form-control', 'placeholder':'Masukkan Link Detail', 'required':'required'}),
            'kelompok_id' : forms.Select({'class':'form-control', 'placeholder':'Pilih kelompok', 'required':'required'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
