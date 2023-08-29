from django.db import models

### 순서
## 1. python manage.py makemigrations
## 2. python manage.py migrate로 db에 적용시킨다.
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/', blank=True)
    # 처음 저장하는 시점
    created_at = models.DateTimeField(auto_now_add=True)
    # 마지막으로 저장하는 시점
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}/'