from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

from .forms import FicheForm
from .models import Fiche_de_condidature


def index(request):
    return render(request, 'personal/home.html')

def studentHome(request):
    return render(request, 'personal/student.html')

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("personal:studentHome")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}: {form.error_messages[msg]}")

                #print(form.error_messages[msg])

            return render(request = request,
                          template_name = "personal/register.html",
                          context={"form":form})

    form = UserCreationForm
    return render(request = request,
                  template_name = "personal/register.html",
                  context={"form":form})

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
       # print(uploaded_file.name)
       # print(uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render (request , 'personal/upload.html', context)

def ficheList(request):
    fiches = Fiche_de_condidature.objects.all()
    return render(request, 'personal/fiches.html' , {
        'fiches' : fiches
    })


def uploadFiche(request):
    if request.method == 'POST':
        form = FicheForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('ficheList')
    else:
        form = FicheForm()
        
    return render(request, 'personal/upfiche.html' ,{
        'form': form
    })







