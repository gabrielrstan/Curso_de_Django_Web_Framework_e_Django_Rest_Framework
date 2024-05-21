from django.urls import path

from recipes.views import (RecipeDetail, RecipeDetailAPI,
                           RecipeListViewCategory, RecipeListViewHome,
                           RecipeListViewHomeAPI, RecipeListViewSearch)

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListViewHome.as_view(), name='home'),
    path('recipes/search/', RecipeListViewSearch.as_view(), name='search'),
    path('recipes/category/<int:category_id>/',
         RecipeListViewCategory.as_view(), name='category'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe'),
    path('recipes/api/v1/', RecipeListViewHomeAPI.as_view(),
         name='recipes_api_v1'),
    path('recipes/api/v1/<int:pk>/', RecipeDetailAPI.as_view(),
         name='recipes_api_v1_detail'),

]
