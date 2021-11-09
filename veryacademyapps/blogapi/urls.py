from django.urls import path
from .views import ArticleList, ArticleDetail

app_name = "blogapi"

urlpatterns = [
    path("<int:pk>/", ArticleDetail.as_view(), name="detailcreate"),
    path("", ArticleList.as_view(), name="listcreate"),
]
