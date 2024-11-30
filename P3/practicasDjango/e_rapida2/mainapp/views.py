from django.shortcuts import render, redirect

# Create your views here.
def index(requets):
    return render(requets, 'mainapp/index.html', {
        'title': 'Inicio',
        'content': '..:: Esta es mi Pagina de Inicio ::..'
    })
def about(requets):
    return render(requets, 'mainapp/about.html', {
        'title': 'Acerca de',
        'content': 'esta es tu ventana de acerca de, bienvenido'
    })
def mision(requets):
    return render(requets, 'mainapp/mision.html', {
        'title': 'Mision',
    })
def vision(requets):
    return render(requets, 'mainapp/vision.html', {
        'title':'Vision'
    })

def error404(requets, exception):
    return render(requets, 'mainapp/404.html')

def register(requets):
    return render(requets, 'users/register.html', {
        'title' : 'Registro de Usuarios',
        'content' : 'Esta es tu pagina de registro de usuarios'
    })

def login_user(requets):
    return render(requets, 'users/login_user.html', {
        'title' : 'Inicio de Usuarios',
        'content' : 'Aqui podras registrar usuarios'
    })