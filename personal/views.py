from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
from .forms import NewUserForm
from django.http import HttpResponse
import pandas as pd 
from .forms import FicheForm, NewUserForm
from .models import Fiche_de_condidature
from django.http import JsonResponse
import numpy as np
from django import forms
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.decorators import user_passes_test

from django.contrib.auth.mixins import UserPassesTestMixin


def index(request):
    return render(request, 'personal/home.html')



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New account created: {username}")
            login(request, user)
            return redirect("personal:login_request")

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


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect('/uploadfiche')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "personal/login.html",
                    context={"form":form})





def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("personal:index")


def studentHome(request):
    return render(request, 'personal/upload.html')




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














'''class MyView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser
'''

def check_admin(user):
   return user.is_superuser 


#@method_decorator(login_required)
#@login_required(check_admin)
#@login_required

#@permission_required("personal.view_fiche_de_condidature")
@user_passes_test(lambda u: u.is_superuser)
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
            return redirect("personal:upload")
    else:
        form = FicheForm()
        
    return render(request, 'personal/upfiche.html' ,{
        'form': form
    })






def panda(request):
    result = ''
    #if request.method == 'post':
    sheet1 = pd.read_excel(r'C:\Users\Pc\Desktop\PFA\excel1.xlsx') 
    sheet2 = pd.read_excel(r'C:\Users\Pc\Desktop\PFA\excel2.xlsx') 
    sheet1.equals(sheet2)
    comparison_values = sheet1.values == sheet2.values
    print (comparison_values)
    #return JsonResponse({'bbb': comparison_values})
    rows,cols=np.where(comparison_values==False)
    for item in zip(rows,cols):
        sheet1.iloc[item[0], item[1]] = '{} --> {}'.format(sheet1.iloc[item[0], item[1]],sheet2.iloc[item[0], item[1]])
    #sheet1.to_excel('./Excel_diff.xlsx',index=False,header=True)
    sheet1.to_html('./personal/templates/personal/homee.html',index=False,header=True)
    '''text_file = open("Excel_diff.xlsx", "w")
    text_file.write(html)
    text_file.close()'''
    #context = {'comparison_values': comparison_values}
    return render(request, 'personal/homee.html' )







