from django.shortcuts import render
from django.http import FileResponse, Http404

# Create your views here.


def index(request):
    
    return render(request, 'site_est/index.html')

def elements(request):
    
    return render(request, 'site_est/elements.html')

def generic(request):
    
    return render(request, 'site_est/generic.html')

def aula(request):
        
    return render(request, 'site_est/aula.html')

def web(request):
        
    return render(request, 'site_est/web.html')

def edu(request):
        
    return render(request, 'site_est/edu.html')

def labs(request):
        
    return render(request, 'site_est/labs.html')

def lab01(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_yamin_fernanda.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab02(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_marina.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab03(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_diegod.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab04(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_patrick.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab05(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_joao.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab06(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_meu.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab07(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_cristiane.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()

def lab08(request):
    try:
        return FileResponse(open('site_est/static/site_est/labs/lab_carolzinha.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()


