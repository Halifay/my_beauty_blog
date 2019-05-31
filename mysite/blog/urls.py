from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post_info, name='post_info'),
    path('<int:post_id>/comments/', views.comments_view, name='comments_view'),

]
