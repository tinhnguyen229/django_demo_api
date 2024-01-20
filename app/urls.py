from django.urls import path
from . import views


urlpatterns = [
    # path('', views.home, name='home'),
    path('get_course_list/', views.get_course_list, name='get_course_list'),
    path('create_course', views.post_course, name='create_course'),
    path('get_course_detail/<id>/', views.get_course_detail, name='get_course_detail'),
]