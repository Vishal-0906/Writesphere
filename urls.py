from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("register/", views.register_view, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("post/<int:pk>/", views.post_detail_view, name="post_detail"),
    path("post/new/", views.create_post_view, name="create_post"),
    path("post/<int:pk>/like/", views.like_post_view, name="like_post"),
    path("profile/<int:user_id>/", views.profile_view, name="profile"),
    path("profile/<int:user_id>/follow/", views.follow_author_view, name="follow_author"),
]
