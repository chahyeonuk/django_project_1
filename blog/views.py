from .models import Post
from django.views.generic import ListView, DetailView

# html내에서는 post_list라는 딕셔너리가 자동으로 인식
class PostList(ListView):
    model = Post
    ordering = '-pk'
 
# # Create your views here.
# def index(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(
#         request,
#         'blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

class PostDetail(DetailView):
    model = Post
