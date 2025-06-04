from django.urls import path
from . import views

urlpatterns = [
    path("blogpost/",views.BlogPostListCreate.as_view(), name="blog-view-create"),

    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestroy.as_view(),
        name="update",
    ),

]
