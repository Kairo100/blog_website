from django.urls import path
from . import views


urlpatterns = [
   path ('', views.dashboard , name ='dashboard' ),
   path('categories/',views.categories, name='categories'),
   path('categories/add',views.add_categories, name='add_categories'),

    
]