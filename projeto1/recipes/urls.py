from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from recipes.views.api import RecipeAPIv2ViewSet, tag_api_detail
from recipes.views.site import (RecipeDetail, RecipeDetailAPI,
                                RecipeListViewCategory, RecipeListViewHome,
                                RecipeListViewHomeAPI, RecipeListViewSearch,
                                RecipeListViewTag, theory)

app_name = 'recipes'

recipe_api_v2_router = SimpleRouter()
recipe_api_v2_router.register(
    'recipes/api/v2',
    RecipeAPIv2ViewSet,
    basename='recipes-api',
)

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
    path('recipes/api/v2/tag/<int:pk>/', tag_api_detail,
         name='recipes_api_v2_tag'),
    path('recipes/api/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('recipes/api/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('recipes/api/token/verify/', TokenVerifyView.as_view(),
         name='token_verify'),



]

urlpatterns += recipe_api_v2_router.urls
