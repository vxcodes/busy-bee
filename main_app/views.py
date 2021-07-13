from django.shortcuts import render

#TODO: temporary comb class for testing purposes
class Comb():
    def __init__(self, title, description, combs):
        self.title = title
        self.description = description
        self.combs = combs

combs = [
    Comb('Self Dev', 'Working on myself', ['do homework', 'plant plants']),
    Comb('Work', 'Responsibility!', ['Accountability', 'Do work!']),
    Comb('Have Fun', 'Yoga time!', ['Hiking time!', 'yay time!']),
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def combs_index(request):
    return render(request, 'combs/index.html', {'combs': combs})