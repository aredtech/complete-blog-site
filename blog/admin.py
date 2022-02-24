from django.contrib import admin
from .models import UserProfile, Post, Author, Tags, ContactMe, Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(UserProfile)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tags)
admin.site.register(Comment)
admin.site.register(ContactMe)


