from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:post_id>/', views.post_info, name='post_info'),
    path('', views.comments_view, name='comments_view'),

]
