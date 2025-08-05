from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    # path('category/<int:category_id>/', views.music_by_category, name='music_by_category'),
]
