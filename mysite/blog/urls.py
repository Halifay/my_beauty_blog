from django.urls import path
from . import views


app_name = 'blog'
urlpatterns = [
    path('', views.post_info, name='index'),
    path('detail/<int:post_id>/', views.post_info, name='post_info'),
    path('leave_a_comment/<int:post_id>', views.leave_a_comment,
         name='leave_a_comment')

]
