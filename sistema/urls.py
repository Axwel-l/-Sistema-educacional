"""
URL configuration for sistema project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
from django.contrib import admin
from django.urls import path
from app.dologin import dologin
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',login),
    path('create/',create),
    path('store/',store),
    path('login/',login),
    path('dologin/',dologin),
    path('dashboard/',dashboard),
    path('logouts/',logouts),
    path('mudarsenha/',mudarsenha),
    path('redmudarsenha/',redmudarsenha),



    path('docente/add',CriarDocente.as_view(),name='create_docente'),
    path('docente',ListDocenteView.as_view(),name='list_docente'),
    path('docente/<int:pk>/update',UpdateDocente.as_view(),name='docente_update'),
    path('docente/<int:pk>/delete',DeleteDocente.as_view(),name='docente_delete'),
    path('pesquisarDocente/',pesquisardocente, name='pesquisar_docente'),



    path('aluno/add',CriarAluno.as_view(),name='create_aluno'),
    path('aluno',ListAluno.as_view(),name='list_aluno'),
    path('aluno/<int:pk>/update',UpdateAluno.as_view(),name='aluno_update'),
    path('aluno/<int:pk>/delete',DeleteAluno.as_view(),name='aluno_delete'),
    path('pesquisarAluno/',pesquisaraluno, name='pesquisar_aluno'),
    
    
    
    path('disciplina/add',CriarDisciplina.as_view(),name='create_disciplina'),
    path('disciplina',ListDisciplina.as_view(),name='list_disciplina'),
    path('disciplina/<int:pk>/update',UpdateDisciplina.as_view(),name='disciplina_update'),
    path('disciplina/<int:pk>/delete',DeleteDisciplina.as_view(),name='disciplina_delete'),
    path('pesquisarDisciplina/',pesquisardisciplina, name='pesquisar_disciplina'),

]