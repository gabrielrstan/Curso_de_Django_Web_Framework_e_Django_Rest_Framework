from django.urls import path
from rest_framework.routers import SimpleRouter

from authors.views import (dashboard, login_create, login_view, logout_view,
                           register_create, register_view)
from authors.views.api import AuthorViewSet
from authors.views.dashboard_recipe import (DashboardRecipe,
                                            DashboardRecipeCreate,
                                            DashboardRecipeDelete)
from authors.views.profile import ProfileView

app_name = 'authors'
author_api_route = SimpleRouter()
author_api_route.register('api', AuthorViewSet, basename='author-api')

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register/create/', register_create, name='register_create'),
    path('login/', login_view, name='login'),
    path('login/create/', login_create, name='login_create'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/recipe/new/', DashboardRecipeCreate.as_view(),
         name='dashboard_recipe_new'),
    path('dashboard/recipe/delete/', DashboardRecipeDelete.as_view(),
         name='dashboard_recipe_delete'),
    path('dashboard/recipe/<int:id>/edit/', DashboardRecipe.as_view(),
         name='dashboard_recipe_edit'),
    path('profile/<int:id>/', ProfileView.as_view(), name='profile'),

]

urlpatterns += author_api_route.urls
