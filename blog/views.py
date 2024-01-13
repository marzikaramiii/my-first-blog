from django.shortcuts import render,get_object_or_404,redirect
from .models import Post,Comment,Tag
from django.utils import timezone
from .forms import PostForm,CommentForm

# Create your views here.
def post_list(request):
    posts=Post.objects.filter(publish_date__lte=timezone.now()).order_by('publish_date')
    return render(request,'blog/post_list.html', {'posts':posts})



def post_detail(request,pk):
    post=get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})
    

def post_new(request):
    if request.method == 'POST':
        form =PostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            tags = form.cleaned_data['tags']
            post.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'blog/post_edit.html',{'form':form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            # Clear existing tags for the post
            post.tags.clear()

            # Get selected tags from the form and add them to the post
            tags = form.cleaned_data['tags']
            post.tags.add(*tags)
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_draft_list(request):
    posts=Post.objects.filter(publish_date__isnull=True).order_by('created_date')
    return render(request,'blog/post_draft_list.html',{'posts': posts})

def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail',pk=pk)


def post_remove(request,pk):
     post = get_object_or_404(Post, pk=pk)
     post.delete()
     return redirect('post_list')


def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('post_detail',pk=comment.post.pk)

def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.delete()
    return redirect('post_detail',pk=comment.post.pk)


def list_posts_by_tag(request,tag_id):
    tag = get_object_or_404(Tag,id = tag_id)
    posts = Post.objects.filter(publish_date__lte=timezone.now(),tags= tag)
    context = {
        "tag_name": tag.title,
        "posts": posts
    }
    return render(request,'blog/post_list.html',context)