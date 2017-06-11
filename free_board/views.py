from django.shortcuts import render
from django.views.generic import ListView

from .models import Post
# Create your views here.

class PostLV(ListView):
    model = Post
    template_name = 'free_board/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2


