from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
def index (request):
    return render(request,'index.html')


def signup(request):
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})  # Renderiza el formulario HTML
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], 
                    password=request.POST['password1']
                )
                user.save()
                return HttpResponse('Usuario creado satisfactoriamente')
            except:
                return HttpResponse('El usuario ya existe')    
        return HttpResponse('Las contraseñas no coinciden')

      


        