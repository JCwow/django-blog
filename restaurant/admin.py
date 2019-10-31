from django.contrib import admin
from restaurant.models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'pub_date')
admin.site.register(Post, PostAdmin)