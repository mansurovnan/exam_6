from django.shortcuts import render
from django.views import View
from blog.models import Post





class HomeView(View):
    def get(self, request):
        recent_posts = Post.objects.all()[:5]
        return render(request, "core/home.html", {"recent_posts": recent_posts})
