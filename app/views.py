# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import  authenticate,login,logout

# Create your views here.
#Página inicial
def home (request):
    return render(request,'home.html')
#Fromulario de cadastro
def create (request):
    return render(request,'create.html')
#Inserção de dados no banco
def store (request):
    data={}
    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class']='alert-danger'
    else:
        user =User.objects.create_user(request.POST['user'],request.POST['email'],request.POST['password'])
        user.first_name=request.POST['name']
        user.save()
        data['msg'] = 'Usuario cadastrado com sucesso'
        data['class']='alert-success'
    
    return render(request,'create.html',data)
#Formulario de login
def  login(request):
    return render(request,'login.html')
#Processa o login
def dologin (request):
    data={}
    user = authenticate(username=request.POST['user'],password=request.POST['password'])
    if user is not None:
        login(request,user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuario ou senha invalidos'
        data['class']='alert-danger'
        return render(request,'painel.html',data)
#Pagina inicial do dashboard
def  dashboard(request):
    return render(request,'dashboard/home.html')
#Logout do sistema
def  logouts(request):
    logout(request)
    return redirect('/login/')
#Alterar a senha
def redmudarsenha(request):
    return render(request,'mudarsenha.html')
def mudarsenha(request):
    user = User.objects.get(email=request.user.email)
    user.set_password(request.POST['password'])
    user.save()
    logout(request)
    return redirect('/painel/')