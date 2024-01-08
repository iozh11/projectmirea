from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def fridrih_engels(request):
    return render(request, 'main/fridrih_engels.html')