from django.urls import path

from recipes.views import category, home, recipe, search

app_name = 'recipes'

urlpatterns = [
    path('', home, name='home'),
    path('recipes/search/', search, name='search'),
    path('recipes/category/<int:category_id>/', category, name='category'),
    path('recipes/<int:id>/', recipe, name='recipe'),

]
