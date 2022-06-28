from django.urls import path
from .views import PostCreateView
from .views import PostListView
from .views import PostDetailView
from .views import PostUpdateView
from .views import PostDeleteView
from . import views

  
app_name = "blog" 
  
urlpatterns = [ 
     path("", views.PostListView.as_view(), name="all"), 
     path("create/", views.PostCreateView.as_view(), name="post_create"), 
     path("delete/<slug:slug>", views.PostDeleteView.as_view(), name="post_delete"), 
     path("update/<slug:slug>", views.PostUpdateView.as_view(), name="post_update"), 
     path("read/<slug:slug>", views.PostDetailView.as_view(), name="post_detail"), 
  
 ]


