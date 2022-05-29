# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from authapp.models import MyUser




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
            perfilPatinadores=forms.cleaned_data.get('perfilPatinadores')
            request.session['username'] = username
    
    
            user = authenticate(username=username, password=password)
            if user:                              
                loginPatinador  = MyUser.objects.filter(username=username).values('patinador')
                if (loginPatinador[0]['patinador']):                
                    
                    if (int(perfilPatinador) ==1):                     
                        login(request, user)
                        return redirect('despachoPatinador')                                   
                    
                    
                    
                    if(int(perfilPatinador)==2):pass#produccion
                    if(int(perfilPatinador)==3):pass#acumulado
                    if(int(perfilPatinador)==4):pass#casino
                    
                    
                    
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
