from django.urls import path

from .views import (BlogListApiView, BlogCreateApiView, BlogUpdateApiView,
                    BlogDeleteApiView, BlogRetrieveApiView,)


urlpatterns = [
    path('', BlogListApiView.as_view(), name='blog_api_list'),
    path('detail/<int:pk>/', BlogRetrieveApiView.as_view(),
         name='blog_api_retrieve'),
    path('new/', BlogCreateApiView.as_view(), name='blog_api_new'),
    path('edit/<int:pk>/', BlogUpdateApiView.as_view(), name='blog_api_edit'),
    path('delete/<int:pk>/', BlogDeleteApiView.as_view(), name='blog_api_delete'),
]
