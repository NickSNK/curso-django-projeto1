from django.shortcuts import render
from django.http import HttpResponse

from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context)

def category(request, id):
    recipes = Recipe.objects.filter(category__id=id, is_published=True).order_by('-id')
    context = {
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/home.html', context)

def recipe(request, id):
    recipes = Recipe.objects.get(id=id)
    context = {
        'recipe': recipes,
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe.html', context)