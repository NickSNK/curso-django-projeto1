from django.shortcuts import render, get_list_or_404
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
    recipes = get_list_or_404(Recipe.objects.filter(category__id=id, is_published=True).order_by('-id'))
    context = {
        'title': f'{recipes[0].category.name}',
        'recipes': recipes,
    }
    return render(request, 'recipes/pages/category.html', context)

def recipe(request, id):
    recipes = Recipe.objects.get(id=id)
    context = {
        'title': f'{recipes.title}',
        'recipe': recipes,
        'is_detail_page': True,
    }
    return render(request, 'recipes/pages/recipe.html', context)