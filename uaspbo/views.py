from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from uaspbo.models import *
from uaspbo.forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as authlogin





# Create your views here.
@login_required(login_url='login')

def home(request):

    ikans = Ikan.objects.all()
    data = {
        'Title' : "Home",
        'ikans' : ikans,
    }
    return render(request, 'home.html', data)

@login_required(login_url='login')
def lokasi(request):
    data = {
        'Title' : "Lokasi",
    }
    return render(request, 'lokasi.html', data)

@login_required(login_url='login')
def ikandilindungi(request):
    ikans = Ikan.objects.all()
    data = {
        'Title' : "Halaman Ikan Dilindungi",
        'ikans' : ikans,
    }
    return render(request, 'halamanberanda.html', data)

@login_required(login_url='login')
def halamandetail1(request):
    ikans = Ikan.objects.all()
    data = {
        'Title' : "Pari Sungai Tutul",
        'ikans' : ikans,
    }
    return render(request, 'halamandetail1.html', data)

@login_required(login_url='login')
def halamandetail2(request):
    ikans = Ikan.objects.all()
    data = {
        'Title' : "Ikan Balashark",
        'ikans' : ikans,
    }
    return render(request, 'halamandetail2.html', data)

@login_required(login_url='login')
def halamandetail3(request):
    ikans = Ikan.objects.all()
    data = {
        'Title' : "Arwana Jardini",
        'ikans' : ikans,
    }
    return render(request, 'halamandetail3.html', data)

def register(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

def login(request):
    if request.user.is_authenticated:
        return redirect('/home/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                authlogin(request, user)
                return redirect('/home/')

            else:
                messages.info(request, 'Username OR password is incorrect')

        context ={}
        return render(request, 'login.html', context)

def logoutUser(request):
    logout(request)
    messages.info(request, 'Anda berhasil keluar')
    return redirect('/login/')

@login_required(login_url='login')
def tambah_data(request):
    if request.POST:
        form = FormIkan(request.POST)
        if form.is_valid():
            form.save()
            form = FormIkan()
            pesan = 'Data Berhasil Ditambahkan'
            data = {
                'Title' : "Halaman Tambah Ikan",
                'form' : form,
                'pesan' : pesan,
            }
            return render(request, 'tambah_data.html', data)
    else:
        form = FormIkan()
        data = {
            'Title' : "Halaman Tambah Ikan",
            'form' : form,
        }
    return render(request, 'tambah_data.html', data)

@login_required(login_url='login')
def update_data(request, id_ikan):
    ikan = Ikan.objects.get(id = id_ikan)
    if request.POST:
        form = FormIkan(request.POST, instance=ikan)
        if form.is_valid():
            form.save()
            form = FormIkan()
            pesan = 'Data Berhasil Diupdate'
            data = {
                'Title' : "Halaman Edit Ikan",
                'form' : form,
                'pesan' : pesan,
                'ikan' : ikan,
            }
            return render(request, 'update_data.html', data)
    else:
        form = FormIkan(instance=ikan)
        data = {
            'Title' : "Halaman Edit Ikan",
            'form' : form,
            'ikan' : ikan,
        }
    return render(request, 'Update_data.html', data)

@login_required(login_url='login')
def delete_data(request, id_ikan):
    ikan = Ikan.objects.get(id = id_ikan)
    ikan.delete()
    return redirect('/ikandilindungi/')
