from django.shortcuts import render


def index(request):
    return render(request, 'main/index.html')

def fridrih_engels(request):
    return render(request, 'main/fridrih_engels.html')

def karl_marks(request):
    return render(request, 'main/karl_marks.html')

def ilych_lenin(request):
    return render(request, 'main/ilych_lenin.html')



