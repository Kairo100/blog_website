from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Category , Blogs
from django.contrib.auth.decorators import login_required
from dashboard.forms import CategoryForm

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count
    blogs_count = Blogs.objects.all().count
    context= {
        'category_count':  category_count,
        'blogs_count':blogs_count 

    }
    return render(request, 'dashboard/dashboard.html' , context)

# categories
def categories(request):
    return render(request,'dashboard/categories.html')

#add categories
def add_categories(request):
    if request.method == "POST":
         forms = CategoryForm(request.POST)
         if forms.is_valid():
             forms.save()
             return redirect('categories')
             
    else:
        forms = CategoryForm()
    context ={ 
        'forms':forms
    }
    return render(request , 'dashboard/add_categories.html',context)


# edit categories

def edit_categories(request,pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
       forms = CategoryForm(request.POST,instance=category)
       if forms.is_valid():
           forms.save()
           return redirect('categories')


    forms = CategoryForm(instance=category)
     
    context ={
        'forms':forms,
        'category':category
    }
    return render (request,'dashboard/edit_categories.html', context)


# delete 
def delete_categories(request , pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

