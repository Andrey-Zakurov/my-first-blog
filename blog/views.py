from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, Comment_form




def post_list(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    context = {'posts':posts}
    return render(request, 'blog/post_list.html', context)


def post_detail(request, pk):
    print(type(request), pk, type(pk))
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post_id=pk)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        # ---------------------------
        print(post.author, '\n', post.text, '\n',)
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


def comment_post_create(request, pk):
    if request.method == "POST":
        form = Comment_form(request.POST)
        if form.is_valid():
            com = form.save(commit=False)
            com.author = request.user
            com.post_id = pk
            com.published_date = timezone.now()
            com.save()
            return redirect('post_detail', pk=com.post_id)
    else:
        form = Comment_form()
    return render(request, 'blog/comment_pub.html', {'form': form})


def comment_list(request, pk):
    pass
