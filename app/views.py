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

from .models import Aluno, Docente, Disciplina
FAluno = Aluno
FDocente=Docente
FDisciplina=Disciplina


def minha_view(request):
    form1 = Aluno()
    form2 = Docente()
    return render(request, 'dashboard/home.html', {'form1': form1, 'form2': form2})
# Docente
class CriarDocente( CreateView):
    model=Docente
    fields=('nome','cpf','data_nascimento','email')
    template_name= 'dashboard/Docente/docenteadd.html'
    success_url = reverse_lazy('list_docente')
class ListDocenteView(ListView):
    model = Docente
    template_name = 'dashboard/Docente/docente.html'
    context_object_name='docentes'

class UpdateDocente(UpdateView):
    model =Docente
    template_name= 'dashboard/Docente/docente_update.html'
    fields = ('nome', 'cpf', 'email', 'data_nascimento')
    success_url = reverse_lazy('list_docente')
class DeleteDocente( DeleteView):
    model =Docente
    template_name='dashboard/Docente/docente_delete.html'
    success_url = reverse_lazy('list_docente')

def pesquisardocente(request):
    query = request.GET.get('q')
    resultados = Docente.objects.filter(nome__icontains=query)
    return render(request, 'dashboard/Docente/docente.html', {'resultados': resultados, 'query': query})
    


# Aluno
class CriarAluno( CreateView):
    model=Aluno
    fields=('nome','cpf','data_nascimento','email')
    template_name= 'dashboard/Aluno/alunoadd.html'
    success_url = reverse_lazy('list_aluno')
class ListAluno(ListView):
    model = Aluno
    template_name = 'dashboard/Aluno/aluno.html'
    context_object_name='alunos'

class UpdateAluno(UpdateView):
    model =Aluno
    template_name= 'dashboard/Aluno/aluno_update.html'
    fields=('nome','cpf','data_nascimento','email')
    success_url = reverse_lazy('list_aluno')
class DeleteAluno( DeleteView):
    model =Aluno
    template_name='dashboard/Aluno/aluno_delete.html'
    success_url = reverse_lazy('list_aluno')

def pesquisaraluno(request):
    query = request.GET.get('q')
    resultados = Aluno.objects.filter(nome__icontains=query)
    return render(request, 'dashboard/Aluno/aluno.html', {'resultados': resultados, 'query': query})





# Disciplina
class CriarDisciplina( CreateView):
    model=Disciplina
    fields=('nome','data_criacao')
    template_name= 'dashboard/Disciplina/Dadd.html'
    success_url = reverse_lazy('list_disciplina')
class ListDisciplina(ListView):
    model = Disciplina
    template_name = 'dashboard/Disciplina/Disciplina.html'
    context_object_name='disciplinas'

class UpdateDisciplina(UpdateView):
    model =Disciplina
    template_name= 'dashboard/Disciplina/D_update.html'
    fields = ('nome','data_nascimento')
    success_url = reverse_lazy('list_disciplina')
class DeleteDisciplina( DeleteView):
    model =Disciplina
    template_name='dashboard/Disciplina/D_delete.html'
    success_url = reverse_lazy('list_disciplina')

def pesquisardisciplina(request):
    query = request.GET.get('q')
    resultados = Disciplina.objects.filter(nome__icontains=query)
    return render(request, 'dashboard/Disciplina/disciplina.html', {'resultados': resultados, 'query': query})