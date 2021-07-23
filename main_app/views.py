from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.shortcuts import render, redirect
from .models import Comb
from .models import Goal
from .forms import GoalForm

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
    goals = Goal.objects.all()
    return render(request, 'combs/detail.html', {'comb': comb, 'goals': goals})

class CombCreate(CreateView):
    model = Comb
    fields = '__all__'

class GoalCreate(CreateView):
    model = Goal
    fields = '__all__'

# def add_goal(request, comb_id):
#     form = GoalForm(request.POST)
#     if form .is_valid():
#         new_goal = form.save(commit=False)
#         new_goal.comb_id = comb_id
#         new_goal.save()
#     return redirect('index')

class CombUpdate(UpdateView):
    model = Comb
    fields = ['title', 'description', 'atchieve_by']

class CombDelete(DeleteView):
    model = Comb
    success_url = '/combs/'