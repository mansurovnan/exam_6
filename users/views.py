from django.shortcuts import render,redirect
from .models import CustomUser
from django.views import View
from .forms import SignUpForm, LoginForm, ProfileEditForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'users/signup.html',{'form':form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.set_password(form.cleaned_data['password'])

            user.save()
            return redirect('home')
        return render(request, 'users/signup.html', {'form':form})

class LoginView(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'users/login.html', {'form':form})

    def post(self, request):
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            form.add_error("username",
            "Username or password is wrong")

        return render(request,"users/login.html",{"form": form})

def logout_view(request):
    logout(request)
    return redirect("login")

class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        user = request.user
        return render(request, 'users/profile.html', {'user':user})
    
class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request):
        form = ProfileEditForm(instance=request.user)

        return render(request,'users/profile_edit.html',{'form': form})
    def post(self, request):
        form = ProfileEditForm(
            request.POST,
            instance=request.user
        )

        if form.is_valid():
            form.save()
            return redirect('profile')

        return render(
            request,
            'users/profile_edit.html',
            {'form': form}
        )

class UserListView(LoginRequiredMixin, View):
    def get(self, request):
        users = CustomUser.objects.all()

        for user in users:
            user.post_count = Post.objects.filter(author=user).count()

        return render(request, 'users/user_list.html', {'users': users})

class UserPostsView(LoginRequiredMixin, View):
    def get(self, request, pk):
        user = CustomUser.objects.get(pk=pk)
        posts = Post.objects.filter(author=user)
        return render(request, 'users/user_posts.html', {'user': user, 'posts': posts})
    



    





