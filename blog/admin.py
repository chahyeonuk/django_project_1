from django.contrib import admin
from .models import Post

# admin 페이지에 DB를 적용할 model를 작성해준다.
# Register your models here.

admin.site.register(Post)
