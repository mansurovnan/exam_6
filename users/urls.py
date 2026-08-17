from django.urls import path
from .views import SignUpView, LoginView, logout_view, ProfileView, ProfileEditView, UserListView, UserPostsView, CommentDeleteView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("profile/",ProfileView.as_view(),name="profile"),
    path("profile/edit/",ProfileEditView.as_view(),name="profile_edit"),
    path("users/", UserListView.as_view(), name="user_list"),
    path("users/<int:pk>/posts/", UserPostsView.as_view(), name="user_posts"),
    path("comments/<int:pk>/delete/", CommentDeleteView.as_view(), name="comment_delete"),
    
]