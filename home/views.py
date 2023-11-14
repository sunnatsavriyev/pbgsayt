from .form import *
from .models import *
from django.contrib import messages 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
# Create your views here.

def index(request):

    return render(request, 'index.html')

def reseler_account(request):
        projectss= AccountModel.objects.filter(turi='reseler account')
        # view = AccountModel.objects.get(id = resid)
        # view.view += 1
        # view.save()
        ctx={
            'projectss':projectss,
            # 'view':view
        }

        return render(request, 'reseller.html',ctx )
    

@login_required() 
def addaccountview(request,profilid):
    profile_id = ProfileModel.objects.get(id=profilid)
    if request.method == "POST":
        form = AccountForm(request.POST, request.FILES, instance=profile_id)
        if form.is_valid():
            level = form.cleaned_data['level']
            price = form.cleaned_data['price']
            acount_image = form.cleaned_data['acount_image'] 
            rp = form.cleaned_data['rp']
            turi = form.cleaned_data['turi']    
            mifik = form.cleaned_data['mifik']    
            qoshimcha = form.cleaned_data['qoshimcha']
            murojaat_uchun = form.cleaned_data['murojaat_uchun']    
            profil_data = AccountModel(level=level,price=price,mifik=mifik,qoshimcha=qoshimcha,acount_image=acount_image, profil=profile_id, rp=rp,turi=turi,murojaat_uchun=murojaat_uchun)
            profil_data.save()
            return redirect('account_page')

        else:
            print('error')
            return redirect('addacount')
        
    elif request.method == "POST":
        form = AccountForm(request.POST, request.FILES, instance=profile_id)
        if form.is_valid():
            level = form.cleaned_data['level']
            price = form.cleaned_data['price']
            acount_image = form.cleaned_data['acount_image'] 
            rp = form.cleaned_data['rp']
            turi = form.cleaned_data['reseler account']    
            mifik = form.cleaned_data['mifik']    
            qoshimcha = form.cleaned_data['qoshimcha']
            murojaat_uchun = form.cleaned_data['murojaat_uchun']    
            profil_data = AccountModel(level=level,price=price,mifik=mifik,qoshimcha=qoshimcha,acount_image=acount_image, profil=profile_id, rp=rp,turi=turi,murojaat_uchun=murojaat_uchun)
            profil_data.save()
            return redirect('reseller')

        else:
            return redirect('addacount')
    form = AccountForm()
    accounts = AccountModel.objects.filter(profil_id = profile_id)
    ctx ={
        'form':form,
        'accounts': accounts,
        'profilid':profilid
    }
    
    return render(request, 'addacount.html',ctx)



def Userlogin(request):
    if request.POST:
        username = request.POST["UserName"]
        password = request.POST["password"]

        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'xush kelipsiz')
            return redirect('index')
        else:
            messages.error(request, 'xato username yoki passwordda')

    form = LoginForm()
    ctx = {
        "form": form,
        
    }
    return render(request, 'login.html',ctx)
    
    
def UserLogout(request):
    logout(request)
    return redirect('login')

# def sign(request):
#     if  request.method == 'POST':
#         form =SignupForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else :
#             print("error")
#             return redirect('sign_up')
#     form =SignupForm()
#     ctx = {
#             'form' : form,
#         }
    
#     return render(request, 'sign_up.html',ctx)


@login_required()  
def EditProfilView(request,editid):
    editprofil = ProfileModel.objects.get(id=editid)
    if request.method=="POST":
        form = ProfilForm(request.POST,  request.FILES, instance=editprofil)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('error')
    form = ProfilForm(instance=editprofil)
    profil = ProfileModel.objects.filter(id = editid)
    data = request.user.profilemodel
    print(data)
    ctx={
        'form':form,
        'editprofil':editprofil,
        'profil':profil,
        'data':data
    }
    
    return render(request, 'editprofil.html',ctx)


def account_page(request):
    projects= AccountModel.objects.filter(turi='garant account')
    # view = AccountModel.objects.get(id = accid)
    # view.view += 1
    # view.save()
    ctx={
        'projects':projects,
        # 'view':view
    }

    return render(request, 'account_page.html',ctx )

# Create your views here.



@login_required()
def EditProjectView(request,edit_id):
    edit_account = AccountModel.objects.get(id=edit_id)
    if request.method=="POST":
        form = AccountForm(request.POST, instance=edit_account)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print('error')
    form =AccountForm(instance=edit_account)
    ctx={
        'form':form,
        'edit_account':edit_account
    }
    return render(request, 'edit_account.html', ctx)


@login_required()
def DeleteProjectView(request,delete_id):
    delete_account = AccountModel.objects.get(id=delete_id)
    print(delete_account)
    if request.POST:
        delete_account.delete()
        return redirect('/')
    else:

        ctx={
            'delete_account':delete_account
        }
        return render(request, 'delete_account.html', ctx)