from django.shortcuts import render
from rest_framework import generics


from .models import Blog
from .serializers import BlogListSerializer
# Create your views here.


class BlogListApiView(generics.ListAPIView):

    model = Blog
    queryset = Blog.objects.all()
    serializer_class = BlogListSerializer


class BlogCreateApiView(generics.CreateAPIView):

    model = Blog
    serializer_class = BlogListSerializer


class BlogUpdateApiView(generics.UpdateAPIView):

    model = Blog
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()


class BlogDeleteApiView(generics.DestroyAPIView):

    model = Blog
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()


class BlogRetrieveApiView(generics.RetrieveAPIView):

    model = Blog
    serializer_class = BlogListSerializer
    queryset = Blog.objects.all()
