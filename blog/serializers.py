from rest_framework import serializers

from .models import Blog


class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields = ['title', 'body', 'pub_date']
