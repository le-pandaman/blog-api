from django.contrib import admin

# Register your models here.
from .models import Blog


class BlogAdmin(admin.ModelAdmin):

    list_display = ['title', 'body', 'pub_date']
    list_filter = ['pub_date', 'title']
    fieldsets = [
        (
            None,
            {
                'fields': [
                    'title',
                    'pub_date',
                    'body',
                ],
            }
        ),
    ]


admin.site.register(Blog, BlogAdmin)
