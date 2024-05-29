from django.urls import path

from recipes.views.api import (RecipeAPIv2Detail, RecipeAPIv2List,
                               tag_api_detail)
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
    path('recipes/api/v2/', RecipeAPIv2List.as_view(), name='recipes_api_v2'),
    path('recipes/api/v2/<int:pk>/', RecipeAPIv2Detail.as_view(),
         name='recipes_api_v2_detail'),
    path('recipes/api/v2/tag/<int:pk>/', tag_api_detail,
         name='recipes_api_v2_tag'),

]
