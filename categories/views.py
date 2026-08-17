from django.shortcuts import render, redirect
from django.views import View
from .forms import CategoryForm
from .models import Category


class CategoryListView(View):

    def get(self, request):
        categories = Category.objects.all()

        return render(
            request,
            "categories/category_list.html",
            {"categories": categories}
        )

class CategoryCreateView(View):
    def get(self, request):
        form = CategoryForm
        return render(request,"categories/category_create.html",{"form": form})

    def post(self, request):
        form = CategoryForm(request.POST,request.FILES)

        if form.is_valid():
            form.save()

            return redirect("category_list")

        return render(request,"categories/category_create.html",{"form": form})
class CategoryDetailView(View):

    def get(self, request, pk):
        category = Category.objects.get(pk=pk)
        return render(request,"categories/category_detail.html",{"category": category})
    
class CategoryUpdateView(View):

    def get(self, request, pk):

        category = Category.objects.get(pk=pk)
        form = CategoryForm(instance=category)

        return render(
            request,
            "categories/category_update.html",
            {"form": form,"category": category})

    def post(self, request, pk):

        category = Category.objects.get(pk=pk)
        form = CategoryForm(request.POST,request.FILES,instance=category)

        if form.is_valid():
            form.save()
            return redirect("category_detail",pk=category.pk)

        return render(request,"categories/category_update.html",{"form": form,"category": category})

class CategoryDeleteView(View):

    def get(self, request, pk):

        category = Category.objects.get(pk=pk)

        return render(
            request,
            "categories/category_delete.html",
            {
                "category": category
            }
        )

    def post(self, request, pk):

        category = Category.objects.get(pk=pk)

        category.delete()

        return redirect("category_list")
        