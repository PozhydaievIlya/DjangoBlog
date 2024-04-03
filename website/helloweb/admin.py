from django.contrib import admin
from .models import Post, Category, Person, Tag, UsersEmail, Comments, Profile

# Register your models here.


admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Tag)
admin.site.register(UsersEmail)
admin.site.register(Comments)
admin.site.register(Profile)