from django.urls import path
from . import views
urlpatterns = [
    path('',views.ArticleAPI.as_view(),name="index"),
    path('<int:article_id>/',views.ArticleDetail.as_view(),name = "article_view")
]