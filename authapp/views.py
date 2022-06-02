# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from authapp.models import MyUser
from patinador.models import Patinador 
User = get_user_model()
from .forms import LoginForm, RegistrationForm      

def signin(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            perfilPatinador= forms.cleaned_data['perfilPatinador']
            request.session['username'] = username           
            user = authenticate(username=username, password=password)
            if user:                              
                loginPatinador = MyUser.objects.filter(
                    username=username).values('patinador', 'username','integrante_id')                
                if (loginPatinador[0]['patinador']):                    
                    if (perfilPatinador == '1'):
                        ctrlDespacho = Patinador.objects.filter(integrante_id=loginPatinador[0]['integrante_id']).values('ctrlDespacho')
                        print(ctrlDespacho,"ttttttttttttttttt")
                        
                        
                        if (ctrlDespacho[0]['ctrlDespacho']==''):
                            
                            return redirect('signin')
                        
                        
                        if (ctrlDespacho[0]['ctrlDespacho']):
                            login(request, user) 
                            return redirect('despachoPatinador')  # 80%
                        else:redirect('signin')
                    if(perfilPatinador == '2'):
                        ctrlProduccion = Patinador.objects.filter(
                            integrante_id=loginPatinador[0]['integrante_id']).values('ctrlProduccion')
                        if(ctrlProduccion[0]['ctrlProduccion']):
                            login(request, user)
                            return redirect('produccionPatinador')#80%
                        else:redirect('signin')                    
                    if(perfilPatinador=='3'):                    
                        login(request, user)
                        return redirect('acumuladoPatinador')#80%                    
                    if(perfilPatinador=='4'):
                        ctrlCasino = Patinador.objects.filter(
                            integrante_id=loginPatinador[0]['integrante_id']).values('ctrlCasino')
                        if(ctrlCasino[0]['ctrlCasino']):
                            login(request, user)
                            return redirect('casinoPatinador')#80%                    
                        else:return redirect('signin')
                    else:return redirect('signin')                
                else:                    
                    login(request, user)  
                    return redirect('home')
    context = {
        'form': forms
    }
    return render(request, 'signin.html', context)


def signout(request):
    logout(request)
    return redirect('signin')

def signup(request):
    forms = RegistrationForm()
    if request.method == 'POST':
        forms = RegistrationForm(request.POST)
        if forms.is_valid():
            firstname = forms.cleaned_data['firstname']
            lastname = forms.cleaned_data['lastname']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            confirm_password = forms.cleaned_data['confirm_password']
            if password == confirm_password:
                try:
                    User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
                   
                    return redirect('signin')
                except Exception as e:
                    print(str(e))
                    context = {
                        'form': forms,
                        'error': 'This Username Already exists!'
                    }
                    return render(request, 'signup.html', context)
    context = {
        'form': forms
    }
    return render(request, 'signup.html', context)
