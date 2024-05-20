from django.urls import path

from recipes.views import (RecipeDetail, RecipeListViewCategory,
                           RecipeListViewHome, RecipeListViewSearch)

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListViewHome.as_view(), name='home'),
    path('recipes/search/', RecipeListViewSearch.as_view(), name='search'),
    path('recipes/category/<int:category_id>/',
         RecipeListViewCategory.as_view(), name='category'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe'),

]
