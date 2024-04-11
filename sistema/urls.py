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
from app.views import mudarsenha, dashboard, home,create, redmudarsenha,store,login,logouts



from app.views import (
    CriarDocente,
    ListDocenteView,
    DetailDocente,
    UpdateDocente,
    DeleteDocente,
)
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
    path('docente/<int:pk>',DetailDocente.as_view(),name='docente_detail'),
    path('docente/<int:pk>/update',UpdateDocente.as_view(),name='docente_update'),
    path('docente/<int:pk>/delete',DeleteDocente.as_view(),name='docente_delete'),

]