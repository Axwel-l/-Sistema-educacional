# Create your views here.
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import  logout

from django.urls import reverse_lazy
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
    )
from django.views.generic import  ListView, DetailView
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
    return redirect('/login/')


from .models import Docente
# def docente(request):
#     if request.method == 'POST':
#         form = DocenteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = DocenteForm()
#     return render(request, 'docente.html', {'form': form})

class CriarDocente( CreateView):
    model=Docente
    fields=('nome','cpf','data_nascimento','email')
    template_name= 'docenteadd.html'
    success_url = reverse_lazy('list_docente')
class ListDocenteView(ListView):
    model = Docente
    template_name = 'dashboard/docente.html'
    context_object_name='docente'

class DetailDocente(DetailView):
    model = Docente
    template_name= 'docente_detail.html'

class UpdateDocente(UpdateView):
    model =Docente
    template_name= 'docente_update.html'
    fields = ('nome', 'cpf', 'email', 'data_nascimento')
    success_url = reverse_lazy('list_docente')
class DeleteDocente( DeleteView):
    model =Docente
    template_name='docente_delete.html'
    success_url = reverse_lazy('list_docente')