from django.urls import path 

from . import views

app_name = "blog"

urlpatterns = [
    path('', views.home_page, name='home'),
    path('detail/<post_id>', views.detail, name='detail'),
    
]
