from django.urls import path
from . import views

app_name = 'config'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('answer/', views.AnswerView, name='answer'),
]