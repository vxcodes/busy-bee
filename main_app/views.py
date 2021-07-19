from django.shortcuts import render
from .models import Comb
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def combs_index(request):
    combs = Comb.objects.all()
    return render(request, 'combs/index.html', {'combs': combs})

def combs_detail(request, comb_id):
    comb = Comb.objects.get(id=comb_id)
    return render(request, 'combs/detail.html', {'comb': comb})