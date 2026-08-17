from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import PostForm, Post
from .models import Post, Like
from django.http import HttpResponseForbidden

class PostListView(View):

    def get(self, request):

        posts = Post.objects.all()

        return render(
            request,
            "blog/post_list.html",
            {
                "posts": posts
            }
        )

class PostCreateView(View):

    def get(self, request):

        form = PostForm()
        return render(request,"blog/post_create.html",{"form": form})

    def post(self, request):

        form = PostForm(request.POST,request.FILES)

        if form.is_valid():

            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect("post_list")

        return render(request,"blog/post_create.html",{"form": form})




class PostDetailView(View):

    def get(self, request, pk):

        post = get_object_or_404(Post,pk=pk)
        return render(request,"blog/post_detail.html",{"post": post})

class PostUpdateView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.author != request.user:
            return HttpResponseForbidden("You cannot edit this post.")

        form = PostForm(instance=post)
        return render(request, "blog/post_update.html", {"form": form, "post": post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.author != request.user:
            return HttpResponseForbidden("You cannot edit this post.")

        form = PostForm(request.POST, request.FILES, instance=post)

        if form.is_valid():
            form.save()
            return redirect("post_detail", post.pk)

        return render(request, "blog/post_update.html", {"form": form, "post": post})

class PostDeleteView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.author != request.user:
            return HttpResponseForbidden("You cannot delete this post.")

        return render(request, "blog/post_delete.html", {"post": post})

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)

        if post.author != request.user:
            return HttpResponseForbidden("You cannot delete this post.")

        post.delete()
        return redirect("post_list")
class LikeView(View):
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
        else:
            Like.objects.create(user=request.user, post=post)

        return redirect("post_detail", pk=pk)


