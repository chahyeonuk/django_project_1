from django.contrib import admin
from .models import Post, Category, Tag, Comment

# 1. admin 페이지에 DB를 적용할 model를 작성해준다.
# 2. model에서 추가한 테이블을 admin.py에 추가

admin.site.register(Post)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comment)