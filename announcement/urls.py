from django.urls import path
from announcement.views import *

urlpatterns = [
    path("", ItemListAPIView.as_view()),
    path("<int:pk>/", ItemDetailAPIView.as_view()),
    path("create/", ItemCreateAPIView.as_view()),

]
