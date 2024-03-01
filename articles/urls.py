from django.urls import path
from . import views

urlpatterns = [path("", views.article_list), path("<slug: article>", views.article_detail)]
