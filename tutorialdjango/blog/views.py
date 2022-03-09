from django.views.generic import DateDetailView, ListView 

from .models import Post


class PostListView(ListView):
    model = Post

class PostDetailVeiw(DateDetailView):
    model = Post
