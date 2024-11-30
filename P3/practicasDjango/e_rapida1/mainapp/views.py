from django.shortcuts import render

# Create your views here.
def index(requets):
    return render(requets, 'mainapp/index.html', {
        'title':'Inicio | Pagina Principal',
        'content':'.:: Binevenido a mi pagina principal ::.'
    })

def about(requets):
    return render(requets, 'mainapp/about.html',{
        'title':'Acerca de',
        'content':'.:: Somos un equipo de Desarrolo de SW con Django'
    })

def mision(requets):
    return render(requets, 'mainapp/mision.html',{
        'title':'Mision',
    })

def vision(requets):
    return render(requets, 'mainapp/vision.html',{
        'title':'Vision',
    })