from django.urls import path

from recipes.views.api import recipe_api_list
from recipes.views.site import (RecipeDetail, RecipeDetailAPI,
                                RecipeListViewCategory, RecipeListViewHome,
                                RecipeListViewHomeAPI, RecipeListViewSearch,
                                RecipeListViewTag, theory)

app_name = 'recipes'

urlpatterns = [
    path('', RecipeListViewHome.as_view(), name='home'),
    path('recipes/search/', RecipeListViewSearch.as_view(), name='search'),
    path('recipes/tags/<slug:slug>/',
         RecipeListViewTag.as_view(), name='tag'),
    path('recipes/category/<int:category_id>/',
         RecipeListViewCategory.as_view(), name='category'),
    path('recipes/<int:pk>/', RecipeDetail.as_view(), name='recipe'),
    path('recipes/api/v1/', RecipeListViewHomeAPI.as_view(),
         name='api_v1'),
    path('recipes/api/v1/<int:pk>/', RecipeDetailAPI.as_view(),
         name='api_v1_detail'),
    path('recipes/theory/', theory, name='theory'),
    path('recipes/api/v2/', recipe_api_list, name='recipes_api_v2'),

]
