from django.urls import path

from .views import PostCreateView, PostListView, PostDetailView, PostUpdateView, PostDeleteView, LikeView, CommentCreateView, MostViewedPostsView, PostSearchView


urlpatterns = [
    path("posts/create/",PostCreateView.as_view(),name="post_create"),
    path("posts/",PostListView.as_view(),name="post_list"),
    path("posts/<int:pk>/",PostDetailView.as_view(),name="post_detail"),
    path("posts/<int:pk>/update/", PostUpdateView.as_view(), name="post_update"),
    path("posts/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("posts/<int:pk>/like/", LikeView.as_view(), name="post_like"),
    path("posts/<int:pk>/comment/", CommentCreateView.as_view(), name="comment_create"),
    path("posts/most-viewed/", MostViewedPostsView.as_view(), name="most_viewed"),
    path("posts/search/", PostSearchView.as_view(), name="post_search"),

]