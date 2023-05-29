from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('write',views.write,name='write'),
    path('about',views.about,name='about'),
    path('post_detail/<int:pk>/',views.post_detail,name='post_detail'),
    path('post_edit/<int:pk>/',views.post_edit,name='post_edit'),
    path('post_delete/<int:pk>/',views.post_delete,name='post_delete')
]
