from django.urls import path

app_name = "masterclass"

urlpatterns = [
    path("", BooksList.as_view(), name="books_list"),

]
