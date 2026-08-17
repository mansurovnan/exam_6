from django.urls import path

from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, LikeView


urlpatterns = [
    path("posts/create/",PostCreateView.as_view(),name="post_create"),
    path("posts/",PostListView.as_view(),name="post_list"),
    path("posts/<int:pk>/",PostDetailView.as_view(),name="post_detail"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<int:pk>/like/", LikeView.as_view(), name="post_like"),

]