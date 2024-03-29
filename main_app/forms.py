from django.forms import ModelForm

from .models import Goal

class GoalForm(ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_title', 'goal_description']