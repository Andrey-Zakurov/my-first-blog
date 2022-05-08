from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from  .help_create import Help_create
from .forms import PostForm

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

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk = post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form':form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
