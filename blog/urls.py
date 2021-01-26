from django.urls import path

from .views import PostDetail, PostFilter, PostList

urlpatterns = [
    path("", PostList.as_view(), name="post_list"),
    path("<slug:slug>/", PostDetail.as_view(), name="post_single"),
    path(
        "category/<slug:category_pk>", PostFilter.as_view(), name="post_category_filter"
    ),
]
