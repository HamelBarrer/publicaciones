from django.urls import path

from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.PostListView.as_view(), name='post'),
    path('agregar_publicacion/', views.PostCreateView.as_view(), name='add_post'),
    path('publicacion/<slug:slug>/', views.PostDetailView.as_view(), name='datail_view'),
    path('comentario/', views.create_commentary, name='commentary'),
]
