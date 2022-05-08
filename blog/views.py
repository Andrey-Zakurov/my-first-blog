from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from  .help_create import Help_create

# Create your views here.

br = Help_create()

def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    print(type(posts))
    print('-----------')
    print(posts.count)
    print('-----------')
    print(dir(posts))
    br.line_string()
    print(dir(render))
    print('-----------')
    br.line_string()
    print(br.line_string())
    context = {'posts':posts}
#    context = {1: 123, 2:125}
    return render(request, 'blog/post_list.html', context)

def post_detail(request,pk):
     post = get_object_or_404(Post, pk=pk)
     return render(request, 'blog/post_detail.html', {'post': post})
