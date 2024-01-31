from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/review/', views.review, name='review'),
    path('<int:article_id>/review/leave_comment', views.leave_comment, name='leave_comment'),

]