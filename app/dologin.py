from app.views import login


from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


def dologin (request):
    data={}
    user = authenticate(username=request.POST['user'],password=request.POST['password'])
    if user is not None:
        login(request,user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuario ou senha invalidos'
        data['class']='alert-danger'
        return render(request,'login.html',data)