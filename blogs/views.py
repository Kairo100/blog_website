from django.shortcuts import render,redirect ,get_object_or_404,HttpResponse
from .models import Blogs, Category  # Ensure 'Blogs' is the correct model name
from django.db.models import Q # from db to use search contains keyword multiple or searching
def posts_by_category(request, category_id):
    # Fetch the posts that belong to the category with id category_id
    posts = Blogs.objects.filter(status='published', category=category_id)
    #use try if u want to do some custom action or else 404 error 
    try:
     category = Category.objects.get(pk=category_id)
    except:
       return redirect ('home')
    # this  use when you want to customize your own 404 page to catch error
    # category = get_object_or_404 (Category, pk=category_id)
    context = {
        'posts': posts,
        'category':category
    }
    
    return render(request, 'posts_by_category.html', context)


#blogs single page blogs
def blogs(request,slug):
   #models slug 
   single_post =  get_object_or_404(Blogs, slug=slug , status ='published')
   context = {
      'single_post':single_post
   }
   return render(request, 'blogs.html', context)


# search function
def search(request):
   keyword = request.GET.get('keyword')
   blogs = Blogs.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(short_description__icontains=keyword))
   context ={
      'blogs':blogs,
      'keyword': keyword
   }
   return render(request, 'search.html', context)
