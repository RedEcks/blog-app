from django.urls import path
from . import views 
import re



urlpatterns = [
    path("", views.article_list),
    path("<slug:slug>",views.article_detail)
]
