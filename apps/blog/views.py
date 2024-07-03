from django.shortcuts import render
from apps.blog.models import Recipe

# Create your views here.
def homepage(request):
    recipes = Recipe.objects.all()
    return render(
        request, "blog/home.html", 
        {'recipes': recipes}
    )

def detail(request, recipe_id):
    try:
        recipe = Recipe.objects.get(pk=recipe_id)
    except Recipe.DoesNotExist:
        raise Http404("Recipe doesn not exist")
    return render(
        request,
        "blog/recipe-details.html",
        {"recipe":recipe}
    )