from django.urls import path
from apps.base.views import index,news_detail
urlpatterns = [
    path('', index, name="index"),
    path("news_detail:<int:id>/", news_detail, name="news_detail")
]