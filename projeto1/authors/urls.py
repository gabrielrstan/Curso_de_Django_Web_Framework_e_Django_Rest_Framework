from django.urls import path

from authors.views import (dashboard, dashboard_recipe_edit,
                           dashboard_recipe_new, login_create, login_view,
                           logout_view, register_create, register_view)

app_name = 'authors'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('register/create/', register_create, name='register_create'),
    path('login/', login_view, name='login'),
    path('login/create/', login_create, name='login_create'),
    path('logout/', logout_view, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/recipe/new/', dashboard_recipe_new,
         name='dashboard_recipe_new'),
    path('dashboard/recipe/<int:id>/edit/', dashboard_recipe_edit,
         name='dashboard_recipe_edit'),

]
