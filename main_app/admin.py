from django.contrib import admin

# Register your models here.
from .models import Comb, Goal, Charm

admin.site.register(Comb)
admin.site.register(Goal)
admin.site.register(Charm)