from django.urls import path

from .views import *
from comments.views import comment_create

urlpatterns = [
    path('', blog_post_list_view),
    path('<str:slug>/', blog_post_detail_view),
    path('<str:slug>/edit/', blog_post_update_view),
    path('<str:slug>/delete/', blog_post_delete_view),

    path('<str:slug>/comment/', comment_create),
    
]
