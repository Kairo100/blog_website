from django.shortcuts import get_object_or_404, render, redirect
from blogs.models import Category , Blogs
from django.contrib.auth.decorators import login_required
from dashboard.forms import CategoryForm, PostForm
from django.template.defaultfilters import slugify

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



# def for post
#posts
def posts(request):
    posts = Blogs.objects.all()
    context ={
        'posts':posts
    }
    return render(request, 'dashboard/posts.html',context)

# adding posts button
#add_posts
def add_posts(request):
    if request.method == "POST":
         forms = PostForm(request.POST, request.FILES)
         if forms.is_valid():
             post = forms.save(commit=False)
             post.author =request.user
            
             title =forms.cleaned_data['title']
             post.slug = slugify(title)
             post.save()
             return redirect('posts')
             
         else:
             print(forms.errors)
    forms = PostForm()
    context ={ 
        'forms':forms
    }
    return render(request , 'dashboard/add_posts.html',context)

# edit pots
def edit_posts(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    if request.method == "POST":
       forms = PostForm(request.POST,request.FILES,instance=post)
       if forms.is_valid():
           post = forms.save()
           title = forms.cleaned_data['title']
           post.slug =slugify(title)
           post.save()
           return redirect('posts')


    forms = PostForm(instance=post)
     
    context ={
        'forms':forms,
        'post':post
    }
    return render (request,'dashboard/edit_posts.html', context)

#delete_posts
def delete_posts(request,pk):
    post = get_object_or_404(Blogs, pk=pk)
    post.delete()
    return redirect('posts')

