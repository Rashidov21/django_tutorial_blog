from django.urls import path 

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<post_id>', views.detail, name='detail'),
    path('rating/<value>/<post_id>', views.set_rating, name='set_rating'),
    
    path("<category_slug>/posts", views.category_list, name='category_list'),
    path("search/", views.search, name="search")
]
