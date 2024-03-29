from django.shortcuts import render
from django.http import HttpResponse

from utils.recipes.factory import make_recipe

# Create your views here.
def home(request):
    context = {
        'recipes': [make_recipe() for i in range(3)],
    }
    
    return render(request, 'recipes/pages/home.html', context)

def recipe(request, pk):
    context = {
        'recipe': make_recipe(),
        'is_detail_page': True,
    }
    
    return render(request, 'recipes/pages/recipe.html', context)