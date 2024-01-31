from django.urls import path, include
# from rest_framework import routers
from rest_framework.routers import SimpleRouter
from . import views

app_name = 'main'

# router = routers.DefaultRouter()
router = SimpleRouter()
router.register(r'api/review', views.ReviewApiView)

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/', views.detail, name='detail'),
    path('<int:article_id>/review/', views.review, name='review'),
    path('<int:article_id>/review/leave_comment', views.leave_comment, name='leave_comment'),
    path('', include(router.urls))
]