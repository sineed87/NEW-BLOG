from django.urls import path, include
from .views import blogApiView, categoryApiView, CategoryPostApiView
from rest_framework import routers

router = routers.SimpleRouter()
router.register('blogs', blogApiView, basename='blogs')
router.register('category', categoryApiView, basename='category')
router.register('categoryBasedBlogs', CategoryPostApiView, basename='categoryBasedBlogs')


urlpatterns = [
    path('', include(router.urls))
]
    


